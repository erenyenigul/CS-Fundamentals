#include <stdio.h>
#include <string.h>

void diamond(char* str){
    int len = strlen(str);
    
    for(int i=0; i<2*len; i++){
        if(i<len){
            for(int j=0;j<=i;j++) printf("%c", str[j]);
        }else{
            char space[i-len+2];
            for(int k = 0; k<i-len+1; k++) space[k] = ' ';
            space[i-len+1]='\0';
            printf("%s", space);
            
            for(int j=i-len+1;j<len;j++) printf("%c", str[j]);
        }
        printf("\n");
    }
    
}

int main()
{
    diamond("SAMPLE TEXT");
    return 0;
}
