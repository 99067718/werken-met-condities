#99067718
#Emiel 't Lam
#de prints die leeg zijn, zijn er om het een beetje overzichtelijk te houden tijdens het invullen


DoesQualify = True
print("")
print("Hallo en welkom bij dit sollicitatiegebeuren, vul de vragenlijst eerlijk in.")
print("")
naam = input("Wat is uw Naam? : ")
print("")

#onzinvraag 1
input("Heeft u wel eens een kat door de wc gespoeld? ")
print("")
antw = int(input("Hoeveel jaar praktijk ervaring heb je met acrobatiek? "))
if antw >= 4:
    print("")
else:
    print("")
    DoesQualify = False

MBO = input("Heeft u een MBO diploma? y/n: ").upper()
if MBO == "Y":
    antw = int(input("Welke diploma??(Nummer): "))
    if antw >= 4:
        print("")
    else:
        print("")
        DoesQualify = False
else:
    print("")
    DoesQualify = False

#onzinvraag 2
input("Heeft u wel eens een alien ontmoet, en er een diner mee gehad? ")
print("")

antw = input("Heeft u een vrachtwagen rijbewijs? (beantwoord met y/n): ").upper()
if antw == "Y":
    print("")
else:
    print("")
    DoesQualify = False


antw = input("Heeft u een hoge hoed? (beantwoord met y/n): ").upper()
if antw == "Y":
    print("")
else:
    print("")
    DoesQualify = False


#onzinvraag 3
input("Heeft u ooit sinterklaas geslagen? ")
print("")

gen = input("bent u een man of vrouw (antwoord met m/v): ").upper()

if gen == "M":
    antw = input("Heeft u een snor breder dan 10 cm? (beantwoord met y/n): ").upper()
else:
    antw = input("Heeft u lang rood krulhaar langer dan 20 cm? (beantwoord met y/n): ").upper()
if antw == "Y":
    print("")
else:
    print("")
    DoesQualify = False


antw = int(input("Hoe lang bent U? "))
if antw >= 150:
    print("")
else:
    print("")
    DoesQualify = False

#onzinvraag 4
input("Heeft u kippen onder uw bed?: ")
print("")

antw = int(input("Hoeveel weegt U?: "))
if antw >= int(90):
    print("")
else:
    print("")
    DoesQualify = False


antw = input("Heeft u een certificaat overleven met gevaarlijk personeel?(beantwoord met y/n): ").upper()
if antw == "Y":
    print("")
else:
    print("")
    DoesQualify = False

if DoesQualify == True:
    print("Gefeliciteerd," + naam + " u voldoet aan al onze eisen!!!")
else:
    print("Sorry, "+ naam + " maar u voldoet niet aan onze eisen.")




