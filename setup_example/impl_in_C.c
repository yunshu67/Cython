#include "impl_in_C.h"
//typedef uint32_t u32;

int fib(int n){
    if(n<2) return n;
    int a=0,b=1,tmp;
    for (int i = 0; i < n-1; ++i) {
        tmp=b;
        b=a+b;
        a=tmp;
    }
    return b;
}

