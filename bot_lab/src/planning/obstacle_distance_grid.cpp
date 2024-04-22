#include <planning/obstacle_distance_grid.hpp>
#include <slam/occupancy_grid.hpp>


ObstacleDistanceGrid::ObstacleDistanceGrid(void)
: width_(0)
, height_(0)
, metersPerCell_(0.05f)
, cellsPerMeter_(20.0f)
{
}

void ObstacleDistanceGrid::initializeDistances(const OccupancyGrid& map) 
{
    int width = map.widthInCells();
    int height = map.heightInCells();

    for (int y = 0; y < height; ++y) {
        for (int x = 0; x < width; ++x) {
            if (map.logOdds(x,y) < 0) {
                distance(x,y) = -1.0;
            }
            else {
                distance(x,y) = 0.0;
            }
        }
    }
}

bool is_cell_free(cell_t cell, const OccupancyGrid& map) {
    return map.logOdds(cell.x, cell.y) <= 0;
}

bool is_cell_occupied(cell_t cell, const OccupancyGrid& map) {
    return map.logOdds(cell.x, cell.y) > 0;
}

void ObstacleDistanceGrid::setDistances(const OccupancyGrid& map)
{
    resetGrid(map);
    
    ///////////// TODO: Implement an algorithm to mark the distance to the nearest obstacle for every cell in the map.

    initializeDistances(map);
    std::priority_queue<DistanceNode> searchQueue;
    enqueue_obstacle_cells(map, *this, searchQueue);
    if (searchQueue.empty())
    {
        int width = map.widthInCells();
        int height = map.heightInCells(); // row
        bool is_EmptyMap = false;

        for (int y = 0; y < height; ++y)
        {
            for (int x = 0; x < width; ++x)
            {
                // the cell is free
                if (distance(x, y) == -1)
                {
                    is_EmptyMap = true;
                }
                // the cell is occupied
                else
                {
                    is_EmptyMap = false;
                    break;
                }
            }
        }

        if (is_EmptyMap)
        {
            for (int y = 0; y < height; ++y)
            {
                for (int x = 0; x < width; ++x)
                {
                    distance(x, y) = 100;
                }
            }
        }
    }
    while(!(searchQueue.empty())) {
        auto nextNode = searchQueue.top();
        searchQueue.pop();
        expand_node(nextNode, *this, searchQueue);
    }
}

void enqueue_obstacle_cells(const OccupancyGrid& map, ObstacleDistanceGrid& grid, std::priority_queue<DistanceNode>& search_queue)
{
    int width = map.widthInCells();
    int height = map.heightInCells();
    cell_t cell;

    for (cell.y = 0; cell.y < height; ++cell.y) {
        for (cell.x = 0; cell.x < width; ++cell.x) {
            if (is_cell_occupied(cell, map)) {
                expand_node(DistanceNode(cell, 0), grid, search_queue);
            }
        }
    }
}

// 8-ways
void expand_node(const DistanceNode& node, ObstacleDistanceGrid& grid, std::priority_queue<DistanceNode>& search_queue)
{
    const int xDeltas[8] = {1, -1, 0, 0, 1, -1, 1, -1};
    const int yDeltas[8] = {0, 0, 1, -1, 1, -1, -1, 1};

    for (int n = 0; n < 4; ++n) {
        cell_t adjacentCell(node.cell.x + xDeltas[n], node.cell.y + yDeltas[n]);
        if (grid.isCellInGrid(adjacentCell.x, adjacentCell.y)) {
            if (grid(adjacentCell.x, adjacentCell.y) == -1) {
                DistanceNode adjacentNode(adjacentCell, node.distance + 1);
                grid(adjacentCell.x, adjacentCell.y) = adjacentNode.distance * grid.metersPerCell();
                search_queue.push(adjacentNode);
            }
        }
    }
    for (int n = 4; n < 8; ++n) {
        cell_t adjacentCell(node.cell.x + xDeltas[n], node.cell.y + yDeltas[n]);
        if (grid.isCellInGrid(adjacentCell.x, adjacentCell.y)) {
            if (grid(adjacentCell.x, adjacentCell.y) == -1) {
                DistanceNode adjacentNode(adjacentCell, node.distance + 1.414);
                grid(adjacentCell.x, adjacentCell.y) = adjacentNode.distance * grid.metersPerCell();
                search_queue.push(adjacentNode);
            }
        }
    }
}

bool ObstacleDistanceGrid::isCellInGrid(int x, int y) const
{
    return (x >= 0) && (x < width_) && (y >= 0) && (y < height_);
}


void ObstacleDistanceGrid::resetGrid(const OccupancyGrid& map)
{
    // Ensure the same cell sizes for both grid
    metersPerCell_ = map.metersPerCell();
    cellsPerMeter_ = map.cellsPerMeter();
    globalOrigin_ = map.originInGlobalFrame();
    
    // If the grid is already the correct size, nothing needs to be done
    if((width_ == map.widthInCells()) && (height_ == map.heightInCells()))
    {
        return;
    }
    
    // Otherwise, resize the vector that is storing the data
    width_ = map.widthInCells();
    height_ = map.heightInCells();
    
    cells_.resize(width_ * height_);
}

// #include <planning/obstacle_distance_grid.hpp>
// #include <slam/occupancy_grid.hpp>

// ObstacleDistanceGrid::ObstacleDistanceGrid(void)
//     : width_(0), height_(0), metersPerCell_(0.05f), cellsPerMeter_(20.0f)
// {
// }

// void ObstacleDistanceGrid::initializeDistances(const OccupancyGrid &map)
// {
 
//     int width = map.widthInCells();
//     int height = map.heightInCells();

//     for (int y = 0; y < height; ++y) {
//         for (int x = 0; x < width; ++x) {
//             if (map.logOdds(x,y) < 0) {
//                 distance(x,y) = -1.0;
//             }
//             else {
//                 distance(x,y) = 0.0;
//             }
//         }
//     }
// }

// void ObstacleDistanceGrid::setDistances(const OccupancyGrid &map)
// {
//     resetGrid(map);
//     initializeDistances(map);

//     // Implement with a priority queue
//     std::priority_queue<DistanceNode> searchQueue;
//     enqueue_obstacle_cells(*this, searchQueue);

//     if (searchQueue.empty())
//     {
//         int width = map.widthInCells();
//         int height = map.heightInCells(); // row
//         bool is_EmptyMap = false;

//         for (int y = 0; y < height; ++y)
//         {
//             for (int x = 0; x < width; ++x)
//             {
//                 // the cell is free
//                 if (distance(x, y) == -1)
//                 {
//                     is_EmptyMap = true;
//                 }
//                 // the cell is occupied
//                 else
//                 {
//                     is_EmptyMap = false;
//                     break;
//                 }
//             }
//         }

//         // For the empty grid a-star test. Will fail if we don't assign a non-negative distance to the cells
//         if (is_EmptyMap)
//         {
//             for (int y = 0; y < height; ++y)
//             {
//                 for (int x = 0; x < width; ++x)
//                 {
//                     distance(x, y) = 100;
//                 }
//             }
//         }
//     }

//     while (!searchQueue.empty())
//     {
//         DistanceNode nextNode = searchQueue.top();
//         searchQueue.pop();
//         expand_node(nextNode, *this, searchQueue);
//     }
// }

// void ObstacleDistanceGrid::resetGrid(const OccupancyGrid &map)
// {
//     // Ensure the same cell sizes for both grid
//     metersPerCell_ = map.metersPerCell();
//     cellsPerMeter_ = map.cellsPerMeter();
//     globalOrigin_ = map.originInGlobalFrame();

//     // If the grid is already the correct size, nothing needs to be done
//     if ((width_ == map.widthInCells()) && (height_ == map.heightInCells()))
//     {
//         return;
//     }

//     // Otherwise, resize the vector that is storing the data
//     width_ = map.widthInCells();
//     height_ = map.heightInCells();

//     cells_.resize(width_ * height_);
// }

// void ObstacleDistanceGrid::enqueue_obstacle_cells(ObstacleDistanceGrid &grid, std::priority_queue<DistanceNode> &searchQueue)
// {
//     int width = grid.widthInCells();
//     int height = grid.heightInCells();
//     cell_t cell;

//     for (cell.y = 0; cell.y < height; cell.y++)
//     {
//         for (cell.x = 0; cell.x < width; cell.x++)
//         {
//             if (distance(cell.x, cell.y) == 0)
//             {
//                 expand_node(DistanceNode(cell, 0.0), grid, searchQueue);
//             }
//         }
//     }
// }

// void ObstacleDistanceGrid::expand_node(const DistanceNode node, ObstacleDistanceGrid &grid, std::priority_queue<DistanceNode> &searchQueue)
// {
    
//     const int xDeltas[8] = {1, -1, 0, 0, 1, -1, 1, -1};
//     const int yDeltas[8] = {0, 0, 1, -1, 1, -1, -1, 1};
//     float adjacent_distance = 0;
//     for (int i = 0; i < 4; i++)
//     {
//         cell_t adjacentCell(node.cell.x + xDeltas[i], node.cell.y + yDeltas[i]);
//         if (grid.isCellInGrid(adjacentCell.x, adjacentCell.y))
//         {
//             adjacent_distance = node.distance + 1.0;

//             float dist = grid(adjacentCell.x, adjacentCell.y);
//             if (dist == -1 || dist > adjacent_distance * grid.metersPerCell())
//             {
//                 DistanceNode adjacentNode(adjacentCell, adjacent_distance);
//                 grid(adjacentCell.x, adjacentCell.y) = adjacentNode.distance * grid.metersPerCell();
//                 searchQueue.push(adjacentNode);
//             }
//         }
//     }
//     for (int i = 4; i < 8; i++)
//     {
//         cell_t adjacentCell(node.cell.x + xDeltas[i], node.cell.y + yDeltas[i]);
//         if (grid.isCellInGrid(adjacentCell.x, adjacentCell.y))
//         {
            
//             adjacent_distance = node.distance + 1.414;

//             float dist = grid(adjacentCell.x, adjacentCell.y);
//             if (dist == -1 || dist > adjacent_distance * grid.metersPerCell())
//             {
//                 DistanceNode adjacentNode(adjacentCell, adjacent_distance);
//                 grid(adjacentCell.x, adjacentCell.y) = adjacentNode.distance * grid.metersPerCell();
//                 searchQueue.push(adjacentNode);
//             }
//         }
//     }
// }

// bool isCellFree(cell_t cell, const OccupancyGrid &map)
// {
//     return map.logOdds(cell.x, cell.y) <= 0;
// }

// bool isCellOccupied(cell_t cell, const OccupancyGrid &map)
// {
//     return map.logOdds(cell.x, cell.y) >= 0;
// }

// bool ObstacleDistanceGrid::isCellInGrid(int x, int y) const
// {
//     return (x >= 0) && (x < width_) && (y >= 0) && (y < height_);
// }