n = int(input())
scores = list(map(int, input().split()))
pass_mark = int(input())

passed = 0

for s in scores:
    if s >= pass_mark:
        passed = passed + 1

failed = n - passed

# calculating pass rate
pass_rate = (passed / n) * 100

print("Passed:", passed)
print("Failed:", failed)
print(f"Pass Rate: {pass_rate:.2f}%")
