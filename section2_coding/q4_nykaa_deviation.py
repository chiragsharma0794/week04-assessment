n = int(input())
prices = list(map(int, input().split()))

# step 1 - computing mean manually, no sum() allowed
total = 0
for p in prices:
    total = total + p

mean = total / n
print(f"Mean Price: Rs.{mean:.2f}")

# step 2 - absolute deviation for each product
# not using abs(), using if condition instead
for i in range(n):
    dev = prices[i] - mean
    if dev < 0:
        dev = -dev
    print(f"Product {i + 1}: Rs.{prices[i]} | Deviation: Rs.{dev:.2f}")
