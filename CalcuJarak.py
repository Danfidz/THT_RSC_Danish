# Danish Muhammad Hafidz
# 16521436


print("masukkan lokasi dengan format latitude, longitude, altitude")
print("contoh: 2, 4, 5")
loc1 = input("Masukkan lokasi 1: ").split(", ")
loc2 = input("Masukkan lokasi 2: ").split(", ")

kuadrat = 0

for i in range(len(loc1)):
    a = (int(loc1[i])-int(loc2[i]))**2
    kuadrat += a


hasil = (kuadrat)**(1/2)
print(f"Jarak koordinat 1 dengan 2 adalah {hasil} meter")
