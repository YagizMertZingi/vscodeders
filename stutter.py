def stutter(word):
    prfx = word[:2]  # İlk iki harfi al
    return f"{prfx}... {prfx}... {word}?"

while True:
    word = input("Bir kelime girin (Çıkış için 'q' tuşlayın): ")
    
    if word.lower() == "q":
        print("Çıkış yapılıyor...")
        break

    if word.strip():
        print(stutter(word))
    else:
        print("Lütfen geçerli bir kelime girin!")
