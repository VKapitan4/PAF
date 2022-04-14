#include <iostream>

void ispisivanje(int polje[], int size){
    std::cout <<"elementi polja:"<< std::endl;
    for (int i = 0; i < size; i++){
        std::cout <<polje[i]<< std::endl;
    }
}

void ispisivanje_u_rasponu(int polje[], int size, int a, int b){
    std::cout <<"elementi polja u odabranom rasponu:"<< std::endl;
    for (int i = 0; i < size; i++){
        if (polje[i]>=a && polje[i]<=b){
            std::cout <<polje[i]<< std::endl;
        }
    }
}

void zamjena(int polje[], int prvi, int drugi){
    int a = polje[prvi];
    polje[prvi] = polje[drugi];
    polje[drugi] = a;
}

void okretanje(int polje[], int size){
    for (int i = 0; i <= (size/2)-1; i++){
        zamjena(polje, i, size-(i+1));
    }
}

void sortiranje(int polje[], int size){
    for (int i = 0; i < size; i++){
        for (int j = i+1; j < size; j++){
            if (polje[j] < polje[i]){
                zamjena(polje, i, j);
            }
        }
    }
}

int main(){
    int polje[9] = {-4,2,-6,5,0,3,1,7,1};
    ispisivanje_u_rasponu(polje, 9, -7, 0);
    ispisivanje(polje, 9);
    okretanje(polje, 9);
    ispisivanje(polje, 9);
    sortiranje(polje, 8);
    return 0;
}