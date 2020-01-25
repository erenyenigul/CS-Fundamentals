def binary_search(list, integer):
    i=0
    j=len(list)-1
    while list[i] != integer :
        k = int((i+j)/2)
        if  list[k] < integer :
            i=k+1
        else :
            j=k
    return i
