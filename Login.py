#the correct ahh password

password = "python123"

#variable to store the user input

attempt = ""

#tracks the number of tries

tries = 0

#Looop continues while the password is wrong AND the user has tries left
while attempt != password and tries < 3:
    attempt = input("Enter the password: ") #Ask user to type the password
    tries += 1 #Add 1 to the number of tries

    #Check if password is wrong
    if attempt != password:
        print("Haha you're like, really wrong dude.")

#Once loop ends, check why it ended
if attempt == password:
    print("Dude, you're like, really right. ooh boy.") #if password is correct
else:
    print("Get out. I don't ever want to see your face here again.") #if user ran out of tries        

