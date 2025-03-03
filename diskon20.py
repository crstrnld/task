def total_pembayaran(dibayar):
    discount = dibayar * 0.20
    pembayaran = dibayar - discount
    return pembayaran

dibayar = float(input("harga awal:"))
pembayaran = total_pembayaran(dibayar)
print(f"harga setelah mendapat discount 20% adalah: {pembayaran}") 