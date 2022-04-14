#include <iostream>

void rjesavanje_sustava(float a1, float b1, float c1, float a2, float b2, float c2){
    float x = c1 - c2*(b2/b1) + a2*(b2/b1);
    float y = (c1 - a1*x)/b1;
    std::cout <<"x="<<x<< std::endl;
    std::cout <<"y="<<y<< std::endl;
}

int main(){
    rjesavanje_sustava(1,5,2,3,6,5);
    return 0;
}