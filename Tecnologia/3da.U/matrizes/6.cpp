#include <iostream>
using namespace std;

int main() {
    int matriz[3][3];  

    cout << "Ingrese los elementos de una matriz 3x3:\n";
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            cout << "Elemento [" << i << "][" << j << "]: ";
            cin >> matriz[i][j];
        }
    }

    int fila;
    cout << "\nIngrese el número de fila que desea mostrar (0, 1 o 2): ";
    cin >> fila;

    if (fila >= 0 && fila < 3) {
        cout << "Elementos de la fila " << fila << ": ";
        for (int j = 0; j < 3; j++) {
            cout << matriz[fila][j] << " ";
        }
        cout << endl;
    } else {
        cout << "Número de fila inválido. Debe ser 0, 1 o 2.\n";
    }

    return 0;
}
