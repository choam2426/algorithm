#include <iostream>
using namespace std;
int main()
{
    int n, t, p;
    int result = 0;
    int size_cnt[6];
    cin >> n;
    for(int i = 0; i < 6; i++){
        cin >> size_cnt[i];
    }
    cin >> t >> p;
    for(int i : size_cnt){
        result += (i % t) ? (i / t + 1) : (i / t);
    }
    cout << result << endl;
    cout << n / p << " " << n % p << endl;

    return 0;
}
