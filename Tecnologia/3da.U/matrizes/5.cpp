#include <iostream>
using namespace std;

int main() {
    int matriz[3][3];
    int suma = 0;
    float promedio;

    cout << "Ingresa los valores para una matriz 3x3:\n";
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            cout << "Elemento [" << i << "][" << j << "]: ";
            cin >> matriz[i][j];
            suma += matriz[i][j]; 
        }
    }

    promedio = suma / 9.0;

    cout << "El promedio de todos los elementos es: " << promedio << endl;

    return 0;
}
