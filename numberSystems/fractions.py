# 
import math

# Umrechung einer
# natürlichen Zahl im Dezimalsystem in eine Zahl zur Basis base.
# Das Ergebnis wird als String ausgegeben.
# Sinnvoll sind nur Basiswerte kleiner als 10,
# da keine Symbole wie A, B, C, D, E oder F
# wie für hexadezimale Zahlen verwendet werden.
# Es wäre möglich, dies einzubauen. 
# Aber darauf wurde verzichtet.
def Natural2Placesystem(num, base) : 
    result = ""    
    # Wir bestimmen k, die Anzahl der Ziffern
    k = math.floor(math.log(num, base)) + 1
    divisor = base**(k-1)
    while (k>0) :         
        digit = num // divisor  
        num = num % divisor 
        # Ziffer in String speichern 
        result += str(digit);  
  
        k -= 1        
        divisor //= base
        
    return result

# Umwandlung einer rationalen Zahl m/n 
# in einen Bruch zur Basis b.
# Dabei wird die Berechnung abgebrochen,
# wenn ein Rest 0 wird oder die 
# gesetzte Anzahl von Nachkommastellen erreicht ist.
def rationalToPlacesystem(m, n, base, precision = 10) : 
  
    result = ""  
  
    # Den ganzzahligen Anteil n bestimmen 
    g = m // n  
    if g > 0 : 
        result = Natural2Placesystem(g, base) + "." 
    else:
        result = "0."
           
    # Den Anteil der Zahl nach dem Dezimalpunkt bestimmen  
    r0 = m - g*n
  
    # Hier noch meinen Algorithmus einbauen,
    # mit allgemeiner Basis und eventuell auch
    # ein Stop vor k_prec, wenn 
    while (precision>0 and r0>0) :            
        r0 *= base
        d = r0 // n
        result += str(d)
        r0 -= d*n 
        precision -= 1

    return result  

def decimalToBinary(num, k_prec) : 
  
    binary = ""  
  
    # Den ganzzahligen Anteil n bestimmen 
    # Dazu verwenden wir einen Cast von double auf int
    g = int(num)  
    print(g)
    # Den Anteil der Zahl nach dem Dezimalpunkt bestimmen  
    r0 = num - g 
  
    if g > 0 : 
        binary = Natural2Base(g, 2) + "." 
    else:
        binary = "0."
  
 
    # Hier noch meinen Algorithmus einbauen,
    # mit allgemeiner Basis und eventuell auch
    # ein Stop vor k_prec, wenn 
    while (k_prec) : 
          
        # Find next bit in fraction  
        r0 *= 2
        fract_bit = int(r0)  
  
        if (fract_bit == 1) : 
              
            r0 -= fract_bit  
            binary += '1'
              
        else : 
            binary += '0'
  
        k_prec -= 1

    return binary  
