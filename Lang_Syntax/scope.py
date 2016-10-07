#!/usr/bin/env python3.5

def five():
    global num
    num = num + 1

def main():
    global num
    num = 1
    five()
    print(num)

num = 0
main() 
print("Hello")