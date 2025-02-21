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
    giris = input("Bir sayı girin (Çıkış için 'q' tuşuna basınız): ") 
    
    if giris.lower() == "q": 
        print("Çıkış yaptın") 
        break

    if giris.isdigit():  
        sayi = int(giris)
        print(fizzbuzz(sayi))
    else:
        print("Lütfen geçerli bir sayı girin!")
