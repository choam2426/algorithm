#include <iostream>
using namespace std;
int main()
{
    int h, m, s, cooking_time, total_second;
    cin >> h >> m >> s;
    cin >> cooking_time;
    total_second = h * 3600 + m * 60 + s + cooking_time;

    cout << total_second / 3600 % 24 << " " << total_second % 3600 / 60 << " " << total_second % 60 << endl;

    return 0;
}
