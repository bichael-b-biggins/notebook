# Taken from https://github.com/CianLR/judge-solutions/blob/d273867c04813a161ec888aecf47e5d6c2dc916a/kattis/freckles_prims.cc
# Tested against Kattis:freckles

#include <math.h>
#include <functional>
#include <queue>
#include <utility>
#include <vector>

using namespace std;

struct Point {
  Point(double x_, double y_) : x(x_), y(y_), in_tree(false) {}
  double x;
  double y;
  bool in_tree;
};

double Dist(const Point &a, const Point &b) {
  return sqrt(pow(a.x - b.x, 2) + pow(a.y - b.y, 2));
}

double PrimsMST(int N, const vector<Point> &pts) {
  typedef pair<double, Point *> CostPoint;
  priority_queue<CostPoint, vector<CostPoint>, greater<CostPoint>> pq;
  pq.emplace(0, &pts[0]);
  double cost = 0;
  int total_nodes = 0;
  while (total_nodes < N) {
    if (pq.top().second->in_tree) {
      pq.pop();
      continue;
    }
    cost += pq.top().first;
    ++total_nodes;
    Point *p = pq.top().second;
    pq.pop();
    p->in_tree = true;
    for (int i = 0; i < N; ++i) {
      if (!pts[i].in_tree)
        pq.emplace(Dist(*p, pts[i]), &pts[i]);
    }
  }
  return cost;
}

