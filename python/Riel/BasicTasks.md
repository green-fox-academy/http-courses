# Bevezető feladatok a Python nyelv elsajátításához

## Változók és operátorok


__Bemutatkozás:__

Mutasd be magad változók segítségével! Hozz létre három változót egyet a nevednek, egyet a korodnak és egyet a kedvenc gyümölcsödnek.
Írd ki a konzolra a következőket a változók használatával:

```
Sziasztok, Béla vagyok 40 éves!
A kedvenc gyümölcsöm a dinnye.
```

__Két szám:__

- Készíts egy programot, ami kinyomtatja két számom végzett néhány művelet eredményét (22 és 13)
- Nyomtasd ki a két szám összegét
- Nyomtasd ki a két szám különbségét
- Nyomtasd ki a két szám szorzatát
- Nyomtasd ki a két szám hányadosát (22 osztva 13-a, tört formátumban)
- Nyomtasd ki a két szám hányadosát (22 osztva 13-a, egész szám formátumban)
- Nyomtasd ki a két szám osztásából eredő maradékot

__Csere:__

- Cseréld fel az a és b változók értékét:

```
a = 123
b = 526
print(a)
print(b)
```

__Átlag:__

- Kérj két számot a felhasználótól (az `input()` metódus segítségével)
- Nyomtasd ki a két szám összegét majd átlagát

<br>

## Elágazások

__Páros vagy páratlan:__

- Kérj egy számot a felhasználótól (az `input()` metódus segítségével)
- Nyomtasd ki azt, hogy `"Páros"`, ha a megadott szám páros, vagy azt, hogy `"Páratlan"`, ha a szám páratlan

__Egy, kettő, sok:__

- Készíts egy programot, ami bekér egy számot a felhasználótól
- Ha a szám kisebb, vagy egyenlő 0-val, nyomtasd ki azt, hogy `"Nem elég"`
- Ha a szám 1, nyomtasd ki: `"Egy"`
- Ha a szám 2, nyomtasd ki: `"Kettő"`
- Ha a szám több 2-nél, nyomtasd ki: `"Sok"`

<br>

## Szövegek, karakterláncok

__Szócsere:__

- Van egy string típusú változónk az alábbi tartalommal: `"In a dishwasher far far away"`
- Módosítsd majd nyomtasd ki ennek a szövegét, a string típus beépített metódusát használva: `"In a galaxy far far away"`
- Nyomtasd ki a szöveg hosszát
- Nyomtasd ki a szöveg első karakterét
- Nyomtasd ki, hány szóból áll a szöveg (Lista használattal)
- Nyomtasd ki az utolsó előtti szót (Lista használattal)

<br>

## Ciklusok

__Számolás:__

- Készíts egy programot, ami bekér 2 számot a felhasználótól
- Ha a második szám kisebb, mint az első, nyomtasd ki: `"A másodiknak nagyobbnak kell lennie!"`
- Ha a második szám nagyobb, nyomtass ki minden számot a két szám között

```
Példa:

Első szám: 3
Második szám: 6

A print eredméne:
3
4
5
6
````

__PiffPuff:__

Írd ki a konzolra a számokat 1-től 100-ig úgy, hogy ha a szám osztható 3-mal, akkor azt írod a szám helyett, hogy `"Piff"`, ha osztható 7-tel, akkor azt, hogy `"Puff"`, ha mindkettővel, akkor pedig azt, hogy `"PiffPuff"`.

__Karakter lista:__

- Nyomtasd ki az alábbi `szoveg` változó minden egyes karakterét, az alábbi formátumban:

```
szoveg="Kutyuli"

Eredmény:
1. K
2. u
3. t
4. y
5. u
6. l
7. i
```

- Nyomtasd ki ugyanezt fordított sorrendben

__Háromszög:__

- Készíts egy programot, ami bekér 1 számot a felhasználótól, majd egy ilyen háromszöget rajzol. A háromszögnek annyi sora legyen, amennyi a felhasználó által megadott szám.

```
*
**
***
****
```

__Piramis (nehezebb):__

Hozz létre egy változót `sorokSzama` néven, amit tölts fel értékkel, pl. `4`. Készíts programot, amely ezt rajzolja ki a konzolra, úgy hogy pont annyi sor legyen, amennyi épp a változó értéke:

```
    *
   ***
  *****
 *******
```

<br>

## Lista

__Lista bevezető:__

- Hozz létre egy listát `a` néven, a következő tartalommal:

`Apple, Avocado, Blueberries, Durian, Lychee`

- Hozz létre egy `b` listát, aminek az értékei azonosak az `a` lista értékeivel
- Nomytasd ki, hogy az `a` lista tartalmazza-e a `Durian` elemet
- Távolítsd el a `Durian` elemet a listából
- Add hozzá a `Kiwifruit` elemet az `a` listához, a 4. elem után
- Hasonlítsd össze a 2 lista méretét
- Nyomtasd ki az `Avocado` elem indexét az `a` listában
- Nyomtasd ki a `Durian` elem indexét a `b` listában
- Add hozzá a `Passion Fruit` és `Pomelo` elemeket a `b` listához, egyetlen parancs segítségével
- Nyomtasd ki az `a` lista 3. elemét

<br>

### Tuple

__Harmadik:__

- Készíts egy tuple változót a következő tartalommal: `(4, 5, 6, 7)`
- Nyomtasd ki a harmadik elemét

__Összeg:__

- Készíts egy tuple változót a következő tartalommal: `(54, 23, 66, 12, 66)`
- Nyomtasd ki az első és a harmadik elem összegét
- Nyomtasd ki az összes elem összegét
- Nyomtasd ki, hányszor fordul elő a 66-os szám

__Duplázó:__

- Készíts egy tuple változót a következő tartalommal: `(3, 4, 5, 6, 7)`
- Duplázz meg minden elemet

__Fordító:__

- Készíts egy tuple változót a következő tartalommal: `(3, 4, 5, 6, 7)`
- Készíts egy új tuple-t, ami ugyan ezeket az elemeket tartalmazza, csak fordított sorrendben

__Jó leszek:__
- Készíts egy tuple-t aminek a tartalma 27 db string ezzel a szöveggel: `"Jó leszek"`

<br>

## Szótár

__Telefonkönyv:__

Az ismerőseink telefonszámait egy szótárban fogjuk reprezentálni. 
A kulcsok (név) és az érzékek (szám) egyaránt szövegek lesznek.

- Hozz létre egy Dictionary-t az alábbi tartalommal:

  | Name (key)          | Phone number (value) |
  | :------------------ | :------------------- |
  | William A. Lathan   | 405-709-1865         |
  | John K. Miller      | 402-247-8568         |
  | Hortensia E. Foster | 606-481-6467         |
  | Amanda D. Newland   | 319-243-5613         |
  | Brooke P. Askew     | 307-687-2982         |

- Készíts egy alkalmazást, ami megoldja a következő feladatot:
  - Mi `John K. Miller` telefonszáma?
  - Kinek a telefonszáma a `307-687-2982`?
  - Tudjuk `Chris E. Myer` telefonszámát?

<br>

## Funkciók

__Duplázó:__

- Hozz létre egy integer típusú változót `base_num` néven és add hozzá a 123 értéket.
- Készíts egy funkciót, ami megkapja ezt a változót paraméterül, megduplázza azt, majd a megduplázott számot adja vissza
- Nyomtasd ki a visszakapott értéket

__A-t hozzáad:__

- Készíts egy string változót `typo` néven és add neki a `Chinchill` értéket
- Készíts egy funkciót, ami megkapja ezt a változót paraméterül, hozzáad egy `a` karakter a végéhez és visszaadja a módosított szöveget
- Módosítsd ezt a funkciót úgy, hogy kaphasson még egy szöveg változót, és azt adja hozzá az első paraméter értékéhez

__Karakter számláló:__

- Készíts egy funkciót, ami kap egy string változót és visszatér a legtöbbször előforduló karakter gyakoriságával
