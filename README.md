# Kjapp intro til linting og autoformatering

Når vi skriver og snakker er det mye lettere å få til god kommunikasjon hvis språket er godt og konsekvent.
På samme måte er det med programmering: Akkurat som vi har konvensjoner, normer og regler på norsk, har vi det
i programmeringsspråk.
[PEP8](https://www.python.org/dev/peps/pep-0008/) er en stilguide for Python. Her står det en del regler/konvensjoner om
ting som hvordan formatere lister, bruke operatorer, osv.

La oss si at alle skriver kode på den måten de synes er best selv. Mest sannsynlig vil det variere.
Noen kommenterer mye, noen ikke. Noen bruker ofte linjer mellom kodeblokker, noen ikke.
Jo større prosjekter, jo større sjanse er det da for at kodebasen blir veldig lite homogen.
Det blir fort slitsomt å sette seg inn i kode og vanskeligere å lese dersom man må bruke energi på å tenke på variasjon her.

**Kort fortalt er den beste grunnen til å bruke linting at man sparer tid i det lange løp!**

Noen argumenter for å bruke linting her: [How Python Linters Will Save Your Large Project](https://jeffknupp.com/blog/2016/12/09/how-python-linters-will-save-your-large-python-project/).

En del av PEP8-reglene får man beskjed om i PyCharm også.

## Flake8

Flake8 er en linter som håndhever PEP8. Dersom du kjører det på en fil vil du få en beskjed om hvilke regler du ikke følger.
Noen av disse er rent stilmessige, andre er faktisk kodelogikk, altså feil man har gjort. Eksempler (noen [herfra](http://flake8.pycqa.org/en/latest/user/error-codes.html)):

- line too long
- local variable `x` is assigned to but never used
- module imported but unused
- a break statement outside of a while or for loop
- redefinition of unused name from line N

### Installasjon

Installer på hele systemet, så sørg for å ikke være i en virtual environment. (Skriv `deactivate` i terminalen for å være sikker.)

```
pip install flake8
```
### Flake8 i terminalen

Du kan kjøre Flake8 på en fil eller en mappe, og få beskjed om alle brudd på pep8-standarden. Dette gjør du ved å skrive:

```
flake8 <path to file/folder>
```

Du kan overstyre pep8-standarden - enten ignorere regler eller endre default-verdiene (f.eks. maks lengde på en linje). Dette kan du gjøre ved å enten sende det inn som parameter i kommandoen eller lagre det i en config-fil. Hirarkiet som bestemmer hvilken verdi som blir satt er: 

1. Parameter i kommandoen 
2. Config-fil i prosjekt-mappen
3. Global config-fil

Config-filen må hete `.flake8` og vi foreslår følgende som standard: <TODO>


### Flake8 i PyCharm

Du kan også bruke PyCharm til å kjøre Flake8 på en fil eller en mappe: 

1. Installer Flake8 (se over)
2. Lokaliser Flake8: `which flake8`
3. Preferences -> Tools -> External Tools -> + (legg til) `+`
4. Fyll inn som her: ![Imgur](https://i.imgur.com/Y8YMDQb.png)
  > *Name*: `Flake8 - file` (én enkel fil) eller `Flake8 - folder` (én mappe)\
  > *Program*: _<resultatet fra steg 2>_\
  > *Arguments*: `--max-line-length 110 $FileDir$/$FileName$` (én enkel fil) eller `--max-line-length 110 $FileDir$` (én mappe)\
  > *Working directory*: `$ProjectFileDir$`
  
#### For å ta det i bruk
1. Høyeklikk på en fil eller mappe du vil kjøre Flake8 på
2. Velg External tools -> Flake 8 - file / Flake 8 - folder
3. Brudd på pep8 blir listet opp i terminalen


## Black

>[Black](https://github.com/ambv/black) is the uncompromising Python code formatter.

Black er et program som man kjører på kodefiler, og den bare endrer disse filene slik at formateringa følger visse regler.
De reglene den håndhever er et utvalg av reglene i PEP8. Du kan kjøre Black på en fil ved å gjøre `black file`.

>Black makes code review faster by producing the smallest diffs possible.

Ved å bruke Black konsekvent på et prosjekt vil man få små diffs (forskjellen som kommer opp i Git),
kun det som "faktisk" er endret vil dukke opp. Dersom man skal bruke Black må alle på prosjektet være enige om det, hvis ikke blir det kaos!

### Installasjon

På Mac, i terminalen: (Pass på å ikke være i et virtual environment, så skriv `deactivate` i terminalen for å være sikker.)

```
brew install python3
pip3 install black
```

Vet ikke hvordan det gjøres i Ubuntu - spør Ruben!

### Black i PyCharm

Merk at du må ha PyCharm Professional!

1. Installer Black (se over)
2. Preferences -> Tools -> File Watchers -> + (legg til) `<custom>`
3. Fyll inn som her: ![settings](https://i.imgur.com/UsuFDXm)

Dersom du har Linux må du nok endre `/usr/local/bin/black`. Bare skriv `which black` i terminalen og kopier den stien.

Nå vil Black kjøres på fila du jobber med når du lagrer!
