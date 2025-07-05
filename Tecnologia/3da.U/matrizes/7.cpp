#include <iostream>
using namespace std;

int main() {
    int matriz[3][3];

    cout << "Ingresa los elementos de una matriz 3x3:\n";
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            cout << "Elemento [" << i << "][" << j << "]: ";
            cin >> matriz[i][j];
        }
    }

    int columna;
    cout << "Ingresa el número de columna que deseas mostrar (0, 1 o 2): ";
    cin >> columna;

    if (columna < 0 || columna > 2) {
        cout << "Columna inválida. Debe ser 0, 1 o 2.\n";
    } else {
        cout << "Elementos de la columna " << columna << ":\n";
        for (int i = 0; i < 3; i++) {
            cout << matriz[i][columna] << endl;
        }
    }

    return 0;
}
