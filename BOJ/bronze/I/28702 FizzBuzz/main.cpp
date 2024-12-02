#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
int main()
{
    vector<string> inputs;
    vector<string> fizz_buzz = {"Fizz", "Buzz", "FizzBuzz"};
    for (int i = 0; i<3; i++){
        string temp;
        cin >> temp;
        inputs.push_back(temp);
    }
    int next_number;
    int tmp = 0;
    for (string number : inputs){
        tmp++;
        if (find(fizz_buzz.begin(), fizz_buzz.end(), number) != fizz_buzz.end()){
            continue;
        }
        next_number = stoi(number) + 4 - tmp;
    }

    string result = "";
    if (next_number % 3 == 0){
        result += "Fizz";
    }
    if (next_number % 5 == 0){
        result += "Buzz";
    }
    if (result.empty()){
        cout << next_number << endl;
    }
    else{
        cout << result << endl;
    }
    return 0;
}
