def area(base,altura):
    return base*altura

def main():
    b = float(input("Dame la base: "))
    a = float(input("Dame la altura: "))

    r = area(b,a)

    print("El área del rectángulo es:",r)

if __name__=='__main__':
    main()
