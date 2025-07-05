#include <iostream>
using namespace std;

int main() {
    int matriz[2][2];

    matriz[0][0] = 1;
    matriz[0][1] = 2;
    matriz[1][0] = 3;
    matriz[1][1] = 4;

    cout << "Matriz 2x2:" << endl;
    for (int i = 0; i < 2; ++i) {
        for (int j = 0; j < 2; ++j) {
            cout << matriz[i][j] << "\t";
        }
        cout << endl;
    }

    return 0;
}
