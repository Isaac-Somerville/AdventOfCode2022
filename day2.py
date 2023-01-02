with open('day2.txt') as f:
    lines = f.readlines()
    
res = []
for str in lines:
    res.append(str.strip())

    
# # Opponent: A rock, B paper, C scissors
# # Me: X rock, Y paper, Z scissor

# points = {"X" : 1, "Y" : 2, "Z" : 3}
# drawDict = {"X" : "A", "Y" : "B", "Z" : "C"}
# winDict = {"X" : "C", "Y": "A", "Z" : "B"}

# #test = ["A Y", "B X", "C Z"]
# score = 0
# for game in res:
#     them, me = game[0], game[-1]
#     score += points[me]
#     if winDict[me] == them:
#         score += 6
#     elif drawDict[me] == them:
#         score += 3
    
# print(score)


# Opponent: A rock, B paper, C scissors
# Me: X lose, Y draw, Z win

myPoints = {"A" : 1, "B" : 2, "C" : 3}
winDict = {"A" : "B", "B": "C", "C" : "A"}
loseDict = {"A" : "C", "B" : "A", "C" : "B"}

test = ["A Y", "B X", "C Z"]
score = 0
for game in res:
    them, outcome = game[0], game[-1]
    if outcome == "X":
        me = loseDict[them]
        score += myPoints[me]
    elif outcome == "Y":
        score += myPoints[them] + 3
    else:
        me = winDict[them]
        score += myPoints[me] + 6
    
print(score)


    
