#!/usr/bin/env python3

def print_formatted(number):
    # your code goes here
    if(number >= 1 and number <= 99):
        for i in range(1, number+1):
            num1 = DectoOct(i)
            num2 = DectoHex(i)
            num3 = DectoBin(i)
            print(i,num1,num2,num3)
def DectoOct(num):
    octal = 0
    n = 1
    while(num!=0):
        octal = octal + (num % 8) * n
        num = int(num/8)
        n = n * 10
    return octal
def DectoHex(n):
    hex_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
    reversed_number = ""
    while n > 0:
        remainder = n % 16
        n -= remainder
        n //= 16
        reversed_number += str(hex_values[remainder])

    return(reversed_number[::-1])
def DectoBin(num):
    binary = 0
    n = 1
    while(num!=0):
        binary = binary + (num%2) * n
        num = int(num/2)
        n = n * 10
    return binary

n = int(input())
print_formatted(n)
