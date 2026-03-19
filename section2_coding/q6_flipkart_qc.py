# Newton-Raphson square root - no math import allowed
def my_sqrt(x):
    if x == 0:
        return 0.0
    guess = x / 2.0
    for _ in range(50):
        guess = (guess + x / guess) / 2.0
    return guess

# manual absolute value
def my_abs(x):
    if x < 0:
        return -x
    return x


m = int(input())
total_defective = 0

for batch_num in range(1, m + 1):
    n = int(input())
    scores = list(map(int, input().split()))

    # mean
    total = 0
    for s in scores:
        total = total + s
    mean = total / n

    # variance
    variance = 0
    for s in scores:
        diff = s - mean
        variance = variance + diff * diff
    variance = variance / n

    # std deviation using newton raphson
    std_dev = my_sqrt(variance)

    # z-score flagging
    defective = 0

    if std_dev == 0:
        result_line = "No outliers — all scores identical."
    else:
        for s in scores:
            z = (s - mean) / std_dev
            z = my_abs(z)
            if z > 1.5:
                defective = defective + 1
        result_line = "Defective Products: " + str(defective)
        total_defective = total_defective + defective

    print("Batch " + str(batch_num) + ":")
    print(f"  Mean Score : {mean:.2f}")
    print(f"  Std Deviation : {std_dev:.2f}")
    print("  " + result_line)

print("Total Defective Products:", total_defective)
