#include <slam/mapping.hpp>
#include <slam/moving_laser_scan.hpp>
#include <slam/occupancy_grid.hpp>
#include <common/grid_utils.hpp>
#include <numeric>

using namespace std;

Mapping::Mapping(float maxLaserDistance, int8_t hitOdds, int8_t missOdds)
: kMaxLaserDistance_(maxLaserDistance)
, kHitOdds_(hitOdds)
, kMissOdds_(missOdds)
, initialized(false)
{
}

// Look through Videos (for step-by-step coding) & Lecture 07
void Mapping::updateMap(const lidar_t& scan, const pose_xyt_t& pose, OccupancyGrid& map)
{
    //////////////// TODO: Implement your occupancy grid algorithm here ///////////////////////
    /*
    for each cell in map
        if m is within the z_max or perceptual field of zt
            lt,i = lt-1 + inverse_sensor_model(m, xt,zt) - inital (0)
        else
            lt,i = lt-1,i

    return 0;
    */

   MovingLaserScan movingScan(scan, previousPose_, pose);

    // going through all the rays in the scan, scoring each ray
   for(auto& ray : movingScan) {
       scoreEndpoint(ray, map);
   }

    for(auto& ray : movingScan) {
        scoreRay(ray, map);
    }

    previousPose_ = pose;
}

void Mapping::scoreEndpoint(const adjusted_ray_t& ray, OccupancyGrid& map) {
    if(ray.range < kMaxLaserDistance_) {
        /*
        * global_position_to_grid_position converts a point in the global coordinate system to a point in the grid coordinate system. The
        * point can be fractions of a grid cell so no information (modulo floating-point error) is lost converting back and forth
        * between global and grid points.
        */
        Point<double> StartPoint = global_position_to_grid_position(ray.origin, map);

        Point<double> EndCell;

        // we use sohcahtoa to calculate the x and y value of the EndCell
        EndCell.x = static_cast<int>(StartPoint.x + ray.range * cos(ray.theta) * map.cellsPerMeter());
        EndCell.y = static_cast<int>(StartPoint.y + ray.range * sin(ray.theta) * map.cellsPerMeter());

        // clamping map value to between range
        if(map.isCellInGrid(EndCell.x, EndCell.y)) {
            if(map(EndCell.x, EndCell.y) + kHitOdds_ >= 127) {
                map(EndCell.x, EndCell.y) = 127;
            } else {
                map(EndCell.x, EndCell.y) += kHitOdds_;
            }
        }
    }
}

void Mapping::scoreRay(const adjusted_ray_t& ray, OccupancyGrid& map) {
    // create a vector of points within the ray using Bresenham's algorithm
    vector<Point<int>> cells_touched = Mapping::bresenham(ray, map);
    // iterate through those points checking if they are within the grid
    for(auto const& pt : cells_touched) {
        if(map.isCellInGrid(pt.x, pt.y)) {
            // if so decrease their log odds because we know they are empty
            // clamping map value to between range
            if(map(pt.x, pt.y) - kMissOdds_ > -127) {
                map(pt.x, pt.y) -= kMissOdds_;
            } else {
                map(pt.x, pt.y) = -127;
            }
        }
    }
}

vector<Point<int>> Mapping::bresenham(const adjusted_ray_t& ray, OccupancyGrid& map) {

    vector<Point<int>> cells_touched;

    // Starting point
    Point<int> rayStart = global_position_to_grid_position(ray.origin, map);

    Point<int> EndCell;
    // we use sohcahtoa to calculate the x and y value of the EndCell
    EndCell.x = static_cast<int>(rayStart.x + ray.range * cos(ray.theta) * map.cellsPerMeter());
    EndCell.y = static_cast<int>(rayStart.y + ray.range * sin(ray.theta) * map.cellsPerMeter());

    // Calculate the absolute distance between the two points 
    int dx = abs(EndCell.x - rayStart.x);
    int dy = abs(EndCell.y - rayStart.y);

    // Figure out the sign of x and y using the signs of each coordinate
    int s_x = rayStart.x < EndCell.x ? 1 : -1;
    int s_y = rayStart.y < EndCell.y ? 1 : -1;

    // Error difference b/w x & y
    int err = dx - dy;

    // Begin Moving along ray
    int x = rayStart.x;
    int y = rayStart.y;

    while (x != EndCell.x || y != EndCell.y) {

        // Update Odds
        Point<int> current_pt;
        current_pt.x = x;
        current_pt.y = y;
        cells_touched.push_back(current_pt);

        // Error * 2
        int error_2 = err * 2;
        if (error_2 >= -dy) {
            err -= dy;
            x += s_x;
        }

        if (error_2 <= dx) {
            err += dx;
            y += s_y;
        }
    }

    return cells_touched;
}

void Mapping::increaseCellOdds(int x, int y, OccupancyGrid& map){
    if (std::numeric_limits<CellOdds>::max() - map(x,y) > kHitOdds_){
        map(x,y) += kHitOdds_;
    }
    else{
        map(x,y) = std::numeric_limits<CellOdds>::max();
    }
}

void Mapping::decreaseCellOdds(int x, int y, OccupancyGrid& map){
    if (map(x, y) - std::numeric_limits<CellOdds>::min() > kMissOdds_)
    {
        map(x, y) -= kMissOdds_;
    }
    else
    {
        map(x, y) = std::numeric_limits<CellOdds>::min();
    }
}
