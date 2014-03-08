while True:
    s = input("Please enter a number: ")
    try:
        x = int(s)
        break  # остановить цикл
    except ValueError:
        print("Can't parse '{0}' as number.".format(s))
    print("Try again")

print("You entered:", x)
