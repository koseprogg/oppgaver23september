# Oppgaver til Koseprogg 23. september

## Kodeutfordringer
Her er noen kodeutfordringer der dere skal lage en funksjon som gjør noe spesifikt.

- [toSum](tosum.md)

Om dere synes oppgavene er litt for enkle, kan dere prøve en av bonusutfordringene:

### Hold det på én linje

Selv om Python vanligvis bruker whitespace i koden, går det an å gjøre mye forskjellig på én linje

Eks:

```python
def tellTil(tall):
    for i in range(1, tall+1):
        print(i)
```
kan skrives som
```python
tellTil = lambda tall: [print(i) for i in range(1, tall+1)]
```
yikes!

### Dropp while og for, embrace rekursjon

En mulig løsning av `tellTil(tall)` uten while og for kunne vært

```python
def tellTil(tall):
    if tall > 0:
        tellTil(tall-1)
        print(tall)
```


## Tegn og behandle bilder
Du kan tegne og behandle bilder med [Pillow-pakken til Python](https://pillow.readthedocs.io/en/stable/#)

For å installere det trenger du python lokalt. Når du har det kan du gå til [installerinssiden til Pillow](https://pillow.readthedocs.io/en/stable/installation.html)

- [Gjør et gråverdibilde til svart-hvitt med dithering](dithering/dithering.md)
