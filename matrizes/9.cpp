#include <iostream>
using namespace std;

int main() {
    int matriz[3][3];
    int columna, suma = 0;
    
    cout << "Ingresa los elementos de una matriz 3x3:" << endl;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            cout << "Elemento [" << i << "][" << j << "]: ";
            cin >> matriz[i][j];
        }
    }

    cout << "Ingresa el número de columna (0, 1 o 2) para sumar: ";
    cin >> columna;

    if (columna < 0 || columna > 2) {
        cout << "Número de columna inválido." << endl;
        return 1;
    }

    for (int i = 0; i < 3; i++) {
        suma += matriz[i][columna];
    }

    cout << "La suma de la columna " << columna << " es: " << suma << endl;

    return 0;
}
