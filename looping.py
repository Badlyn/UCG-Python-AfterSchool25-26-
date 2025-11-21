#Program Description: Checking multiples of 5 from numbers 1-20 tee hee

#Creating list called numbers

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]


#For loop to check numbers divisible by 5
for i in numbers:
    if i % 5 == 0:
        print(i)