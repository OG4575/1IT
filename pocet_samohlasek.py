text = input("Zadej slovo: ").lower()
samohlasky = "aeiouáéíóúů"
pocet = 0
for znak in text:
    if znak in samohlasky:
        pocet += 1
print("Počet samohlásek:", pocet)
