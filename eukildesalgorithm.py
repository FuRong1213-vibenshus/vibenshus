def EuklidsMetodeForFellesFaktorAv(a, b):
    while a != 0:
        
        a, b = max(a, b), min(a, b) # Definerer a til å være den største av a og b.
        print(a, '=', (a//b),'*',b,'+',a%b)
        a = a % b # Redefinerer a til å være resten etter divisjonen a / b. 
    print("sdf er:", b)
    return b

def LosningAvDiofantiskLikningMedKoeffisienter(a, b):
    if a < b:
        return LosningAvDiofantiskLikningMedKoeffisienter(b, a)
    if (b == 0):
        return a, 1, 0
    else:
        sff, x, y = LosningAvDiofantiskLikningMedKoeffisienter(b, a % b)
    x, y = y, (x - (a // b) * y)
    print(sff, '=', x,'*', a, '+', y,'*',b)
    return sff, x, y
print("Input two non-negative integers a and b such that a>=b")
a, b = map(int, input().split())
EuklidsMetodeForFellesFaktorAv(a, b)
print("-----------------------------------------")
LosningAvDiofantiskLikningMedKoeffisienter(a,b)