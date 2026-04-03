
def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)

#-------------------------------
absolute = lambda val: val if val >= 0 else -val


def exp_x(x, n):
    totalSum = 0
    for i in range(n):
        term_val = (x ** (2 * i)) / factorial(2 * i)
        if i % 2 == 0:
            totalSum += absolute(term_val)
        else:
            totalSum -= absolute(term_val)

    return totalSum


#------------------------------
gn_total = 0


def calculate_gn(n, r):

    global gn_total
    if n < 0:
        return
    gn_total += r ** n
    calculate_gn(n - 1, r)

ex = float(input("Enter value x: "))

en = int(input("Enter number of terms: "))

resultX = exp_x(ex, en)
print("Result of S:", resultX)

print()
en_geo = int(input("Enter n max power: "))
ar_geo = float(input("Enter common ratio: "))
gn_total = 0
calculate_gn(en_geo, ar_geo)
print("Result of Gn:", gn_total)