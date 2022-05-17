#Write a program that prints the numbers from 1 to 100.
#But for multiples of three, print Fizz instead of the number, and multiples of five, print Buzz.
#For numbers that are multiples of both three and five, print FizzBuzz
for i in range(100):
    a = (1+i)
    print (a)
    if a%3 == 0 and a%5 == 0:
        print ("FizzBuzz")
    
    elif a%3 == 0:
        print ("Fizz")
    elif a%5 == 0:
        print ("Buzz")
    else:
        ()