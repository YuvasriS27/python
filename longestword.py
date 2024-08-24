string = "Yuva sri sekaran"
length = ""
longest_word = ""
max_count = 0
count = 0
for s in string:
    if s != " ":
        length += s
        count += 1
    else:
        if count > max_count:
            max_count = count
            longest_word = length
        length = ""
        count = 0
if count > max_count:
    longest_word = length

print("The longest word is:", longest_word)
