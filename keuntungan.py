def keuntungan(domba):
    harga_beli = 2500000
    harga_jual = 3000000
    jumlah_terbeli = harga_beli * domba
    total_terjual = harga_jual * domba
    profit = total_terjual - jumlah_terbeli
    return jumlah_terbeli, profit

domba = int(input("How many sheep did you sell? "))
jumlah_terbeli, profit = keuntungan(domba)
print(f"ini jumlah penghasilanmu:")
print(f"jumlah terbeli: {jumlah_terbeli}")
print(f"total keuntungan: {profit}")
