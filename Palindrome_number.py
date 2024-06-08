number = int(input("Please enter a number: "))
temp = number
x = 0
while number > 0 :
    y = number%10
    x = (x*10)+y
    number = number//10
if temp == x:
    print('Palindrome')
else:
    print('Not palindrome')


