yil = int(input("Bir yıl giriniz: "))

if yil < 1582:
    print("Bu yıl Gregoryen takvimine dahil değildir.")
elif yil % 4 != 0:
    print("Normal yıl")
elif yil % 100 != 0:
    print("Artık yıl")
elif yil % 400 != 0:
    print("Normal yıl")
else:
    print("Artık yıl")
