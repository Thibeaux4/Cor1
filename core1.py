#basics 0-150
for i in range(151):
    print(i)


#Print all multiples of 5
for i in range(0, 1001, 5):
    print(i)


#Counting the dojo way
for i in range(0, 101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)


#Whoa. That Sucker's Huge
sum = 0
for i in range(0, 500000):
    if i % 2 == 1:
        sum += i
print(sum)


#Countdown by Fours
num = 2018
while num > 0:
    print(num)
    num -= 4


    #Flexible Counter
lowNum = 2
highNum = 9
mult = 3

for i in range(lowNum, highNum + 1):
    if i % mult == 0:
        print(i)