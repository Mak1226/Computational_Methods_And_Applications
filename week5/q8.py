import scipy.fft as sp

def calculate(x, y):
    d = len(str(x)) + len(str(y))
    m, n = x, y
    a, b = [], []
    for _ in range(d):
        a.append(m % 10)
        b.append(n % 10)
        m = int(m/10)
        n = int(n/10)

    # FFTs 
    a = sp.fft(a)
    b = sp.fft(b)
    p = a * b

    # Inverse FFT
    p = sp.ifft(p)

    # Actual Product
    s, e = 0, 0
    for i in p:
        s += pow(10,e) * i.real
        e += 1
    return s

try:
    x = int(input("Enter the 1st integer: "))
    y = int(input("Enter the 2nd integer: "))
    if x < 0 or y < 0:
        raise Exception("Enter only positive values")

    print(f"Computed Product: {int(calculate(x,y))}")
    print(f"Actual Product:   {x * y}")

except(ValueError):
    print("Enter only int values.")
