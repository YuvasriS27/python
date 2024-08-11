string = "abcde"
count = 0
vowels = ('a', 'e', 'i', 'o', 'u')

for ch in string:
    if ch in vowels:
        continue
    count += 1

print(count)
