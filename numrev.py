#meant to like, put numbers in reverse. Does it to letters too haha!

n = input("Enter the heh, number: ")

rev = ""
i = len(n) - 1

while i >= 0:
    rev = rev + n[i]
    i -= 1
print(f"The friggan number is: {rev}")