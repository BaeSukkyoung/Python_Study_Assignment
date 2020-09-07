n=input()

if n % 4 == 0:
    print('Fizz')
elif n % 7 == 0:
    print('Buzz')
elif (n % 4 == 0) & (n % 7 == 0):
    print('FizzBuzz')