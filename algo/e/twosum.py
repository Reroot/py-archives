def twosum(arr, target):
    map = {}
    for i in range(len(arr)):
        comp = target-arr[i]#look for thhis value type in our map later
        if(comp in map):
            return [map[comp], i]
        else:
            map[arr[i]] = i
            #key is arr[i], and value is the index
#map contains the comps, and the index as keys

input_list = [2,8,12,15]
print(twosum(input_list, 20))

