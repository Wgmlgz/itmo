// #define ONLINE_JUDGE
// #define IDS
#ifndef NO_ONLINE_JUDGE
#define ONLINE_JUDGE
#endif

#pragma region
// #pragma GCC optimize("Ofast")
// #pragma GCC target("avx,avx2,fma")
// #pragma GCC optimize ("unroll-loops")
#include <algorithm>
#include <bitset>
#include <functional>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <random>
#include <regex>
#include <set>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
// #include <multiset>
// #include <multimap>
// #include <unordered_multiset>
// #include <unordered_multiset>
// #include <ext/pb_ds/assoc_container.hpp>
// #include <ext/pb_ds/tree_policy.hpp>
// using namespace __gnu_pbds;
using namespace std;
#define int int64_t
int MOD = 998244353ll;
int INF = 1e9;
int64_t inf = 1e18;
typedef string str;
typedef int64_t ll;
template <typename T>
using vec = vector<T>;
typedef pair<int, int> ii;
typedef vec<int> vi;
typedef vec<ii> vii;
typedef vec<vi> vvi;
// template<typename T,typename CMP=less<T>> using
// oset=tree<T,null_type,CMP,rb_tree_tag,tree_order_statistics_node_update>;
// template <typename T> using minpq = priority_queue<T, vector<T>, greater<T>>;
// template<typename KEY,typename VAL,typename CMP=less<KEY>> using omap =
// tree<KEY, VAL, CMP, rb_tree_tag, tree_order_statistics_node_update>;
template <typename T = int>
auto arr2(int x, int y, const T& val = 0) {
  return vec<vec<T>>(x, vec<T>(y, val));
}
template <typename T = int>
auto arr3(int x, int y, int z, const T& val = 0) {
  return vec<vec<vec<T>>>(x, vec<vec<T>>(y, vec<T>(z, val)));
}
auto& out = cout;
#define hmap unordered_map
#define hset unordered_set
#define GET_MACRO2(_1, _2, NAME, ...) NAME
#define GET_MACRO3(_1, _2, _3, NAME, ...) NAME
#define GET_MACRO4(_1, _2, _3, _4, NAME, ...) NAME
#define sz size()
#define bg begin()
#define ed end()
#define bk back()
#define fr front()
#define lb lower_bound
#define ub upper_bound
#define pb push_back
#define em emplace
#define eb emplace_back
#define F first
#define S second
#define ret return
#define fl(i, x) for (auto& i : x)
#define flc(i, x) for (auto i : x)
#define flp(a, b, x) for (auto& [a, b] : x)
#define flpc(a, b, x) for (auto [a, b] : x)
#define fo_2(i, n) for (int i = 0; i < n; i++)
#define fo_3(i, k, n) for (int i = k; i < n; ++i)
#define fo_4(i, a, b, c) for (int i = a; i < b; i += c)
#define fou(i, k, n) for (int i = k; i < n; ++i)
#define fod(i, k, n) for (int i = k; i > n; --i)
#define fo(...) GET_MACRO4(__VA_ARGS__, fo_4, fo_3, fo_2, fo_1)(__VA_ARGS__)
#define db dd <<
#define o outs <<
#define O out <<
#define I in >>
#define flsh \
  { cout.flush(); }
// #define endl "\n"
#define yes \
  { o "YES"; }
#define no \
  { o "NO"; }
#define yesr \
  {          \
    yes;     \
    return;  \
  }
#define nor \
  {         \
    no;     \
    return; \
  }
#define all(x) (x).bg, (x).ed
template <typename T>
inline bool emax(T& a, T b) {
  if (a < b) {
    a = b;
    return true;
  }
  return false;
}
template <typename T>
inline bool emin(T& a, T b) {
  if (a > b) {
    a = b;
    return true;
  }
  return false;
}
template <typename TC, typename T>
auto FIND(const TC& cont, const T& x) {
  return find(all(cont), x);
}
template <typename TC, typename T>
bool IN(const TC& cont, const T& x) {
  return FIND(cont, x) != cont.ed;
}
#define rv(v, n) \
  vec<ll> v(n);  \
  fl(i, v) { I i; }
#define rs(s) \
  str s;      \
  I s;
#define rm(v, n, m)                \
  vec<vec<int>> v(n, vec<int>(m)); \
  fl(i, v) { fl(j, i) I j; }
#define rc(v) \
  fl(i, v) { I i; }
#define ri_1(a) \
  ll a;         \
  I a;
#define ri_2(a, b) \
  ll a, b;         \
  I a >> b;
#define ri_3(a, b, c) \
  ll a, b, c;         \
  I a >> b >> c;
#define ri_4(a, b, c, d) \
  ll a, b, c, d;         \
  I a >> b >> c >> d;
#define ri(...) GET_MACRO4(__VA_ARGS__, ri_4, ri_3, ri_2, ri_1)(__VA_ARGS__)
#define ct \
  { continue; }
#define br \
  { break; }
#define dig -'0'
#define let -'a'
#define LET -'A'
#define in cin
vector<int> dx{1, 0, -1, 0};
vector<int> dy{0, 1, 0, -1};
template <typename T>
void on(T t) {
  O t << "\n";
}
template <typename T, typename... Args>
void on(T t, Args... args) {
  O t << " ";
  on(args...);
}
template <typename T>
int sgn(T val) {
  return (T(0) < val) - (val < T(0));
}
string getInput();
bool getTests();
void solve(int);
void preSolve();
void solve(int);
void presolve();
string bits(int c, const size_t s = 10) {
  return bitset<64>(c).to_string().substr(64 - s, s);
}
void yn(bool x) { on(x ? "YES" : "NO"); }
template <typename T>
void sort(T& c) {
  sort(c.begin(), c.end());
}
template <typename T>
void rev(T& c) {
  reverse(c.begin(), c.end());
}
template <typename T>
void unq(T& c) {
  c.erase(unique(c.begin(), c.end()), c.end());
}
template <class T>
auto sum(T& c) {
  return accumulate(c.begin(), c.end(), 0LL);
}
template <typename T1, typename T2>
istream& operator>>(istream& is, pair<T1, T2>& p) {
  is >> p.first;
  is >> p.second;
  return is;
}
template <typename T1, typename T2>
ostream& operator<<(ostream& os, const pair<T1, T2>& p) {
  os << p.first << " " << p.second;
  return os;
}
template <typename T>
ostream& OTC(ostream& ot, const T& v, bool isf) {
  for (auto& i : v) ot << i << (isf ? " " : "\n");
  return ot;
}
#define OT(nm)                                            \
  template <typename T>                                   \
  ostream& operator<<(ostream& ot, const nm<T>& v) {      \
    return OTC<nm<T>>(ot, v, (is_fundamental<T>::value)); \
  }
#define OTP(nm)                                           \
  template <typename T1, typename T2>                     \
  ostream& operator<<(ostream& ot, const nm<T1, T2>& v) { \
    return OTC<nm<T1, T2>>(ot, v, 0);                     \
  }
OTP(map)
OTP(multimap)
OTP(unordered_map)
OTP(unordered_multimap)
OT(list)
OT(set)
OT(deque)
OT(multiset) OT(unordered_set) OT(unordered_multiset) OT(vector) struct OUTS {};
OUTS outs;
template <typename T>
OUTS& operator<<(OUTS& tt, const T& t) {
  cout << t << '\n';
  return tt;
}
#define gg(...) 666
#ifdef ONLINE_JUDGE
struct dbstream {
  dbstream(std::ostream&) {}
};
template <typename T>
dbstream& operator<<(dbstream& dbs, const T& t) {
  return dbs;
}
signed main() {
  // ios_base::sync_with_stdio(0), in.tie(0), out.tie(0);
  presolve();
  if (getTests()) {
    int n;
    I n;
    for (int i = 1; i <= n; ++i) solve(i);
  } else
    solve(0);
}
#else
#include "./CP-Lib/Code/debug.hpp"
#include "./CP-Lib/Code/main.hpp"
#endif
dbstream dd(out);
struct INPUT {
  template <typename T>
  operator T() {
    T t;
    I t;
    return t;
  }
};
INPUT rd;
mt19937 rng;
#define tests        \
  bool getTests() <% \
    return
#define hf \
  ;        \
  %>       \
  void presolve()
#define code void solve(int TT)
#pragma endregion

tests 0 hf {}

// #pragma once
// const int INF = 1000 * 1000 * 1000;

#pragma region
template <typename T>
class SegTree {
  /* by Wgmlgz */
  std::function<T(const T&, const T&)> seg_merge;

  std::vector<T> base;
  std::vector<T> tree;

  void build(int pos, int l, int r) {
    if (r - l == 1) {
      tree[pos] = base[l];
      return;
    }
    int m = l + (r - l) / 2;
    build(pos * 2, l, m);
    build(pos * 2 + 1, m, r);
    tree[pos] = seg_merge(tree[pos * 2], tree[pos * 2 + 1]);
  }

  std::pair<bool, T> getRange(int pos, int ql, int qr, int l, int r) {
    if (ql <= l and qr >= r) return {true, tree[pos]};
    if (qr <= l or ql >= r) return {false, T()};

    int m = l + (r - l) / 2;
    auto r1 = getRange(pos * 2, ql, qr, l, m);
    auto r2 = getRange(pos * 2 + 1, ql, qr, m, r);

    if (r1.first and r2.first)
      return {true, seg_merge(r1.second, r2.second)};
    else if (r1.first)
      return {true, r1.second};
    else
      return {true, r2.second};
  }
  void update(int pos, int q, int l, int r, const T& val) {
    if (r - l == 1) {
      tree[pos] = val;
      return;
    }
    int m = l + (r - l) / 2;
    if (m > q)
      update(pos * 2, q, l, m, val);
    else
      update(pos * 2 + 1, q, m, r, val);
    tree[pos] = seg_merge(tree[pos * 2], tree[pos * 2 + 1]);
  }

 public:
  SegTree(const std::vector<T>& v,
          std::function<T(const T&, const T&)> seg_merge) {
    this->seg_merge = seg_merge;
    base = v;
    tree.resize(4 * base.size());
    build(1, 0, base.size());
  }
  T getRange(int l, int r) { return getRange(1, l, r, 0, base.size()).second; }
  void update(int pos, const T& val) { update(1, pos, 0, base.size(), val); }
};

template <typename T>
struct SegSumT : public SegTree<T> {
  SegSumT(const std::vector<T>& v)
      : SegTree<T>::SegTree(v, [](auto a, auto b) { return a + b; }) {}
};

template <typename T>
struct SegMinT : public SegTree<T> {
  SegMinT(const std::vector<T>& v)
      : SegTree<T>::SegTree(v, [](auto a, auto b) { return std::min(a, b); }) {}
};

template <typename T>
struct SegMaxT : public SegTree<T> {
  SegMaxT(const std::vector<T>& v)
      : SegTree<T>::SegTree(v, [](auto a, auto b) { return std::max(a, b); }) {}
};

typedef SegSumT<int64_t> SegSum;
typedef SegSumT<long double> SegSumLD;
typedef SegSumT<double> SegSumD;
typedef SegSumT<int> SegSumI;

typedef SegMinT<int64_t> SegMin;
typedef SegMinT<long double> SegMinLD;
typedef SegMinT<double> SegMinD;
typedef SegMinT<int> SegMinI;

typedef SegMaxT<int64_t> SegMax;
typedef SegMaxT<long double> SegMaxLD;
typedef SegMaxT<double> SegMaxD;
typedef SegMaxT<int> SegMaxI;
#pragma endregion

code {
  ri(n, m);
  ri(x, y);
  ri(x1, y1);

  --x, --y;
  --x1, --y1;
  vec<str> grid(n);
  fo(i, n) I grid[i];

  vvi c(n, vi(m, INF));
  vec<vec<ii>> old(n, vii(m, {x, y}));

  minpq<pair<int, pair<ii, ii>>> q;
  q.push({0, {{x, y}, {x, y}}});

  auto check = [&](int x, int y, int cost, ii cur) {
    if (x >= 0 && x < n && y >= 0 && y < m && grid[x][y] != '#') {
      int r = cost;
      if (grid[x][y] == 'W') r += 2;
      if (grid[x][y] == '.') r += 1;
      if (c[x][y] > r) {
        q.push({r, {{x, y}, cur}});
      }
    }
  };

  // db grid;
  while (!q.empty()) {
    // db c;
    auto [cost, positions] = q.top();
    auto [pos, pr] = positions;
    auto [x, y] = pos;
    q.pop();

    if (c[x][y] <= cost) continue;
    c[x][y] = cost;
    old[x][y] = pr;

    if (x == x1 && y == y1) break;

    check(x - 1, y, cost, pos);
    check(x + 1, y, cost, pos);
    check(x, y - 1, cost, pos);
    check(x, y + 1, cost, pos);
  }

  if (c[x1][y1] == INF) {
    on(-1);
  } else {
    auto res = c[x1][y1];
    on(res);

    str s;
    ii cur = {x1, y1};
    db c;
    db old;
    while (true) {
      db cur;
      auto [x, y] = cur;
      if (x == -1) break;
      auto [nx, ny] = old[x][y];
      int dx = x - nx;
      int dy = y - ny;
      if (dx == -1) s += "N";
      if (dx == 1) s += "S";
      if (dy == -1) s += "W";
      if (dy == 1) s += "E";

      // on(s);

      if (dx == 0 && dy == 0) break;
      cur = {nx, ny};
    }
    // on(s);

    reverse(all(s));
    // on(s);

    // s = s.reserve();
    on(s);
  }
}