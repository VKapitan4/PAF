#include <iostream>

void rjesavanje_sustava(float a1, float b1, float c1, float a2, float b2, float c2){
    if (a1*b2-b1*a2!=0){
        if (b2!=0){
            float x = (c1-c2*(b1/b2))/(a1-a2*(b1/b2));
            float y = (c2 - a2*x)/b2;
            std::cout <<"x="<<x<< std::endl;
            std::cout <<"y="<<y<< std::endl;
        }
        else{
            float x = c2/a2;
            float y = (c1 - a1*x)/b1;
            std::cout <<"x="<<x<< std::endl;
            std::cout <<"y="<<y<< std::endl;
        }
    }
    else{
        std::cout <<"Rjesenje nije jedinstveno ili ne postoji."<< std::endl;
    }
}

int main(){
    rjesavanje_sustava(1,1,0,1,1,2);
    return 0;
}