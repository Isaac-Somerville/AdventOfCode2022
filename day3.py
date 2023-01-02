with open('day3.txt') as f:
    lines = f.readlines()
    
input = []
for str in lines:
    input.append(str.strip())
    
print(input)

# score = 0
# test = ["vJrwpWtwJgWrhcsFMMfFFhFp",
# "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
# "PmmdzqPrVvPwwTWBwg",
# "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
# "ttgJtRGJQctTZtZT",
# "CrZsJsPPZsGzwwsLwLmpwMDw"]
# for cargo in input:
#     n = len(cargo)
#     l, r = set(cargo[:n//2]), set(cargo[n//2:])
#     for char in cargo:
#         if char in l and char in r:
#             duplicate = char
#             break
#     if char.isupper():
#         score += ord(char) - 38
#     else:
#         score += ord(char) - 96
        
# print(score)

score = 0
test = ["vJrwpWtwJgWrhcsFMMfFFhFp",
"jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
"PmmdzqPrVvPwwTWBwg",
"wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
"ttgJtRGJQctTZtZT",
"CrZsJsPPZsGzwwsLwLmpwMDw"]

i = 0 
while i < len(input):
    group = input[i:i+3]
    two, three = set(group[1]), set(group[2])
    for char in group[0]:
        if char in two and char in three:
            break
    print(char)
    if char.isupper():
        score += ord(char) - 38
    else:
        score += ord(char) - 96
    i += 3
        
print(score)
    