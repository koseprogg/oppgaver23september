# Tre på rad

Spillet går ut på å sette kryss (X) eller runding (O) tre ganger etter hverandre som danner en horisontal, vertikal eller diagonal linje bestående av gjentakende symboler i et grid bestående av 3x3 plasser.

## Oppsett

Spillets grid kan se slik ut i en python representasjon:

```
   |   |
 ---------
   |   |
 ---------
   |   | 
```

### Eksempel

Dersom X har gjort ett trekk og Y har gjort ett trekk kan spillets output være:

```
 X |   |
 ---------
   | O |
 ---------
   |   | 

X SIN TUR>
```

## Oppgave 1

Lag en python representasjon som printer griddet og kan sette X-er og O-er for å representerer spillere X og O.
For hvert trekk kan programmet godt outputte et nytt grid uten å ta høyde for tidligere grids produsert.

<details>
<summary>Tips</summary>
Tenk gjennom hvordan du burde representere et spill i datamodellen for å lettere støtte å gjøre oppgave 3.
</details>

### Oppgave 1 optional

Dersom du ønsker kan du bruke et tredjepartsbibliotek for å lage et GUI til spillerene, men det er også veldig respektabelt om du lager dette terminalbasert.

### Oppgave 1 optional b

Er du skikkelig ivrig kan du bruke terminal-verktøy for å "endre" outputten i terminalen i stedet for å printe nytt grid.

## Oppgave 2

Lag en funksjon som validerer staten av brettet og velger om et nytt trekk er gyldig eller ikke.

## Oppgave 3

Gjør spillet spillbart for 1v1 spill. Bruk input() for å ta inn posisjon man ønsker å sette sitt symbol på. Merk: Husk å validere at inputten er et gyldig trekk.
Bruk ([0, 2], [0, 2]) som representasjon av plassene man kan sette sitt symbol på, hvor (0, 0) representerer firkanten øverst til venstre, og (0, 2) representerer firkanten nederst til venstre.

## Oppgave 4

Lag en CPU som spiller spillet selv. Dette kan lett gjøres context-unaware, alstå at man tar inn spillets nåværende state og hvem som har neste trekk, for deretter å compute hva som er det mest optimale trekket.
Tips: Hvilke algoritmer kan du bruke her? Burde du eventuelt bruke Tensorflow for å bruke en datamodell noen allerede har trent, eller er problemet soppas enkelt at du lett kan beregene det?

## Oppgave 5

Utvid spillets gang for å støtte 1v1 spill, 1vCPU og CPUvCPU.

## Oppgave 6

Optimaliser CPU-en til å gå enda raskere. Er det noen metoder du kan bruke som gjør at du kan skippe masse computations?

<details>
<summary>Tips</summary>
A/B pruning.
</details>
