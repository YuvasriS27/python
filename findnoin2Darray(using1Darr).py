array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
target = 5
found = False
for row in array:
    for num in row:
        if num == target:
            found = True
            break
print(found)
