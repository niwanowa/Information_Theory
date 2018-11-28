import math


def main():
    m = input("Probability of occurrence : ").split()
    # m = ("1/100 " *100).split()
    print(m)
    h = 0
    p = []

    for i, formula in enumerate(m):
        p.append(eval(formula))
        h += p[i] * math.log2(p[i])
        information_volume = - math.log2(p[i])
        print("P{} = {} , I = {}".format(i+1, p[i], information_volume))

    h *= -1
    r = 1 - (h/math.log2(len(m)))

    print("p = " + str(p))
    print("H(s) = " + str(h))
    print("r(S) = " + str(r))


if __name__ == '__main__':
    main()
