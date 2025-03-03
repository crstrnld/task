import math

def segitiga(alas, tinggi):
    luas = (alas * tinggi) / 2
    sisi_terpanjang = math.sqrt(alas ** 2 + tinggi ** 2)
    keliling = alas + tinggi + sisi_terpanjang
    return luas, keliling

alas = float(input("masukan panjang alas segitiga: "))
tinggi = float(input("masukan tinggi segitiga: "))
luas, keliling = segitiga(alas, tinggi)
print(f"Here are the triangle's properties:")
print(f"luas seegitiga: {luas} ")
print(f"keliling segiitiga: {keliling} ")
