# Uses python3
import sys

def fibonacci_sum(n):
    previous = 0
    current  = 1
    sum      = 1

    '''
    fib(60) last digit is 0 and fib(61) last digit is 1, 
    that is same as fib(0) and fib(1), 
    thus starting at 60 last digits starts to repeat
    '''
    repeat_period = 60
    index = n % repeat_period

    if index<1:
        return index

    for _ in range(2, index+1):
        previous, current = current, (previous + current)%10
        sum = (sum + current)%10

    return sum

if __name__ == '__main__':
#    input = sys.stdin.read()
    n = int(input())
    print(fibonacci_sum(n))
