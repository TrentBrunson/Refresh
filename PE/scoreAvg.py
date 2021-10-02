# Trent Brunson
# Question 2

score = []
print("Enter 3 scores to get the average of the highest 2 scores.")
score.append(int(input("Enter score #1 (integers only): ")))
score.append(int(input("Enter score #2 (integers only): ")))
score.append(int(input("Enter score #3 (integers only): ")))
score.sort(reverse=True)
avg = (score[0] + score[1]) / 2
# print(score, type(score), avg)
print(f"The average of the two highest scores is: {avg}")