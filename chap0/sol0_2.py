import math
from readint import readinput


def calc_theta(c, n):
    ans = 0
    for i in range(n+1):
        ans += math.pow(c, i)
    return ans


def main():
    clist = [0.5, 1, 2]
    print ("Please enter \"n\" value below")
    n = readinput()
    for c in clist:
        theta = calc_theta(c, n)
        print("for c:%0.2f and n:%d, theta is: %0.2f" % (c, n, theta))


if __name__ == '__main__':
    main()
