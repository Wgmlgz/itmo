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
  { cout.flush() }
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

void dfs(int v, vec<pair<vi, int>>& graph, int& count) {
  graph[v].second = 1;
  fl(next, graph[v].first) {
    if (graph[next].second == 0)
      dfs(next, graph, count);
    else if (graph[next].second == 1)
      count++;
  }
  graph[v].second = 2;
}

code {
  ri(n);
  vec<pair<vi, int>> graph(n);
  fo(i, n) {
    ri(t);
    graph[t - 1].first.push_back(i);
  }

  int res = 0;
  fo(i, n) if (graph[i].second == 0) dfs(i, graph, res);
  on(res);
}