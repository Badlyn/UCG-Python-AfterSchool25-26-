#1. This stores the user's input. This is where the magic starts, heh.

word = str(input("Please enter a word, heh: "))

#2. Creates a place to store the reversed word


re_word = ""

#3. Starts from the last letter of the word

i = len(word) - 1

#4. Starts a while loop

while i >= 0:

#5. Inside the loop, it adds the current letter to the reversed word

    re_word += word [i]

#6. Moves one step backward to the previous letter

    i -= 1

#7. Print the final reversed word    

print(re_word)