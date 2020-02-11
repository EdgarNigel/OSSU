# Problem Set 1.1

def vowelcheck(word):
    vow = 0
    for letter in word:
        if letter in ['a', 'o', 'u', 'i', 'e']:
            vow += 1
    print ("Number of vowels: " + str(vow))

# Problem Set 1.2

def bobcheck(word):
    count = 0
    for i in range(len(word)-2):
        if word[i] == "b" and word[i+1] == "o" and word[i+2] == "b":
            count += 1
    print("Number of times bob occurs is: " + str(count))


# Problem Set 1.3

def check_abc(word):
    longest = word[0]
    current = word[0]
    for letter in word[1:]:
        if letter >= current[-1]:
            current += letter
            if len(current) > len(longest):
                longest = current
        else:
            current = letter
    print("Longest substring in alphabetical order is:", longest)
