# find all subarray for an an array

arr = [1,2,3]
ans = []

for i in range(len(arr)):
    for j in range(i,len(arr)):
        ans.append(arr[i:j+1])


print(ans)

    