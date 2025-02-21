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



def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n

while True:
    giris = input("Bir sayi girin (Çikiş için 'q' tuşuna basiniz): ") 
    
    if giris.lower() == "q": 
        print("Çikiş yaptin") 
        break

    if giris.isdigit():  
        sayi = int(giris)
        print(fizzbuzz(sayi))
    else:
        print("Lütfen geçerli bir sayi girin!")

