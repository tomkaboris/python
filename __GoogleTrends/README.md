# Google Trends Analyzer

Ova skripta preuzima podatke sa Google Trends-a za izabranu ključnu reč (keyword), poredeći poslednjih 24 meseca pretraga na području Srbije. Skripta iscrtava grafikon sa istorijskim nivoima interesovanja, prosečnim vrednostima i linijskom regresijom, kao i označava potencijalno "povoljne" vremenske periode za marketinške kampanje.

## Karakteristike

- **Preuzimanje i kombinovanje Google Trends podataka** za poslednjih 24 meseca.
- **Prikaz prosečnog interesovanja** za ključnu reč.
- **Obračun linearne regresije** kako bi se identifikovao trend rasta ili opadanja interesovanja.
- **Identifikacija "Smart Campaign Periods"** - perioda kada je interesovanje veće od prosečnog, ali ispod 90% maksimalne zabeležene vrednosti.
- **Vizuelizacija podataka** kroz grafikon sa jasno označenim trendovima.

## Preuslovi i Instalacija

### 1. Python verzija
Skripta zahteva **Python 3.7+**. Možete proveriti verziju Python-a pomoću sledeće komande:

```bash
python --version
```

### 2. Instalacija zavisnosti
Potrebne biblioteke možete instalirati pokretanjem sledeće komande:

```bash
pip install -r requirements.txt
```

Ako ne koristite `requirements.txt`, možete instalirati zavisnosti pojedinačno:

```bash
pip install pytrends pandas numpy matplotlib
```

## Pokretanje

1. **Klonirajte ili preuzmite** repozitorijum sa GitHub-a.
2. Otvorite terminal i pređite u direktorijum gde se nalazi skripta.
3. Pokrenite skriptu:

   ```bash
   python google_trends_analyzer.py
   ```

   ili ako koristite `python3` kao podrazumevani interpreter:

   ```bash
   python3 google_trends_analyzer.py
   ```

4. Unesite željenu ključnu reč kada skripta to zatraži:
   ```
   Enter the keyword to search for trends:
   ```
   Nakon unosa, skripta će obraditi podatke i prikazati grafikon sa trendovima.

## Analiza
Vrši se kombinovanjem podataka od prethodnog i trenutnog 12 mesecnog perioda.
```bash
combined_data = pd.concat([data_previous_12_months, data_last_12_months])
```
pd.concat spaja DataFrame-ove iz prethodnog i trenutnog 12-mesečnog perioda. Rezultat combined_data pokriva poslednjih 24 meseca (računato unazad od današnjeg datuma).
### Računanje prosečnog interesovanja:
```bash
average_interest = combined_data[keyword].mean()
print(f"Average interest level for '{keyword}': {average_interest:.2f}")
```
- mean() računa aritmetičku sredinu vrednosti interesovanja za dato ključno slovo u celom 24-mesečnom periodu.
- :.2f formatira broj na 2 decimale.
### Linijska (polinomna) regresija
```bash
coefficients = np.polyfit(x, y, 1)
linear_trend = np.polyval(coefficients, x)
```
- np.polyfit(x, y, 1) vrši fitovanje linearne funkcije (stepen 1, tj. y = a*x + b) na skupu podataka (x, y).
- coefficients je lista [a, b] gde je a nagib, a b presečna tačka sa Y-osom.
- np.polyval(coefficients, x) primenjuje dobijenu funkciju na sve tačke x da bi se dobio niz vrednosti koji prikazuje idealnu linearnu „trend liniju”.

## Primer Izlaza

Po završetku analize, skripta ispisuje prosečno interesovanje i prikazuje grafikon koji sadrži:
- Vrednosti interesovanja tokom vremena.
- Crvenu isprekidanu liniju (trend linija).
- Zelenu isprekidanu liniju (prosečno interesovanje).
- Obeležene "Smart Campaign Periods" u narandžastoj boji.

## Autor
Boris Tomka 


## Licence
Ovaj projekat objavljuje se pod [MIT licencom](https://opensource.org/licenses/MIT). Slobodno ga koristite, izmenite i delite prema uslovima licence.

