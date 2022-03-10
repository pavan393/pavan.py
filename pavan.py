if name == 'main':   
    n = int(input())
    
    arr = list(map(int, input().rstrip().split()))
    for i in range(n):
        print(arr[-i-1],end=' ')
n = int(input())
arr = []
for i in range(n):
    ip = input()
    try:
        arr.append(int(ip))
    except:
        arr = list(map(int, ip.split(' ')))
        break
    
    
mydict = {}
for i in range(n):
    for j in range(n):
        for k in range(n):
            if arr[k] == 0:
                continue 
            else :
                value = arr[k]*(arr[j] + arr[i])
                if value in mydict :
                    mydict[value] += 1
                else :
                    mydict[value] = 1
count = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            value = arr[k] + (arr[i] * arr[j])
            if value in mydict :
                count +=  mydict[value]
print(count)