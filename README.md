# ChatBox DSP - softwarové inženýrství

## Úvod

Aplikace bude sloužit ke komunikaci s tzv. Chatbotem.

## Pojmy
- Chatbot: program určený k automatizované komunikaci s lidmi. Tato implementace obsahuje již předdefinovanou řadu dotazů a odpovědí na ně
- SEČ: Středoevropský čas
- ČNB: Česká národní banka

## Popis funkcí

### Znázornění Use case diagramu

<img src="https://github.com/JanPodavka/ChatBotproject/blob/master/data/ucd.jpg">

### Slovní popis funkcí
- dotaz na čas: zobrazí se aktuální SEČ
- dotaz na kurz: zobrazí se aktuální měnový kurz dle ČNB
- dotaz na jméno: zobrazí se jméno chatbota

## Vstupní data
- uživatel ve formě dotazu
- ČNB: data o aktuálním kurzu získané z webové stránky https://www.api.store/cnb.cz/?msclkid=64c36be8be9011ecbf7ee9e40c4499bd
- aktuální systémový čas

## Výstupní data

- standartní výstup webové aplikace

## Uživatelské požadavky

 Chatbot bude umět odpovídat na následující dotazy v níže specifikovaném formátu:
 
 - "jaký je čas ?"
 - "jak se jmenuješ ?"
 - "aktuální kurz EUR vůči CZK ?"

## Specifikace systému
Od uživatele se předpokládají následující požadavky:

### Požadavky na systém uživatele:

- Operační systém: multiplatformní
- Připojení k internetu: povinné
- internetový prohlížeč : povinné

### Požadavky na systém programátora:

- Operační systém: MacOS, Linux, Windows
- Programovací jazyk: Python verze 3.9
- Framework pro webovou aplikaci: Flask


### Chybové stavy

 - Odpojení od internetu:
   - V průběhu: dojde ke smazání historie s chatbotem
   - Při startu programu: uživatel bude upozorněn na připojení k síti
 - Resetování stránky: dojde ke smazání historie s chatbotem
 - Dotaz mimo specifikaci: uživatel bude botem vyvzván k opravě dotazu
 - Kurz během víkendu a svátků: uživatel dostane informaci o kurzu, který byl posledný aktulizovaný
 - Výpadek serveru ČNB: nezobrazí se aktuální kurz
