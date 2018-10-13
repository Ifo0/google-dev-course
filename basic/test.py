import sys

def front_back(a, b):
    lenght_first = len(a)
    lenght_second = len(b)
    if len(a) % 2 == 0:
        a_first_half = a[:len(a) // 2]
        a_second_half = a[-len(a_first_half):]
    if len(a) % 2 != 0:
        a_first_half = a[:len(a) // 2 + 1]
        a_second_half = a[-(len(a_first_half) - 1):]
    if len(b) % 2 == 0:
        b_first_half = b[:len(b) // 2]
        b_second_half = b[-len(b_first_half):]
    if len(b) % 2 != 0:
        b_first_half = b[:len(b) // 2 + 1]
        b_second_half = b[-(len(b_first_half) - 1):]
    return a_first_half + b_first_half + a_second_half + b_second_half

def main():
    print front_back(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
  main()
