#include <iostream>

void fun(float x, float y, float r, float x1, float y1){
    if ((x-x1)*(x-x1)+(y-y1)*(y-y1) < r*r){
        std::cout <<"Tocka je unutar kruznice."<< std::endl;
    }
    else if ((x-x1)*(x-x1)+(y-y1)*(y-y1) > r*r){
        std::cout <<"Tocka je izvan kruznice."<< std::endl;
    }
    else if ((x-x1)*(x-x1)+(y-y1)*(y-y1) == r*r){
        std::cout <<"Tocka je na kruznice."<< std::endl;
    }
}

int main(){
    
    fun(1,1,1,2,1);

    return 0;
}