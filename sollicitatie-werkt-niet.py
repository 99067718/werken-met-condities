print("Hallo en welkom bij dit sollicitatiegebeuren, vul de vragenlijst eerlijk in.")
print("")

naam = input("Wat is uw Naam? : ")

#onzinvraag 1
input("Heeft u wel eens een kat door de wc gespoeld? ")

aw1 = int(input("Hoeveel jaar praktijk ervaring heb je met acrobatiek? "))
MBO = input("Heeft u een MBO diploma?(beantwoord met y/n): ").upper()
if MBO == "Y":
    aw2 = int(input("Welk niveu MBO diploma heeft u? : "))
else:
    aw2 = 0

#onzinvraag 2
input("Heeft u wel eens een alien ontmoet, en er een diner mee gehad? ")

aw3 = input("Heeft u een vrachtwagen rijbewijs? (beantwoord met y/n): ").upper()
aw4 = input("Heeft u een hoge hoed? (beantwoord met y/n): ").upper()

#onzinvraag 3
input("Heeft u ooit sinterklaas geslagen? ")

aw5 = input("bent u een man of vrouw (antwoord met m/v): ").upper()

if aw5 == "M":
    aw5 = input("Heeft u een snor breder dan 10 cm? (beantwoord met y/n): ").upper()
else:
    aw5 = input("Heeft u lang rood krulhaar langer dan 20 cm? (beantwoord met y/n): ").upper()

aw6 = int(input("Hoe lang bent U? "))

#onzinvraag 4
input("Heeft u kippen onder uw bed?: ")

aw7 = int(input("Hoeveel weegt U?: "))
aw8 = input("Heeft u een certificaat \"overleven met gevaarlijk personeel?\"(beantwoord met y/n): ").upper

print("We zijn uw resultaat aan het berekenen.")

if aw1 >= int(4) and aw2 >= int(4) and aw3[0] == "Y" and aw4[0] == "Y" and aw5 == "Y" and aw6 >= int(150) and aw7 >= int(90) and aw8 == "Y":
    print("Gefeliciteerd," + naam + " u voldoet aan al onze eisen!!!")
else:
    print("Sorry, "+ naam + " maar u voldoet niet aan onze eisen.")
 
    
    
    
   