def pn(n):
    if n > 0:
        pn(n - 1)
        print(n)


if __name__ == "__main__":
    pn(10)