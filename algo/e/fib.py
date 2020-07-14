def fibBad(n):
    if(n == 2): return 1
    if(n == 1): return 0
    return  fibBad(n-1) + fibBad(n-2)



#key value, key so that n-2 is 0, and n-1 is 1
def fibrecmemo(n, memo = {1 :0, 2: 1}):
    if n in memo:
        return memo[n]
    else:
        memo[n] = fibrecmemo(n-1, memo) + fibrecmemo(n-2, memo);
        return memo[n]




print(fibBad(7))
print(fibrecmemo(7, memo))