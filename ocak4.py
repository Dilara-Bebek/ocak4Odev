# Kullanıcıdan 5 adet sayı alarak liste oluşturma
sayilar = []
for i in range(5):
    sayi = float(input(f"{i+1}. sayıyı girin: "))
    sayilar.append(sayi)

toplam = sum(sayilar)
ortalama = toplam / len(sayilar)
en_buyuk = max(sayilar)
en_kucuk = min(sayilar)

print(f"Liste: {sayilar}")
print(f"Toplam: {toplam}")
print(f"Ortalama: {ortalama}")
print(f"En büyük sayı: {en_buyuk}")
print(f"En küçük sayı: {en_kucuk}")

# Kullanıcıdan kelimeler alarak listeye ekleyip ters sıralama
kelimeler = []
adet = int(input("Kaç kelime gireceksiniz? "))

for i in range(adet):
    kelime = input(f"{i+1}. kelimeyi girin: ")
    kelimeler.append(kelime)

kelimeler.reverse()
print(f"Ters sıralanmış liste: {kelimeler}")

# Bir listede tekrar eden elemanları kaldırma
orijinal_liste = [1, 2, 3, 4, 2, 3, 5, 6, 1, 7]
benzersiz_liste = list(set(orijinal_liste))  # Set kullanarak tekrar edenleri kaldırma

print(f"Orijinal liste: {orijinal_liste}")
print(f"Tekrarsız liste: {benzersiz_liste}")
