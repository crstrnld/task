def hitung_kembalian(pembelian, dibayar):
    return dibayar - pembelian
pembelian = float(input("masukan harga barang:"))
dibayar = float(input("berapa nominal uang yang keluar untuk membayar:"))
kembalian = hitung_kembalian(pembelian, dibayar)
print(f"kembalianmu berjumlah: {kembalian}")