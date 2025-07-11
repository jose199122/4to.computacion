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

bool verificarGanador() {
    for (int i = 0; i < 3; i++) {
        if (tablero[i][0] == turno && tablero[i][1] == turno && tablero[i][2] == turno) return true;
        if (tablero[0][i] == turno && tablero[1][i] == turno && tablero[2][i] == turno) return true;
    }
    if (tablero[0][0] == turno && tablero[1][1] == turno && tablero[2][2] == turno) return true;
    if (tablero[0][2] == turno && tablero[1][1] == turno && tablero[2][0] == turno) return true;

    return false;
}

bool tableroLleno() {
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            if (tablero[i][j] != 'X' && tablero[i][j] != 'O')
                return false;
    return true;
}

void cambiarTurno() {
    turno = (turno == 'X') ? 'O' : 'X';
}

int main() {
    int opcion;
    bool juegoActivo = true;

    cout << "=== JUEGO TOTITO (Tic-Tac-Toe) ===\n";

    while (juegoActivo) {
        mostrarTablero();
        cout << "Turno de " << turno << ". Elige una casilla (1-9): ";
        cin >> opcion;

        if (opcion < 1 || opcion > 9) {
            cout << "Opción inválida. Intenta de nuevo.\n";
            continue;
        }

        if (!marcarCasilla(opcion)) {
            cout << "Casilla ocupada. Intenta de nuevo.\n";
            continue;
        }

        if (verificarGanador()) {
            mostrarTablero();
            cout << "¡El jugador " << turno << " ha ganado!\n";
            break;
        }

        if (tableroLleno()) {
            mostrarTablero();
            cout << "¡Empate! El tablero está lleno.\n";
            break;
        }

        cambiarTurno();
    }

    return 0;
}
