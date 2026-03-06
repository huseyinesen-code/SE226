#include <iostream>
using namespace std;

int main()
{

    int n;


    while (true)
    {

        cout << "Enter int between 10 and 100: ";
        cin >> n;

        if (n >= 10 && n <= 100)
            break;

        cout << "Invalid" << endl;
    }

    int fizz = 0, buzz = 0, fizzbuzz = 0;

    for (int i = 1; i <= n; i++) {

        if (i % 7 == 0)
            continue;

        if (i % 3 == 0 && i % 5 == 0) {
            cout << "FizzBuzz" << endl;
            fizzbuzz++;
        }
        else if (i % 3 == 0) {
            cout << "Fizz" << endl;
            fizz++;
        }
        else if (i % 5 == 0) {
            cout << "Buzz" << endl;
            buzz++;
        }
        else {
            cout << i << endl;
        }
    }

    cout << "\nSummary:" << endl;
    cout << "Fizz: " << fizz << endl;
    cout << "Buzz: " << buzz << endl;
    cout << "FizzBuzz: " << fizzbuzz << endl;

    return 0;
}