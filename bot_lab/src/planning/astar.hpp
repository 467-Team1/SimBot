#ifndef PLANNING_ASTAR_HPP
#define PLANNING_ASTAR_HPP

#include <lcmtypes/robot_path_t.hpp>
#include <lcmtypes/pose_xyt_t.hpp>

#include <planning/obstacle_distance_grid.hpp>
#include <common/grid_utils.hpp>
#include <queue>

typedef Point<int> cell_t;

struct Node
{
    double h_cost;
    double g_cost;
    Node* parent;
    cell_t cell;
    bool visited;
    Node(int a, int b) : h_cost(1.0E16), g_cost(1.0E16), parent(NULL), cell(a,b), visited(false){}

    double f_cost(void) const {return h_cost + g_cost;}
    bool operator==(const Node& rhs) const {
        return (cell==rhs.cell);
    }
};

struct Compare_Node
{
    bool operator() (Node* n1, Node* n2)
    {
        if (n1->f_cost() == n2->f_cost())
        {
            return n1->h_cost > n2->h_cost;
        } 
        else {
            return n1->f_cost() > n2->f_cost();
        }
    }
};

struct PriorityQueue
{
    std::priority_queue<Node*, std::vector<Node*>, Compare_Node> Q;
    std::vector<Node*> elements;

    bool empty()
    {
        return Q.empty();
    }

    bool is_member(Node* n) {
        for (auto &&node : elements)
        {
            if(*n == *node) return true;
        }
        return false;
    }

    Node* get_member(Node* n) {
        for (auto &&node : elements)
        {
            if(*n == *node) return node;
        }
        return NULL;
    }

    Node* pop(){
        Node* n = Q.top();
        Q.pop();
        int idx = -1;

        for (unsigned i = 0; i < elements.size(); i++) {
            if (*elements[i] == *n) {
                idx = i;
                break;
            }
        }
        elements.erase(elements.begin() + idx);
        return n;
    }

    void push(Node* n) {
        Q.push(n);
        elements.push_back(n);
    }

    int size() {
        return Q.size();
    }
};

class ObstacleDistanceGrid;

/**
* SearchParams defines the parameters to use when searching for a path. See associated comments for details
*/
struct SearchParams
{
    double minDistanceToObstacle;   ///< The minimum distance a robot can be from an obstacle before
                                    ///< a collision occurs
                                    
    double maxDistanceWithCost;     ///< The maximum distance from an obstacle that has an associated cost. The planned
                                    ///< path will attempt to stay at least this distance from obstacles unless it must
                                    ///< travel closer to actually find a path
                                    
    double distanceCostExponent;    ///< The exponent to apply to the distance cost, whose function is:
                                    ///<   pow(maxDistanceWithCost - cellDistance, distanceCostExponent)
                                    ///< for cellDistance > minDistanceToObstacle && cellDistance < maxDistanceWithCost
};

//functions to implement
double h_cost(Node* from, Node* goal, const ObstacleDistanceGrid& distances);
double g_cost(Node* from, Node* goal, const ObstacleDistanceGrid& distances, const SearchParams& params);
std::vector<Node*> expand_node(Node* node, const ObstacleDistanceGrid& distances, const SearchParams& params);

bool isEqual(Node * first, Node * second);
std::vector<Node*> extract_node_path(Node* goal_node, Node* start_node);
std::vector<Node*> prune_node_path(std::vector<Node*> nodePath);

std::vector<pose_xyt_t> extract_pose_path(std::vector<Node*> nodes, const ObstacleDistanceGrid& distances);

bool is_in_list(Node* node, std::vector<Node*> list);
Node* get_from_list(Node* node, std::vector<Node*> list);

/**
* search_for_path uses an A* search to find a path from the start to goal poses. The search assumes a circular robot
* 
* \param    start           Starting pose of the robot
* \param    goal            Desired goal pose of the robot
* \param    distances       Distance to the nearest obstacle for each cell in the grid
* \param    params          Parameters specifying the behavior of the A* search
* \return   The path found to the goal, if one exists. If the goal is unreachable, then a path with just the initial
*   pose is returned, per the robot_path_t specification.
*/
robot_path_t search_for_path(pose_xyt_t start, 
                             pose_xyt_t goal, 
                             const ObstacleDistanceGrid& distances,
                             const SearchParams& params);

#endif // PLANNING_ASTAR_HPP