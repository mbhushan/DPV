# multiplication of 2 binary numbers using grade school technique
from binary_addition import binary_sum


def binary_number_input(msg):
    while True:
        x = input(msg)
        found = True
        for i in x:
            if i != '0' and i != '1':
                found = False
                print ("Bad binary input! Plz try again..")
                break
        if found:
            return x


def binary_mult(x, y):
    y = y[::-1]
    index = 0
    ilist = []
    for i in y:
        if i == '1':
            s = "0" * index
            z = x + s
            ilist.append(z)
        index += 1
    # for n in ilist:
    #    print (n)
    ans = "0"
    for n in ilist:
        ans = binary_sum(ans, n)
    print ("x * y = ", ans)


def main():
    x = binary_number_input("First Binary Number X: ")
    y = binary_number_input("Second Binary Number Y: ")
    binary_mult(x, y)


if __name__ == '__main__':
    main()
