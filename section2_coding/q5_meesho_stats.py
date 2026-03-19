n = int(input())
sales = list(map(int, input().split()))

# step 1 - mean
total = 0
for val in sales:
    total = total + val
mean = total / n

# step 2 - median using bubble sort (no sorted() or .sort())
arr = sales[:]
for i in range(n - 1):
    for j in range(n - 1 - i):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

if n % 2 == 1:
    median = arr[n // 2]
else:
    median = (arr[n // 2 - 1] + arr[n // 2]) / 2

# step 3 - mode using nested loops
# if tie, pick the smallest value
max_freq = 0
mode = sales[0]

for i in range(n):
    freq = 0
    for j in range(n):
        if sales[j] == sales[i]:
            freq = freq + 1
    if freq > max_freq:
        max_freq = freq
        mode = sales[i]
    elif freq == max_freq and sales[i] < mode:
        mode = sales[i]

print(f"Mean: {mean:.2f}")
print(f"Median: {float(median):.2f}")
print(f"Mode: {mode}")
