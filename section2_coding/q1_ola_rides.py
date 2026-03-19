n = int(input())
times = list(map(int, input().split()))

# calculating total, shortest and longest using loops
total = 0
shortest = times[0]
longest = times[0]

for t in times:
    total = total + t
    if t < shortest:
        shortest = t
    if t > longest:
        longest = t

ride_range = longest - shortest

# bubble sort to find IQR
arr = times[:]  # making a copy so i don't mess up original list

for i in range(n - 1):
    for j in range(n - 1 - i):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

q1 = arr[n // 4]
q3 = arr[(3 * n) // 4]
iqr = q3 - q1

print("Total Ride Time:", total, "min")
print("Shortest Ride:", shortest, "min")
print("Longest Ride:", longest, "min")
print("Ride Duration Range:", ride_range, "min")
print("IQR:", iqr, "min")
