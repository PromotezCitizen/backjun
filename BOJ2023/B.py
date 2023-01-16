# No. 27232

n, k = map(int, input().split())
a = list(map(int, input().split()))

if (k == 1):
    print(0)
    exit()

a = [ [idx, value] for idx, value in enumerate(a) ]

min_clean = 9999
for i in range(n-k+1):
    temp = a[i:i+k]
    temp.sort(key=lambda x: -x[1])
    p = 0
    for _ in range(len(temp)-1):
        p += abs(temp[0][0] - temp[1][0])
        temp.pop(0)
    min_clean = min(min_clean, p)
    
print(min_clean)
# n - k == iter max