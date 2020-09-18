# Uses python3
# import sys
from week2_3_gcd import gcd

def lcm_naive(a, b):
    # https://en.wikipedia.org/wiki/Least_common_multiple#:~:text=In%20arithmetic%20and%20number%20theory,by%20both%20a%20and%20b.
    # lcm(a,b) =|a*b| / gcd(a,b)
    return (a * b) // gcd(a, b)

if __name__ == '__main__':
#    input = sys.stdin.read()
    a, b = map(int, input().split())
    print(lcm_naive(a, b))

