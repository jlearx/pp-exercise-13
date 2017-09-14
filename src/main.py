'''
Created on Sep 14, 2017

@author: jlearx
'''

def GetFibonacci(count):
    fibonacci = [1]
    prevNum = 0
    
    for i in range(1,count):
        newNum = fibonacci[i - 1] + prevNum
        fibonacci.append(newNum)
        prevNum = fibonacci[i - 1]
    return fibonacci

if __name__ == '__main__':
    print("Fibonacci Generator")
    count = 0
    
    while (count < 1):
        count = int(input("How many Fibonacci numbers would you like? "))
    
    fibonacci = GetFibonacci(count)
    print(fibonacci)
    