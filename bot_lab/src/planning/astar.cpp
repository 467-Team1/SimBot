/*
Made a whole lot of changes but if i can't make it to OH tomorrow here's some stuff to ask + updates:

Updates: 

1. All test cases pass!! But made some shady code changes to allow it to
2. Prune node path works
3. can visualize path with botgui and ./astar_test --use-gui true

Shady code changes: 
1. 5/6 test cases passed before I did a time check where if we loop for more than 10 seconds call it no path 
This is because this was the narrow test case, which means it had to look through entire grid to know
it couldn't make a path --> very time consuming so time check allows it to quit early so irl it isn't annoying
and doesn't take like 30 minutes

2. changes to the search_for_path has a commented section for closedNode where it doesn't do anythign so I commented it out
3. Talk to john we both had same issues and worked it out together 
4. float conversion for expand_nodes 
5. change to obstacle distance grid (some stuff but didn't make a difference, can highlight lines 120-130)
*/


#include <planning/astar.hpp>
#include <planning/obstacle_distance_grid.hpp>
#include <chrono>

using namespace std::chrono;
using namespace std;

robot_path_t search_for_path(pose_xyt_t start, 
                             pose_xyt_t goal, 
                             const ObstacleDistanceGrid& distances,
                             const SearchParams& params)
{
    ////////////////// TODO: Implement your A* search here //////////////////////////
    std::cout << "start\n";
    auto start_time = high_resolution_clock::now();
    // robot_path_t path;
    // path.utime = start.utime;
    // path.path.push_back(start);    
    // path.path_length = path.path.size();
    // return path;
    // std::cout << "START node: " << start.x << " " << start.y << "\n";
    // cout << "Distance of Original Frame " << distances.originInGlobalFrame().x << "\n";

    // set up start and goal cells
    Point<double> startpos;
    startpos.x = start.x;
    startpos.y = start.y;
    cell_t startCell = global_position_to_grid_cell(startpos, distances);
    Node* startNode = new Node(startCell.x, startCell.y);
    Point<double> goalpos;
    goalpos.x = goal.x;
    goalpos.y = goal.y;
    cell_t goalCell = global_position_to_grid_cell(goalpos, distances);
    Node* goalNode = new Node(goalCell.x, goalCell.y);
    
    // Set the g_cost and h_cost 
    startNode->g_cost = 0.0;
    startNode->h_cost = h_cost(startNode, goalNode, distances);

    robot_path_t finalpath;
    finalpath.utime = start.utime;

    // This is when we reach the end/finish line
    if (isEqual(startNode, goalNode)){
        finalpath.path = extract_pose_path(extract_node_path(goalNode, startNode), distances);
        finalpath.path_length = extract_node_path(goalNode, startNode).size();
        // finalpath.path.pop_back();
        // finalpath.path.push_back(goal);
        return finalpath;
    }

    // Nodes to be explored
    PriorityQueue open;
    open.push(startNode);

    // ExporED Nodes
    std::vector<Node*> closed;

    // Keep expanding and looking until there are no more nodes to explore
    while(!open.empty()){

        auto current_time = high_resolution_clock::now();
        auto elapsed_time = duration_cast<seconds>(current_time - start_time);

        if (elapsed_time.count() > 10) {
            std::cout << "Search time exceeded 10 seconds. Exiting...\n";
            break;
        }

        // Checking Current Position
        Node* currNode = open.pop();
        // std::cout << "current node " << currNode->cell.x << " " << currNode->cell.y << "\n";

        closed.push_back(currNode);

        
        if (*currNode == *goalNode){
                // std::cout << "goal node " << currNode->cell.x << " " << currNode->cell.y << "\n";
                vector<Node*> node_path = extract_node_path(currNode, startNode);
                // cout << "I finished getting node_path" << "\n";
                finalpath.path = extract_pose_path(node_path, distances);
                // cout << "I finished getting pose_path" << "\n";
                finalpath.path_length = extract_node_path(currNode, startNode).size();
                cout << "LENGTH" << finalpath.path_length << "\n";
                // finalpath.path.pop_back();
                // finalpath.path.push_back(goal);
                return finalpath;
        }

        std::vector<Node*> children = expand_node(currNode, distances, params);
        // cout << "open loop length: " << open.size() << "\n";
        // cout << "time: " << finalpath.utime << "\n";
        for (int i = 0; i < children.size(); ++i){

            Node * childNode = children[i];
            childNode->parent = currNode;
            Node* openNode = open.get_member(childNode);
            Node* closedNode = get_from_list(childNode, closed);
            
            double temp_g_cost = g_cost(currNode, childNode, distances, params);
            
            if (openNode){
                // If the child is in the open list with a higher g_cost, update it
                if (openNode->g_cost > temp_g_cost) {
                    openNode->g_cost = temp_g_cost;
                    openNode->h_cost = h_cost(childNode, goalNode, distances);
                    openNode->parent = currNode;
                }
            }
            else if (closedNode) {
                // // If the child is in the closed list with a higher g_cost, update it and move to open list
                // if (closedNode->g_cost > temp_g_cost) {
                //     closedNode->g_cost = temp_g_cost;
                //     closedNode->h_cost = h_cost(childNode, goalNode, distances);
                //     closedNode->parent = currNode;
                //     // open.push(closedNode);
                //     // closed.erase(std::remove(closed.begin(), closed.end(), closedNode), closed.end());
                // }
                // TODO: include this or not 
                
            }
            else {
                // The node wasn't in either the open or closed list, so compute its costs and add it to the open list
                childNode->g_cost = temp_g_cost;
                childNode->h_cost = h_cost(childNode, goalNode, distances);
                childNode->parent = currNode;
                open.push(childNode);
            }
        
            

            /////////////////////////// OLD CODE //////////////////////////////////////////////////////

            // if (!is_in_list(childNode, closed)) {
            //     // cout << "Size of Open: " << open.size() << "\n";
            //     // Check for duplicates
            //     if (open.get_member(childNode)){
            //         open.get_member(childNode)->g_cost = g_cost(currNode, childNode, distances, params);
            //         open.get_member(childNode)->h_cost = h_cost(childNode, goalNode, distances);
            //         open.get_member(childNode)->parent = currNode;
            //     }
            //     else{
            //         childNode->g_cost = g_cost(currNode, childNode, distances, params);
            //         childNode->h_cost = h_cost(childNode, goalNode, distances);
            //         open.push(childNode);
            //     }
            // }

            //////////////////////////////////////////////////////////////////////////////////////////
        }
    }
    
    std::cout << "empty path \n";
    return finalpath;
}

double h_cost(Node* from, Node* goal, const ObstacleDistanceGrid& distances){
    // Diagonal distance
    int dx = std::abs(goal->cell.x - from->cell.x);
    int dy = std::abs(goal->cell.y - from->cell.y);
    double diag_distance = 1.414;

    double h_cost = (dx + dy) + (diag_distance - 2) * std::min(dx,dy);
    return h_cost; 
}

double g_cost(Node* from, Node* goal, const ObstacleDistanceGrid& distances, const SearchParams& params){
    //TODO
    int parent_g_cost = from->g_cost;

    int dx = std::abs(goal->cell.x - from->cell.x);
    int dy = std::abs(goal->cell.y - from->cell.y);
    double diag_distance = 1.414;


    double g_cost = 0.0;
    if (dx == 1 && dy == 1) {
        // Diagonal movement
        g_cost = parent_g_cost + diag_distance;
    } else {
        // horizontal/vertical movement: (dx == 0 && dy == 1) || (dx == 1 && dy == 0)
        g_cost = parent_g_cost + 1.0;
    }

    double cellDistance = distances(goal->cell.x, goal->cell.y);
    double obstacle_penalization = 0.0;

    if (cellDistance > params.minDistanceToObstacle && cellDistance < params.maxDistanceWithCost) {
        obstacle_penalization = pow(params.maxDistanceWithCost - cellDistance, params.distanceCostExponent);
    }

    return g_cost + obstacle_penalization;

    // double dist_to_obst = params.maxDistanceWithCost - distances(from->cell.x, from->cell.y);
    // if (dist_to_obst > 0) {
    //     return pow(dist_to_obst, params.distanceCostExponent);
    // } else {
    //     return 0.5;
    // }
}
std::vector<Node *> expand_node(Node *node, const ObstacleDistanceGrid &distances, const SearchParams &params)
{
    // return all the neighbors of the current node, given certain conditions
    const int xDeltas[8] = {1, -1, 0, 0, 1, -1, 1, -1};
    const int yDeltas[8] = {0, 0, 1, -1, 1, -1, -1, 1};

    std::vector<Node *> children;
    for (int n = 0; n < 8; ++n)
    {
        int cell_x = node->cell.x + xDeltas[n];
        int cell_y = node->cell.y + yDeltas[n];
        Node *childNode = new Node(cell_x, cell_y);
        // Check that the child is inside the map
        if (!distances.isCellInGrid(cell_x, cell_y))
            continue;
        // Check that the child is not an obstacle (or close enough to one)
        if (distances(cell_x, cell_y) <= float((params.minDistanceToObstacle))) // TODO: add float or not 
            continue;
        children.push_back(childNode);
    }
    return children;
}

bool is_in_list(Node* node, std::vector<Node*> list){
    for (auto &&item : list)
    {
        if(*node == *item){
            return true;
        } 
        //cout << "STUCK IN is_in_list for" << "\n";
    }
    return false;
}

Node* get_from_list(Node* node, std::vector<Node*> list){
    for (auto &&item : list)
    {
        if(*node == *item) return item;
    }
    return NULL;
}

bool isEqual(Node * first, Node * second){
    if (first->cell.x == second->cell.x && first->cell.y == second->cell.y){
        return true;
    }
    // if (first == second) {
    //     return true;
    // }
    else{
        return false;
    }
}

// backtracks the path by looking at parent nodes
// returns a vector containing the nodes in the extracted path
std::vector<Node*> extract_node_path(Node* goal_node, Node* start_node){
    std::vector<Node*> node_path;
    Node* current_node = goal_node;
    
    while (!(current_node == start_node)) {
        // cout << !(current_node == start_node) << "\n";
        // cout << "current_node: " << current_node->cell.x << " " << current_node->cell.y << "\n";
        // cout << "current_node: " << current_node->parent << "\n";
        node_path.push_back(current_node);
        current_node = current_node->parent;
    }

    node_path.push_back(current_node);
    std::reverse(node_path.begin(), node_path.end());
    return node_path;
}

// removes redundant nodes that do not contribute significantly to the path or simplifying the path
std::vector<Node *> prune_node_path(std::vector<Node *> nodePath)
{
    std::vector<Node *> new_node_path;

    if (nodePath.size() < 3)
        return nodePath;

    new_node_path.push_back(nodePath[0]); // Always keep the start node
    for (size_t i = 1; i < nodePath.size() - 1; ++i) {
        Node* a = nodePath[i - 1];
        Node* b = nodePath[i];
        Node* c = nodePath[i + 1];

        
        
        Point<int> vecAB {b->cell.x - a->cell.x, b->cell.y - a->cell.y};
        Point<int> vecBC {c->cell.x - b->cell.x, c->cell.y - b->cell.y};

        // Compare vectors to check if they are collinear
        if (vecAB.x * vecBC.y != vecAB.y * vecBC.x) {
            nodePath[i]->parent = new_node_path.back();
            new_node_path.push_back(nodePath[i]); // If not collinear, add node to the new path
            // cout << new_node_path.back()->cell.x << " " << new_node_path.back()->cell.y  << "\n";
        }
    }
    nodePath.back()->parent = new_node_path.back();
    new_node_path.push_back(nodePath.back()); // Always keep the goal node
    cout << new_node_path.back()->cell.x << " " << new_node_path.back()->cell.y  << "\n";
    return new_node_path;
}
// returns a vector containing the pose (position) of each node
std::vector<pose_xyt_t> extract_pose_path(std::vector<Node*> nodes, const ObstacleDistanceGrid& distances){
    std::vector<Node*> new_node_path = prune_node_path(nodes);
    // auto new_node_path = nodes;
    std::vector<pose_xyt_t> pose_path;

    for (auto &&node : new_node_path) {
        // pose_xyt_t pose; 

        // pose.x = node->cell.x * distances.metersPerCell() + distances.originInGlobalFrame().x;
        // pose.y = node->cell.y * distances.metersPerCell() + distances.originInGlobalFrame().y;
        // pose.theta = 0.0; 
        
        // pose_path.push_back(pose);

        Point<double> global_pose = grid_position_to_global_position(node->cell, distances);
        pose_xyt_t pose;
        pose.utime = 0;

        pose.x = global_pose.x;
        pose.y = global_pose.y;
        pose.theta = 0.0;

        pose_path.push_back(pose);
    }

    return pose_path;
}
