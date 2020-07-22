def validatesubsequence(array, subarray):
    i = 0
    j = 0
    while(i < len(array)):
        if(j == len(subarray)):
            break
        if(subarray[j] == array[i]):
            j = j + 1
            i = i + 1
        else:
            i = i + 1
        print(i)
        print(j)
    return j == len(subarray)

print(validatesubsequence([1,3,4,5,15, 19], [1,3, 15]))