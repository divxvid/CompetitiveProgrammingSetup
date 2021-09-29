#include <bits/stdc++.h>
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define eb emplace_back
#define mp make_pair
#define sz(x) ((int)(x.size()))

using namespace std ;
/*
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
  

// For multiset just add a counter with it's value increasing with each insert.
// for finding fix the counter value to 0.
// For Ordered map just add data type in place of null_type
#define ordered_multiset tree<pair<int, int>, null_type, less<pair<int, int>>, rb_tree_tag,tree_order_statistics_node_update>
#define ordered_set tree<int, null_type, less<int>, rb_tree_tag,tree_order_statistics_node_update>

//useful functions : order_of_key(key), find_by_order(order)
*/

void __print(int x) {cerr << x;}
void __print(long x) {cerr << x;}
void __print(long long x) {cerr << x;}
void __print(unsigned x) {cerr << x;}
void __print(unsigned long x) {cerr << x;}
void __print(unsigned long long x) {cerr << x;}
void __print(float x) {cerr << x;}
void __print(double x) {cerr << x;}
void __print(long double x) {cerr << x;}
void __print(char x) {cerr << '\'' << x << '\'';}
void __print(const char *x) {cerr << '\"' << x << '\"';}
void __print(const string &x) {cerr << '\"' << x << '\"';}
void __print(bool x) {cerr << (x ? "true" : "false");}

template<typename T, typename V>
void __print(const pair<T, V> &x) {cerr << '{'; __print(x.first); cerr << ','; __print(x.second); cerr << '}';}
template<typename T>
void __print(const T &x) {int f = 0; cerr << '{'; for (auto &i: x) cerr << (f++ ? "," : ""), __print(i); cerr << "}";}
void _print() {cerr << "]\n";}
template <typename T, typename... V>
void _print(T t, V... v) {__print(t); if (sizeof...(v)) cerr << ", "; _print(v...);}
#ifndef ONLINE_JUDGE
#define debug(x...) cerr << "[" << #x << "] = ["; _print(x)
#else
#define debug(x...)
#endif

typedef long long ll ;
typedef vector<int> vi ;
typedef vector<pair<int, int>> vpii ;
typedef vector<vector<int>> vvi ;
typedef pair<int, int> pii ;
typedef vector<ll> vl ;
typedef vector<vector<ll>> vvl ;
typedef pair<ll, ll> pll ;

void solve() {
}

int main() {
    ios_base::sync_with_stdio(false) ;
    cin.tie(nullptr) ;

    int t ;
    cin >> t ;

    while (t--)
        solve() ;

    return 0 ;
}

