#include <HarmonicOscillator.h>
#include <iostream>
#include <string>
#include <fstream>

using namespace std;

HarmonicOscillator::HarmonicOscillator(float x0, float v0, float m, float k, float vrijeme){
    _dt = 0.1;
    _vrijeme = vrijeme;
    _m = m;
    _k = k;
    _t = 0;
    _x0 = x0;
    _v0 = v0;
    _x = x0;
    _v = v0;
    _a = -(_k/_m)*_x0;
}

HarmonicOscillator::~HarmonicOscillator(){

}

void HarmonicOscillator::move(){
    _t+=_dt;
    _a = -(_k/_m)*_x;
    _v = _v + _a*_dt;
    _x = _x + _v*_dt;
}

void HarmonicOscillator::export_data(){
    if (_t==0){
        ofstream fw1("/Users/test/Documents/Programi/PAF/Vjezbe/Domaci_rad_3/Oscillator_t.txt", ofstream::out);
        fw1 << _t << "\n";
        ofstream fw2("/Users/test/Documents/Programi/PAF/Vjezbe/Domaci_rad_3/Oscillator_x.txt", ofstream::out);
        fw2 << _x <<"\n";
        while(_t < _vrijeme){
            move();
            fw1 << _t << "\n";
            fw2 << _x << "\n";
        }
        fw1.close();
        fw2.close();
    }
    else{
        cout << "Pozovite funkciju restart." <<  endl;
    }
}