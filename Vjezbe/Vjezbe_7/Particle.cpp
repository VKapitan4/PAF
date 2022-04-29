#include <Particle.h>
#include <cmath>
#include <iostream>

Particle::Particle(float x0, float y0, float v0, float kut){
    _t=0;
    _dt=0.001;
    _ax=0;
    _ay=-9.81;
    _vx=v0*cos((kut/360)*2*3.1416);
    _vy=v0*sin((kut/360)*2*3.1416);
    _x=x0;
    _y=y0;
    _y0=y0;
}

Particle::~Particle(){
    
}

float Particle::range(){
    _y=_y0;
    while(_y >= _y0){
        move();
    }
    std::cout <<"domet: "<< _x <<  std::endl;
    return _x;
}

void Particle::move(){
    _t+=_dt;
    _vx = _vx + _ax*_dt;
    _vy = _vy + _ay*_dt;
    _x = _x + _vx*_dt;
    _y = _y + _vy*_dt;
}

float Particle::time(){
    _y=_y0;
    while(_y >= _y0){
        move();
    }
    std::cout <<"vrijeme: "<< _t <<  std::endl;
    return _t;
}