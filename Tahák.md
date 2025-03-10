# Základní datové typy
**int**: celá čísla

**float**: desetinná čísla

**str**: text

**bool**: pravda (True), nepravda (False)

**list**: *seznam*

# Operátory

**Aritmetické**: +, -, *, /, // (celé dělení), % (zbytek), ** (mocnina)

**Porovnávací**: ==, <, >

**Logické:**: and, or, not

**Přiřazení**: =, +=, -=, *=, /=
# Podmínky
```python
x = 10
if x > 5:
    print("Větší než 5")
elif x == 5:
    print("Je to 5")
else:
    print("Menší než 5")
```

# Cykly
**for**: Pro iteraci přes seznamy, rozsahy, řetězce

**while**: Běží, dokud je podmínka pravdivá

```python
for i in range(5):
    print(i)

while x > 0:
    print(x)
    x -= 1 
```
# Funkce
```python
def soucet(a, b):
    return a + b

print(soucet(3, 4)) 
```
# Listy
```python
cisla = [1, 2, 3]
cisla.append(4) 
cisla.remove(2)  
cisla.sort()  
```
# Slovníky
```python
kuchar = {"jméno": "Pepik", "věk": 69}
print(kuchar["jméno"])  
print(kuchar.get("věk")) 
```