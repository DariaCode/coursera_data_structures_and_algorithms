# Uses python3
# import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    cached = [previous, current]

    for i in range(n):
        old = current
        current = (previous + current) % m
        previous = old
        if previous == 0 and current == 1:
            cached.pop()
            break
        else:
            cached.append(current)

    return cached[n % len(cached)]

if __name__ == '__main__':
#    input = sys.stdin.read();
    n, m = map(int, input().split())
    print(get_fibonacci_huge_naive(n, m))
