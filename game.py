#99067718
#Emiel 't Lam



print("Welkom bij...")
print(""" 

───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
─██████████████─██████████████─██████████████─██████████████─██████████████─██████████████────██████████████─██████──██████─██████████████─
─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██────██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░██─
─██░░██████████─██░░██████████─██░░██████████─██░░██████░░██─██░░██████░░██─██░░██████████────██████░░██████─██░░██──██░░██─██░░██████████─
─██░░██─────────██░░██─────────██░░██─────────██░░██──██░░██─██░░██──██░░██─██░░██────────────────██░░██─────██░░██──██░░██─██░░██─────────
─██░░██████████─██░░██████████─██░░██─────────██░░██████░░██─██░░██████░░██─██░░██████████────────██░░██─────██░░██████░░██─██░░██████████─
─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██─────────██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██────────██░░██─────██░░░░░░░░░░██─██░░░░░░░░░░██─
─██░░██████████─██████████░░██─██░░██─────────██░░██████░░██─██░░██████████─██░░██████████────────██░░██─────██░░██████░░██─██░░██████████─
─██░░██─────────────────██░░██─██░░██─────────██░░██──██░░██─██░░██─────────██░░██────────────────██░░██─────██░░██──██░░██─██░░██─────────
─██░░██████████─██████████░░██─██░░██████████─██░░██──██░░██─██░░██─────────██░░██████████────────██░░██─────██░░██──██░░██─██░░██████████─
─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██──██░░██─██░░██─────────██░░░░░░░░░░██────────██░░██─────██░░██──██░░██─██░░░░░░░░░░██─
─██████████████─██████████████─██████████████─██████──██████─██████─────────██████████████────────██████─────██████──██████─██████████████─
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
───────────────────────────────────────────────────────────────────────────────────────────────────
─██████████████─████████████████───██████████─██████████████─██████████████─██████──────────██████─
─██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██████████──██░░██─
─██░░██████░░██─██░░████████░░██───████░░████─██░░██████████─██░░██████░░██─██░░░░░░░░░░██──██░░██─
─██░░██──██░░██─██░░██────██░░██─────██░░██───██░░██─────────██░░██──██░░██─██░░██████░░██──██░░██─
─██░░██████░░██─██░░████████░░██─────██░░██───██░░██████████─██░░██──██░░██─██░░██──██░░██──██░░██─
─██░░░░░░░░░░██─██░░░░░░░░░░░░██─────██░░██───██░░░░░░░░░░██─██░░██──██░░██─██░░██──██░░██──██░░██─
─██░░██████████─██░░██████░░████─────██░░██───██████████░░██─██░░██──██░░██─██░░██──██░░██──██░░██─
─██░░██─────────██░░██──██░░██───────██░░██───────────██░░██─██░░██──██░░██─██░░██──██░░██████░░██─
─██░░██─────────██░░██──██░░██████─████░░████─██████████░░██─██░░██████░░██─██░░██──██░░░░░░░░░░██─
─██░░██─────────██░░██──██░░░░░░██─██░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██──██████████░░██─
─██████─────────██████──██████████─██████████─██████████████─██████████████─██████──────────██████─
───────────────────────────────────────────────────────────────────────────────────────────────────

                                       """)

print("")
path1 = input("Je bent in de gevangenis, er liggen een vijl en een schep in je cel, wil je naar buiten graven, of de vijl gebruiken om te ontsnappen? (type \"v\" om de vijl te kiezen, en de \"s\" om de schep te kiezen: ").upper()
if path1 == "V":

    print("Je bent uit je cel gekomen!!!")
    path1 = input("Je ziet dat er twee bewakers aankomen, wat doe je? ga je de kast in, of sla je ze neer? \"k\" voor kast \"s\" voor slaan: ").upper()
    if path1 == "S":
        print("Je slaat de bewakers neer, en dan besef je je, dat er camera's hangen...")
        path1 = input('wat doe je?, pak je het geweer van de bewaker, en schiet de camera kapot ("G") OF probeer je naar de uitgang te rennen("R"): ').upper()
        if path1 == "G":
            print("")
            print("")
            print("Je pakt het geweer, en schiet de camera kapot.")
            print("")
            print("De schot heeft de aandacht van alle bewakers getrokken.")
            print("")
            print("Je probeert op een van de bewakers te schieten, maar de kogels zijn op.")
            print("")
            print("GAME OVER!!!")
        elif path1 == "R":
            print("")
            print("Je rent langs de bewakers in de kantine, maar je was niet snel genoeg.")
            print("De bewakers stoppen je terug in je cel.")
            print("GAME OVER!!!")
        else:
            print("")
            print("Je probeert de camera, de camera denkt dat je een staar wedstrijd wil doen...")
            print("")
            print("je wil winnen van de camera, maar de camera is er goed in.")
            print("")
            print("na 3 minuten staren, komen er bewakers binnen, en beginnen de camera aan te moedigen.")
            print("")
            print("na nog 4 minuten, knippert de camera, JE HEBT GEWONNEN!!!")
            print("")
            print("Je hebt de 'staarwedstrijd' ending gehaald!!!, maar je gaat gewoon terug je cel in...")
            print("")
            print("GAME OVER!!!")

    elif path1 == "K":
        print("")
        print("Je verstopt je in de kast, en de bewakers lopen langs je zonder je te zien.")
        print("")
        print("Je komt uit de kast en je hebt weer twee nieuwe keuzes.")
        print("")
        path1 = input("Ga je via de deur naar buiten('D'), of via het ventilatierooster('V').").upper()
        if path1 == "D":
            print("")
            print("Je gaat door de deur, en je realiseert je, dat je in de kantine bent beland.")
            print("")
            print("de bewakers houden daar altijd pauze rond deze tijd.")
            print("")
            print("je word gelijk opgepakt, en terug in je cel gestopt...")
            print("")
            print("GAME OVER!!!")
        elif path1 == "V":
            print("")
            print("Je gaat het rooster in, maar je merkt al snel dat het niet zo stevig is.")
            print("")
            print("voordat je je kan omdraaien, stort het helemaal in.")
            print("")
            print("je ziet ineens dat alle bewakers bewusteloos zijn door de klap, en je weet te ontsnappen!!!")
            print("")
            print("Gefeliciteerd!!!, je hebt de 'ventilatie' ending!!!")
        else:
            print(""" 
                                                                     ____
             | | | | |                                               |  |
             | |   | |               O  Je blijft staan en doet niks |  |
             | |   | |              <|>                              ====
            _|_|___|_|______________/|__________________________________
            ____________________________________________________________
            """)
            print("GAME OVER!!!")
            
    else:
        print("")
        print("Je begint te dansen, en zingen.")
        print("")
        print("de bewakers horen je, en beginnen te luisteren naar je zangkunsten.")
        print("")
        print("de bewakers beginnen kaartjes voor je optreden te verkopen!!!")
        print("")
        print("de bewakers vonden je optreden leuk, maar je gaat terug je cel in.")
        print("")
        print("GAME OVER!!!")

elif path1 == "S":

    print("")
    print("Je graaft naar beneden, je belandt in het riool.")
    path2 = input("Ga je naar links of naar rechts? \"L/R\": ").upper()
    if path2 == "L":
        
        path2 = input("Je komt een enge clown tegen vlucht je weg, of vraag je om hulp? \"vraag om hulp(H)\" \"Ren weg(R)\"").upper()
        if path2 == "H":

            print("Hij wijst je de weg naar buiten!!!")
            print("Gefeliciteerd, je hebt de 'clown' ending gehaald!!!")
        elif path2 == "R":

            print("Je rent weg...")
            print("na 2 weken in het riool, geef je op, en besluit een nieuw leven te starten in het riool.")
            print("Gefeliciteerd, je hebt de 'LEVEN IN HET RIOOL' ending.")
        else:

            print("Je staart de clown aan, en doet niks.")
            print("De clown word bang van je, en besluit je neer te slaan en terug te brengen naar je cel.")
            print("GAME OVER!!!")

    elif path2 == "R":
        print("Je gaat naar rechts, en het lijkt niet te eindigen.")
        print("na 3 dagen lopen, zie je de uitgang!!!")
        print("maar toen je naar buiten liep, stonden er een groep politiemannen je op te wachten, en die brachten je terug naar je cel.")
        print("GAME OVER!!!")

else:
    print("Je hebt een rekenmachine gevonden!!!")
    nmmr1 = int(input("Vul een nummer in "))
    nmmr2 = int(input("Vul een nummer in "))
    if nmmr1 > nmmr2:
        print(str(nmmr1)+" is groter dan "+ str(nmmr2))
    elif nmmr2 > nmmr1:
        print(int(nmmr2)+ " is groter dan "+ str(nmmr1))
    elif nmmr2 == 0 and nmm1 == 0:
        print("You devided 0 by 0, and you created a black hole.")
        print("GAME OVER!!!")
    elif nmmr2 >= 100000 or nmmr1 >= 100000:
        print("You overloaded the calculator, and it exploded.")
        print("GAME OVER")
    else:
        print("The numbers are equal")
    print("")
    nmmr3 = int(input("Fill in another number"))
    nmmr4 = int(input("Fill in another number"))   
    print("☟☜☹☹⚐ ☟⚐🕈 ✌☼☜ ✡⚐🕆")



