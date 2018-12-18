def main():
    p = 1/8
    for l in range(2,6):
        ans = l / ((1 - (1 - p)**(2**l - 1))/p)
        print("l" + str(2**l - 1) + " = " + str(ans))


if __name__ == "__main__":
    main()
