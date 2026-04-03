#include <iostream>
using namespace std;

double manuelPowah(double base, int exp) {
    double result = 1.0;
    for (int i = 0; i < exp; i++) {
        result *= base;
    }
    return result;
}

double calculateGn(int n, double r) {

    if (n == 0) {
        return 1.0;
    }

    else {
        return manuelPowah(r, n) + calculateGn(n - 1, r);
    }
}

int main() {
    int n;
    double r;

    cout << "Enter n: number of terms: ";
    cin >> n;
    cout << "Enter r: common ratio: ";
    cin >> r;

    double result = calculateGn(n, r);
    cout << "The sum of the geometric series is: " << result << endl;

    return 0;
}