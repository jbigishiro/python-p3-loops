#!/usr/bin/env python3

def happy_new_year():
    num=10
    while num>0:
        print(num)
        num-=1
    print("Happy New Year!")

def square_integers(int_list):
   return [num**2 for num in int_list]

def fizzbuzz():
    num=1
    while num <= 100:
        if num % 5 == 0 and num % 3 == 0 :
            print("FizzBuzz")
        elif num % 5 ==0:
            print("Buzz")
        elif num % 3 ==0:
            print("Fizz")
        else:
            print(num)
        num+=1