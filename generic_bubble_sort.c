#include <stdio.h>
#include <string.h>

int intcpm(int*i1, int*i2){
    return *i1-*i2;
}

void generic_swap(void* s1, void*s2,size_t nbytes){
    char temp[nbytes];
    memcpy(temp, s1,   nbytes);
    memcpy(s1,   s2,   nbytes);
    memcpy(s2,   temp, nbytes);
}

void bubble_sort(void*arr, size_t arrlength, size_t nbytes, int(*cmp)(void*,void*)){
    short isSorted=0;
    while(!isSorted){
        isSorted=1;
        for(int i=1;i<arrlength;i++){
            char*o2= ((char*)arr)+nbytes*i;
            char*o1= ((char*)arr)+nbytes*(i-1);
            if(cmp(o2,o1)<0){
                isSorted=0;
                generic_swap(o1,o2,nbytes);
            }
        }
    }
}



int main()
{
    int arr[5]={5,4,3,9,2};
    bubble_sort(arr, 5, 4, intcpm);
    for(int i=0; i<5;i++) printf("%d", arr[i]);

    return 0;
}
