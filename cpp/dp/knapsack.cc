# Taken from https://github.com/CianLR/judge-solutions/blob/d273867c04813a161ec888aecf47e5d6c2dc916a/kattis/knapsack.cc

#include <vector>

using namespace std;

struct Object {
  Object(int i_, int v, int w) : i(i_), value(v), weight(w) {}
  int i, value, weight;
};

vector<int> Knapsack(int cap, const vector<Object> &objs) {
  vector<vector<int>> values(objs.size() + 1, vector<int>(cap + 1, 0));
  vector<vector<bool>> taken(objs.size(), vector<bool>(cap + 1, false));
  for (auto &item : objs) {
    for (int c = 0; c <= cap; ++c) {
      if (c < item.weight ||
          values[item.i][c - item.weight] + item.value < values[item.i][c]) {
        // Don't take if can't hold or would reduce value.
        values[item.i + 1][c] = values[item.i][c];
      } else {
        values[item.i + 1][c] = values[item.i][c - item.weight] + item.value;
        taken[item.i][c] = true;
      }
    }
  }
  vector<int> taken_items;
  int c = cap;
  for (int i = objs.size() - 1; i >= 0; --i) {
    if (taken[i][c]) {
      taken_items.push_back(i);
      c -= objs[i].weight;
    }
  }
  return taken_items
}

