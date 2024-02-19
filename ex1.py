import sys

def divise1(a ,b):
 c = a / b
 return c

def divise2(a,b):
    if b!=0:
        c= a/b
        return c
    else:
        print("division par zéro est pas possible")
        c="erreur"
        

def divise3(a,b):
    try:
        c = a/b
    except ZeroDivisionError as e:
        print(f" zero :\t {e}") 
    except TypeError as a:
        print(f" Type \t: {a}") 
    except Exception as t:
        print(t)    
    else:
        return c          


def main():
 a = float(input('saisir le nombre a '))
 b = float(input('saisir le nombre b '))
 #c = divise1(a,b)
 c = divise2(a,b)
 if c is not None:
    print(f'la division de {a}par {b} vaut {c}')

if __name__ == "__main__":
    sys.exit(main())

