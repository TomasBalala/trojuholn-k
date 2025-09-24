import math
a=int(input("zadaj stranu a:"))
b=int(input("zadaj stranu b"))
c=int(input("zadaj stranu c"))
#testujem či je to trojuholník
if (a+b>c) and (a+c>b) and (b+c>a):
    print("je to trojuholník")
    #testujem či je pravouhlý
    if (a**2+b**2==c**2) or (a**2+c**2==b**2) or (c**2+b**2==a**2):
        print("je to trojuholník - pravouhly")
    #testujem či je rovnostranný
    if (a==b==c):
        print("trojuholník je ronvostranný")
    #testujem či je rovnoramenny
    if (a==b and a!=c) or (a==c and b!=c) or (b==c and a!=c):
        print("trojuholník je rovnoramenny")
o=(a+b+c)
po=o/2
S=(po*(po-a)*(po-b)*(po-c))**0.5
va=S*2/a
vb=S*2/b
vc=S*2/c
p_vpis=S/po
p_opis1=(a*b*c)/(4*S)
#pocitam uhly
alpha=round(math.degrees(math.acos((b**2+c**2-a**2)/(2*b*c))),2)
beta=round(math.degrees(math.acos((a**2+c**2-b**2)/(2*a*c))),2)
gama=round(math.degrees(math.acos((b**2+a**2-c**2)/(2*b*a))),2)
print("obvod je:"+str(o))
print("obsah je:"+str(S))
print("vyska a je:"+str(va))
print("vyska a je:"+str(vb))
print("vyska a je:"+str(vc))
print("polomer vpisanej je:"+str(p_vpis))
print("polomer opisanej je:"+str(p_opis1))
print("alpha je:"+str(alpha))
print("beta je:"+str(beta))
print("gama je:"+str(gama))
p_opis2=(a)/(2*math.sin(math.radians(alpha)))


import string
#obvod, obsah, uhly, výšky, taznice, polomer vpisanej, polomer opisanej
#stredne preicky
#vlastnosti: pravouhly, ostrouhly, rovnostraný, rovnoramenny
