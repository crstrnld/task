def pertukaran_nilai(x, y):
    x, y = y, x
    return x, y

x = float(input("nilai x: "))
y = float(input("nilai y: "))
x, y = pertukaran_nilai(x, y)
print(f"setelah ditukar, x menjadi: {x} dan y menjadi1: {y}")
