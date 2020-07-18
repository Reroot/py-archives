def productSum(array = [1,2, 3], multiplier = 1):
    runningsum = 0
    for element in array:
        if type(element) is list:
            runningsum += productSum(element, multiplier + 1)
        else:
            runningsum += element
    return runningsum * multiplier


#ans 20
ar = [1, 3, [4, 1], 6]
print(productSum(ar))
