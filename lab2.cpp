    #include <iostream>
using namespace std;

int main()
{
    int number;
    cout << "Enter + integer greater than 9: ";
    cin >> number;

    int stepCount = 0;

    cout << number;

    while (number >= 10)
    {
        int temp = number;
        int digitSum = 0;

        while (temp > 0)
        {
            digitSum += temp % 10;
            temp /= 10;
        }

        number = digitSum;
        stepCount++;

        cout << " -> " << number;
    }

    cout << endl;
    cout << "Final value: " << number << endl;
    cout << "Total steps: " << stepCount << endl;

    return 0;
}