n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()

result = 0
count = 0

first = data[-1]
second = data[-2]


while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)