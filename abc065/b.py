import sys


def main():
    n = int(input())
    buttons = [int(input()) for _ in range(n)]

    def push(x):
        return buttons[x - 1]

    seq = [push(1)]

    for _ in range(n):
        if seq[-1] == 2:
            print(len(seq))
            return 0
        seq += [push(seq[-1])]

    print(-1)

    return 0


if __name__ == '__main__':
    sys.exit(main())
