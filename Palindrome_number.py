number = int(input("Please enter a number: "))
temp = number
x = 0
while number > 0 :
    y = number%10
    print(y)
    x = (x*10)+y
    print(x)
    number = number//10
    print(number)
if temp == x:
    print('Palindrome')
else:
    print('Not palindrome')


