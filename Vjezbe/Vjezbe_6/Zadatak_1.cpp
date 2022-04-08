#include <iostream>

void fun(float x1, float y1, float x2, float y2){
        if (x1!=x2){
            float k = (y2-y1)/(x2-x1);
            float l = y1 - k*x1;
            if (l<0){
                std::cout <<"Jednadzba pravca: y="<<k<<"x-"<<abs(l)<< std::endl;
            }
            else{
                std::cout <<"Jednadzba pravca: y="<<k<<"x+"<<l<< std::endl;
            }
        }
        else{
            std::cout <<"Jednadzba pravca: x="<<x1<< std::endl;
        }
    }

int main(){
    
    fun(1,1,2,2);

    return 0;
}