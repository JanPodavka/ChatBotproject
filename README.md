# ChatBox DSP - softwarové inženýrství

## Úvod

Aplikace bude sloužit ke komunikaci s tzv. Chatbotem skrze webovou aplikaci.

## Pojmy
- Chatbot: program určený k automatizované komunikaci s lidmi. Tato implementace obsahuje již předdefinovanou řadu dotazů a odpovědí na ně
- SEČ: Středoevropský čas
- ČNB: Česká národní banka

## Popis funkcí

### Znázornění Use case diagramu

<img src="https://github.com/JanPodavka/ChatBotproject/blob/master/data/ucd.jpg">

### Slovní popis funkcí
- Dotaz na čas: zobrazí se aktuální SEČ
- Dotaz na kurz: zobrazí se aktuální měnový kurz dle ČNB
- Dotaz na jméno: zobrazí se jméno chatbota

## Vstupní data
- Uživatel ve formě dotazu
- ČNB: data o aktuálním kurzu získané z webové stránky https://www.api.store/cnb.cz/?msclkid=64c36be8be9011ecbf7ee9e40c4499bd
- Aktuální systémový čas

## Výstupní data

- Standartní výstup webové aplikace

## Uživatelské požadavky

 Chatbot bude umět odpovídat na následující dotazy v níže specifikovaném formátu:
 
 - "Jaký je čas?"
 - "Jak se jmenuješ?"
 - "Aktuální kurz EUR vůči CZK?"

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

### Omezení ze strany serveru:

- 2,000 CPU vteřin
- Maximální počet dotazů: 100 000 hit/den
- 1GB místa na disku

### Chybové stavy

 - Odpojení od internetu:
   - V průběhu: dojde ke smazání historie s chatbotem
   - Při startu programu: uživatel bude upozorněn na připojení k síti
 - Resetování stránky: dojde ke smazání historie s chatbotem
 - Dotaz mimo specifikaci: uživatel bude botem vyvzván k opravě dotazu
 - Kurz během víkendu a svátků: uživatel dostane informaci o kurzu, který byl posledný aktulizovaný
 - Výpadek serveru ČNB nebo změna formátu kurzu: nezobrazí se aktuální kurz



# DSP rozšíření

Rozšiřujicí DSP popisující nové funkcionality dle domluvy.

### Slovní popis funkcí
- Dotaz na historii kurzu: zobrazí se kurz eura za posledních 14 dní
- Dotaz na doporučení eura: zobrazí se, zda je aktuálně výhodný nákup eura, včetně zdůvodnění

## Uživatelské požadavky

 Chatbot bude umět odpovídat na následující dotazy v níže specifikovaném formátu:
 
 - "jaka je historie kurzu eura?"
 - "doporucujes mi euro?"

Dále uvádíme, že maximální odchylka od takto specifikovaných vyhledávaných termínů jsou maximálně dva znaky.

## Doporučení eura

Doporučení eura je rozhodnuta dle následujících faktorů:

Kurz je doporučen v případě že:

- Kurz eura je klesající v průběhu posledních 3 dnů (posledních 3, tedy mimo dnešního dne)
- Kurz eura nestoupl o více než 10% z průměru za poslední 3 dny

Kurz není doporučen v případě, že nejsou splněny předchozí podmínky

## Výstupní formát nové funkcionality

- Ano, kurz eura je dnes doporucen \  Ne, kurz eura neni dnes doporucovan
- Dnesni kurz: "aktuální kurz" CZE/EUR 
- Prumer za posledni tři dny: "průměr" CZE/EUR
- Kurz vzrostl za posledni tri dny o "o kolik" \ Kurz klesl za posledni tri dny o "o kolik" ("o kolik" se rozumí rozdíl mezi 1. a 3. dnem)
- Kurz posledni tri dny pouze klesá \ Kurz posledni tri dny je nestabilni (pouze neklesá)

Pokud se průměr nezvýšil o více než 10 % z průměru za poslední 3 dny:

- Kurz se nezvysil o více nez 10 procent z prumeru poslednich tri dni
- Kurz by se nedal doporucit pokud by vzrostl o %.3f na %.3f CZE/EUR

Pokud se průměr zvýšil o více než 10 % z průměru za poslední 3 dny:

- Kurz se zvysil o více nez 10 procent z prumeru za posledni tri dny
- Kurz by se dal doporucit pokud by klesl o "o kolik" na "hranice doporučelnosti z průměru"


## Use case diagram rozšíření

<img src="https://github.com/JanPodavka/ChatBotproject/blob/master/data/chatbot_diagram_enchanted.jpg">
