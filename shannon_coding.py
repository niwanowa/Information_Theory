# input ex)1/8 3/16 3/8 1/16 1/4
import math


def main():
    m = input("Probability of occurrence : ").split()
    a = {}
    cumulative_value = 0
    for k, formula in enumerate(m):
        a["a{}".format(k+1)] = eval(formula)
    sorted_a = sorted(a.items(), key=lambda x:x[1], reverse=True)
    sorted_a = [list(i) for i in sorted_a]
    for i, _a in enumerate(sorted_a):
        code_length = math.ceil(- math.log2(_a[1]))
        sorted_a[i].append(code_length)
        sorted_a[i].append(floattobin(cumulative_value))
        cumulative_value += _a[1]
    print(sorted_a)
    ave = 0
    for tmp in [i[1] * i[2] for i in sorted_a]:
        ave += tmp
    print("average cumulative value = ", ave)


def floattobin(p):
    i = 0
    bined="0."
    for _ in range(10):
        i -= 1
        if p >= 2**i:
            p -= 2**i
            bined += "1"
        else :
            bined += "0"
        if p == 0:
            break
    return bined

if __name__ == '__main__':
    main()
