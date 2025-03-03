def operasi(no1, no2):
    pertambahan = no1 + no2
    pengurangan = no1 - no2
    perkalian = no1 * no2
    pembagian = no1 / no2 if no2 != 0 else "tak terdefinisi"
    return pertambahan, pengurangan, perkalian, pembagian

no1 = float(input("masukan bilangan pertama:"))
no2 = float(input("masukan bilangan ke dua:"))
pertambahan, pengurangan, perkalian, pembagian = operasi(no1, no2)
print(f"ini jawaban anda:")
print(f"pertambahan: {pertambahan}")
print(f"pengurangan: {pengurangan}")
print(f"perkalian: {perkalian}")
print(f"pembagian: {pembagian}")


