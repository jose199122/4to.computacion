#include <iostream>
using namespace std;

char tablero[3][3] = {
    {'1', '2', '3'},
    {'4', '5', '6'},
    {'7', '8', '9'}
};

char turno = 'X';

void mostrarTablero() {
    cout << "\n";
    for (int i = 0; i < 3; i++) {
        cout << " ";
        for (int j = 0; j < 3; j++) {
            cout << tablero[i][j];
            if (j < 2) cout << " | ";
        }
        if (i < 2) cout << "\n-----------\n";
    }
    cout << "\n\n";
}

bool marcarCasilla(int opcion) {
    int fila = (opcion - 1) / 3;
    int columna = (opcion - 1) % 3;

    if (tablero[fila][columna] != 'X' && tablero[fila][columna] != 'O') {
        tablero[fila][columna] = turno;
        return true;
    } else {
        return false;
    }
}

