#include<bits/stdc++.h>
using namespace std;
int h[510][510];
int ans[510][510];
int book[510][510];
int n, m;
queue<pair<int,int> > v;
int mm(int i, int j){
    int mmin = 1000000000;
    if (h[i][j]>=h[i-1][j]) mmin = min(mmin, ans[i-1][j]);
    if (h[i][j]>=h[i+1][j]) mmin = min(mmin, ans[i+1][j]);
    if (h[i][j]>=h[i][j-1]) mmin = min(mmin, ans[i][j-1]);
    if (h[i][j]>=h[i][j+1]) mmin = min(mmin, ans[i][j+1]);
    return mmin;
}
void ss(int i, int j){
    ans [i][j] = mm(i, j) + 1;
}
void dd(int i, int j){
    if(i+1<=m && j<=n && book[i+1][j]==0 && h[i][j]>=h[i+1][j])
        v.push(make_pair(i+1, j));
    if(i-1>=1 && j<=n && book[i-1][j]==0 && h[i][j]>=h[i-1][j])
        v.push(make_pair(i-1, j));
    if(i<=m && j+1<=n && book[i][j+1]==0 && h[i][j]>=h[i][j+1])
        v.push(make_pair(i, j+1));
    if(i<=m && j-1>=1 && book[i][j-1]==0 && h[i][j]>=h[i][j-1])
        v.push(make_pair(i, j-1));
}
void add(int i, int j){
    book[i+1][j] = 1;
    book[i-1][j] = 1;
    book[i][j+1] = 1;
    book[i][j-1] = 1;
}
int main()
{

    cin>>m>>n;
    for (int i=1; i<=m; i++){
        for (int j=1; j<=n; j++){
            cin>>h[i][j];
        }
    }
    for (int i=1; i<=m; i++){
        for (int j=1; j<=n; j++){
            if (h[i][j] == 0){
                ans[i][j] = 0;
                add(i, j);
                v.push(make_pair(i+1, j));
                v.push(make_pair(i-1, j));
                v.push(make_pair(i, j+1));
                v.push(make_pair(i, j-1));
            }
        }
    }
    while(!v.empty()){
        ss(v.front().first, v.front().second);
        dd(v.front().first, v.front().second);
        add(v.front().first, v.front().second);
        v.pop();
    }
    for (int i=1; i<=m; i++){
        for (int j=1; j<=n; j++){
            cout<<ans[i][j]<<" ";
        }
        cout<<endl;
    }
    return 0;
}
