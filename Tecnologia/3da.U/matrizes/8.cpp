#include <iostream>
using namespace std;

int main() {
    int matriz[3][3];
    int fila, suma = 0;

    cout << "Ingresa los elementos de una matriz 3x3:" << endl;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            cout << "Elemento [" << i << "][" << j << "]: ";
            cin >> matriz[i][j];
        }
    }

    cout << "Ingresa el número de fila a sumar (0-2): ";
    cin >> fila;

    if (fila < 0 || fila > 2) {
        cout << "Número de fila inválido." << endl;
        return 1;
    }

    for (int j = 0; j < 3; j++) {
        suma += matriz[fila][j];
    }

    cout << "La suma de los elementos de la fila " << fila << " es: " << suma << endl;

    return 0;
}
