#-----------------------
def fibbad(n):
    if(n == 2): return 1
    if(n == 1): return 0
    return fibbad(n-1) + fibbad(n-2)

#key value, key so that n-2 is 0, and n-1 is 1
#-----------------------
def fibrecmemo(n, memo = {1 :0, 2: 1}):
    if n in memo:
        return memo[n]
    else:
        memo[n] = fibrecmemo(n-1, memo) + fibrecmemo(n-2, memo);
        return memo[n]
#-----------------------
def fibiter(n):
    if(n == 1): return 1
    if(n == 0): return 0
    if(n == 2): return 2
    fibtescurrent = 0;
    store = [0 , 1] #default fib, 0 index is prev res, 1 index is curr res
    while(n > 2):
        n = n - 1
        fibtescurrent = store[1] #  save before modding
        store[1] = fibtescurrent + store[0]
        store[0] = fibtescurrent
    return store[1]

print(fibbad(7))

print(fibrecmemo(7))
print(fibiter(7))

