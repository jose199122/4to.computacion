#include <iostream>
using namespace std;

int main() {
    int matriz[2][2];
    int suma = 0;

    cout << "Ingrese los valores de una matriz 2x2:" << endl;

    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            cout << "Elemento [" << i << "][" << j << "]: ";
            cin >> matriz[i][j];
            suma += matriz[i][j];
        }
    }

    cout << "La suma de todos los elementos es: " << suma << endl;

    return 0;
}
