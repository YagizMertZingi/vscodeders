def f(liste):
    if len(liste) == 0:
        return 0
    else: 
        return liste[0] + f(liste[1:])
    
liste = [1, 2, 3, 4, 5 ,6 ,7 ,8, 9, 10]

print(f(liste = liste))

