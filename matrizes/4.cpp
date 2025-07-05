#include <iostream>
using namespace std;
int matriz[3][3],i,j;
int numero;
int main(){
	cout <<"ingresa la matriz:" << endl;
	for(i=0; i<3; i++){
		for(j=0; j<3; j++){
			cout<<"usuario, ingresa la posicion["<<i <<"]["<<j << "]:";
			cin>> matriz[i][j];
			cout<<endl;
		}
	}
	cout << "mostrando matriz:"<<endl;
	for(i=0; i<3; i++){
		for(j=0; j<3; j++){
			cout<<"["<<matriz[i][j]<<"]";
		}
		cout<<endl;
	}
	cout << "usuario, ingresa un numero a buscar:";
	cin >> numero;
	for(i=0; i<3; i++){
		for(j=0; j<3; j++){
			if(numero==matriz[i][j]){
				cout<<"el numero"<<numero<<"esta en la posicion["<<i<<"]["<<j<<"]"<<endl;
				return 0;
			}
		}
	}
	cout <<"el numero"<< numero<< "no se encuentra en la matriz."<< endl;
}
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    