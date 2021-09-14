#99067718
#Emiel 't Lam


invoer = input("Is de kaas geel? y/n: ").upper()


if invoer == "Y":
    
    invoer = input("zitten er gaten in? y/n: ").upper()

    if invoer == "Y":

        invoer = input("Is de kaas belachelijk duur? y/n:  ").upper()
        if invoer == "Y":

            print("De kaas die je in gedachten hebt is: Emmenthaler")
        else:

            print("De kaas die je in gedachten hebt is: Leerdammer")
    else:

        invoer = input("Is de kaas hard als steen? y/n: ").upper()
        if invoer == "Y":

            print("De kaas die je in gedachten hebt is: Pamniago Reggiano")
        else:

            print("De kaas die je in gedachten hebt is: Goudse kaas")
else:
    invoer = input("Heeft de kaas blauwe schimmels? y/n: ").upper()
    if invoer == "Y":
        
        invoer = ("Heeft de kaas een korst? y/n: ").upper()
        if invoer == "Y":

            print("De kaas die je in gedachten hebt is: Bleu de Rochbaron")
        else:

            print("De kaas die je in gedachten hebt is: Foumme d'Ambert")
    else:
        
        invoer = input("Heeft de kaas een korst? y/n: ").upper()
        if invoer == "Y":

            print("De kaas die je in gedachten hebt is: camembert")
        else:

            print("De kaas die je in gedachten hebt is: Mozzerella")
