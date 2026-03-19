n = int(input())
orders = input().split()

# building a unique list of categories manually - no Counter or dict.get allowed
categories = []

for o in orders:
    found = False
    for c in categories:
        if c == o:
            found = True
            break
    if not found:
        categories.append(o)

# sorting categories alphabetically using bubble sort
m = len(categories)
for i in range(m - 1):
    for j in range(m - 1 - i):
        if categories[j] > categories[j + 1]:
            temp = categories[j]
            categories[j] = categories[j + 1]
            categories[j + 1] = temp

# counting each category using nested loop
for cat in categories:
    count = 0
    for o in orders:
        if o == cat:
            count = count + 1
    print(cat + ": " + str(count) + " orders")
