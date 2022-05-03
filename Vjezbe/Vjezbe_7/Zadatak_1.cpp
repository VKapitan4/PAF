#include <iostream>
#include <Particle.h>

int main(){
    std::cout <<"particle 1:"<< std::endl;
    Particle p1(0,0,10,60);
    p1.range();
    p1.time();
    std::cout <<"particle 2:"<< std::endl;
    Particle p2(3,4,15,45);
    p2.range();
    p2.time();
    std::cout <<"particle 3:"<< std::endl;
    Particle p3(0,0,5,10);
    p3.range();
    p3.time();
    return 0;
}
