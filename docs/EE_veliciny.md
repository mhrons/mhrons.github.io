# Elektrotechnika pre stredné školy
Stránka **EE pre SŠ** je vo výstavbe a aktuálne slúži ako záznam mojich poznámok z teoretického výkladu predmetov týkajúcich sa elektrotechniky. Jedinou kompletnou je zatiaľ kapitola "Úvod a elektrické veličiny". Ostatné kapitoly plánujem postupne textovo aj graficky zeditovať (nahradiť scany), doplniť textovým výkladom a podľa potreby rozšírim aj obsahovú štruktúru.     

## Úvod
Asi nikto nepochybuje o tom, že teoretické vzdelanie je pre elektrotechnika užitočné a potrebné. Získať ho je však namáhavé a stojí to veľa času. Čas sú peniaze a tie sa dajú zarobiť ľahšie a rýchlejšie, ako učením sa. Štúdium je výzva na dlhú cestu, ktorá začína prácou bez zárobku, a to ešte i s neznámym cieľom. Cesta sa začína dlhým tmavým tunelom, ktorý vedie do sveta poznania. Je to skúška Vašej vytrvalosti a odolnosti. Svetlo zo vstupu tunela už zaniklo, ale vpredu je ešte stále tma. Zmietate sa v pochybnostiach, či by nebolo lepšie vrátiť sa. Ako dlho ešte bude trvať táto tmavá neistota? V najvyšší čas sa ďaleko pred Vami zjaví prvé svetlo: "Pochopil(a) som niečo dovtedy úplne nevídané, a to stálo za to! To svetlo ešte nie je na konci tunela, ale znamená, že ***všetko, čo ste raz pochopili, si už nemusíte viac detailne pamätať***. V pamäti Vám ostanú len základné princípy, s pomocou ktorých si všetky vzorce logicky odvodíte. Takto sa pred Vami otvorí nekonečný proces poznávania. Rovnako je to aj s tým svetlom v diaľke: Nikdy naň celkom nedosiahnete, ale dokým za ním pôjdete, bude stále silnieť. Pocit, že ste v úzkom tuneli, postupne zanikne. Zistíte, že ak zabočíte, stena tunela Vám ustúpi. Tunel sa zmení na Váš komfortný pracovný priestor a odteraz Vy určujete, kam povedie - že by k novému objavu? Postupne Vám Váš tunel dá viac energie, ako stačíte minúť. Okrem radosti z nového poznania získate aj sebaistotu a rovnováhu. A tá má aspoň takú cenu, ako získané vedomosti. Nech sa páči, vstúpte! Kto sa nezľakne a vydrží, ten neoľutuje.  

***Cieľom*** tohoto učebného textu je vysvetliť vybrané časti z teórie elektrických obvodov a ich praktické aplikácie tak, aby ich mohli ***pochopiť a samostatne logicky odvodiť*** žiaci stredných škôl. Základom analýzy elektrických obvodov je ***Ohmov a Kirchofove zákony***. Učebný text používa matematický aparát bez diferenciálneho počtu. (Toto pravidlo potvrdzujú výnimky v kapitolách [Indukčnosť a kapacita](https://mhrons.github.io/Reaktancia/) a [Operačné siete](https://mhrons.github.io/OZ_siete/).) Zvolený postup analýzy elektrických obvodov je v texte logicky jednoznačne odôvodnený a vysvetlený. Matematické úpravy rovníc sú komentované. V nevyhnutnom prípade možno text použiť aj pri samoštúdiu, ale z motivačného hľadiska nenahradí výklad učiteľa. Matematická analýza elektrických obvodov bez diferenciálneho počtu si vyžaduje osobitne presné textové formulácie vzťahov intenzitných a extenzívnych fyzikálnych veličín s vymedzením podmienok ich platnosti. Vždy je uvádzaný rozsah platnosti použitého matematického modelu. ***Zásada primeranosti*** si kladie za cieľ vytvoriť minimalizovaný, avšak technicky výstižný matematický model s dôrazom nezanedbať žiaden významný aspekt skúmaného objektu. Takýmto prístupom možno navrhovať technické zariadenia s dobrým komerčným potenciálom.   
***Hľadanie optimáleho kompromisu medzi zložitosťou a presnosťou fyzikálneho modelu je základnou pracovnou metódou dobrého inžiniera.***   

## Fyzikálne veličiny elektrotechniky
Fyzika modeluje prírodu matematickými prostriedkami a tie používajú premenné a konštanty, ktoré reprezentujú rôzne čísla. Fyzika povýšila matematické premenné na tzv. fyzikálne veličiny, ktoré popisujú prírodné objekty a ich stav dvoma údajmi:  

- reálnym číslom (niekedy komplexným - pozri fázor) vyjadrujúcim veľkosť, resp. kvantitatívnu mieru veličiny  
- fyzikálnou jednotkou vyjadrujúcou typ, resp. kvalitatívnu identitu veličiny.  

Oba údaje sú navzájom neodlúčiteľné, preto ich píšeme VŽDY SPOLOČNE a matematicky predstavujú súčin (veľkosť x jednotka). Fyzikálna jednotka často v sebe obsahuje aj tzv. násobiteľ veľkosti: Je to skratka gréckeho slova, znamenajúca dekadické číslo. Ak týmto číslom vynásobíme predchádzajúce reálne číslo, vyjadríme tak veľkosť veličiny v jej základnej fyzikálnej jednotke, napr. 5km = 5*1000m = 5000m. Takýmto skratkovým zápisom sa šetrí písanie zbytočne dlhých čísel, väčšinou pozostávajúcich z opakujúcich sa núl. V elektrotechnike sa používajú najmä tieto dekadické násobitele:

- p = piko = 10^-12^
- n = nano = 10^-9^
- µ = mikro = 10^-6^
- m = mili = 10^-3^
- k = kilo = 10^3^
- M = Mega = 10^6^
- G = Giga = 10^9^
- T = Tera = 10^12^

Fyzikálna veličina môže byť buď:

- základná, ktorej význam definujeme slovným popisom, alebo  
- odvodená fyzikálnym zákonom zo základných veličín. Príslušný fyzikálny zákon je popísaný matematickým vzorcom, ktorého premenné sú fyzikálne veličiny, prípadne konštanty. Napr. silu definuje Newtonov pohybový zákon ako súčin hmotnosti a zrýchlenia. Hmotnosť je základnou fyzikálnou veličinou a zrýchlenie možno odvodiť zo základných veličín dĺžka a čas.   

Matematické premenné považujeme za nadmnožinu fyzikálnych veličín. Abstraktná matematika pracuje s veličinami bez fyzikálneho rozmeru. (Vystačí si s holými číslami.) Príkladom takej matematickej veličiny je uhol v radiánoch: Bezrozmerné číslo, ktorého fyzikálny význam si dokážeme predstaviť po jeho vynásobení fyzikálnou konštantou 1m, čím dostaneme dĺžku oblúka na jednotkovej kružnici, prislúchajúceho danému uhlu. (Porovnaj si vzorec na výpočet obvodu kružnice s "kruhovým" uhlom 2π.) Na rozdiel od matematickej veličiny, fyzikálna sa vždy vyjadruje veľkosťou aj fyzikálnou jednotkou.  
Elektrické veličiny sú podmnožinou fyzikálnych a častým javom je, že veľkosť elektrickej veličiny sa mení v čase. To, či je veličina konštantná alebo nie, je užitočné na prvý pohľad vedieť, a preto:

- Časovo-premenné elektrické veličiny označujeme malým písmenom napr. napätie u, prípadne ako funkciu času u(t).  
- Konštantné elektrické veličiny sa na rozlíšenie od premenných označujú Veľkým Písmenom. (Napríklad parametre prvkov el. obvodu sú konštanty.) Vo výpočtoch ich kedykoľvek môžeme nahradiť ich číselnou hodnotou spolu s fyzikálnou jednotkou.  

Vizuálne rozlišovanie konštánt od časových premenných je rozhodne užitočné. Elektrotechnila však používa aj iné fyzikálne veličiny, ktorých značenie historicky pochádza z fyziky, a tá pravidlo veľkých a malých písmen nepozná. Prevzaté fyzikálne veličiny označujeme rovnako ako vo fyzike a takou veľkosťou písma, aby sme sa vyhli kolízii s inou veličinou (napr. konštantná frekvencia f versus sila F). Informáciu, či sa sila v priebehu času mení alebo nie, potom vložíme za názov premennej, napr: F(t) alebo F.

#### Skalár a vektor  
Niektoré fyzikálne veličiny vyjadrujú okrem veľkosti aj smer, ktorým sa veličina "uberá" v priestore (t.j. v pravoúhlej súradnicovej sústave 2D alebo 3D). Typickým príkladom je rýchlosť. Takáto veličina sa nazýva ***vektor*** a jeho matematický význam je ***posunutie z bodu A do bodu B*** v priestore. Veľkosť vektora je rovná vzdialenosti oboch bodov a jeho smer je daný priamkou prechádzajúcou cez oba body. Vektor možno bezo zmeny premiestniť kamkoľvek v priestore, ak rovnobežne zachováme jeho smer a nezmeníme jeho veľkosť. Takto môžeme východzí bod A umiestniť do počiatočného bodu 0 súradnej sústavy. Ak vektor zapíšeme pravoúhlymi súradnicami koncového bodu B, a priori predpokladáme, že začiatok posunutia je v bode 0. Veľkosť vektora vypočítame zo súradníc bodu B pomocou Pytagorovej vety. Ekvivalentne možno vektor zapísať pomocou uhla a veľkosti. V 3-D priestore na to potrebujeme 2 uhly: Θ (Theta) je uhol od osi x v rovine x-y a uhol Φ (Fí) je nad kolmým priemetom spojnice 0-B do roviny x-y.  
Jednorozmerné veličiny vyjadrujúce len veľkosť (napr. dĺžka, hmotnosť) nazývame ***skaláry***.   
Fyzikálnou jednotkou násobíme veľkosť veličiny. V prípade vektora môžeme fyz. jednotkou alternatívne vynásobiť buď jeho veľkost, alebo všetky jeho pravoúhle súradnice.  
**Praktická poznámka:** Výpočty so skalármi sú zjavne jednoduchšie, ako s vektormi. Počítaniu s vektormi sa preto podľa možnosti vyhýbame: Ak sa smer vektora - napr. rýchlosti - nemení v čase, súradnicovú sústavu môžeme zvoliť resp. natočiť tak, aby jedna z jej osí (napr. os x) bola rovnobežná so smerom rýchlosti. Potom má vektor rýchlosti iba jedinú nenulovú súradnicovú zložku (x) a s touto ďalej pracujeme ako so skalárom.

#### Fázor
V elektrodynamike sa často používajú harmonické časové signály reprezentované napätím u(t) alebo prúdom i(t). Takéto signály sa matematicky vyjadria goniometrickou funkciou cos alebo sin. Súčin uhlovej rýchlosti a času (ω\*t) tvorí vstupný argument goniometrickej funkcie. Často potrebujeme násobiť alebo deliť celý harmonický signál iným harmonickým signálom, a to je pomocou reálnej algebry obtiažne (súčin goniom. funkcií) až nemožné (ich podiel). Fázor je komplexnou funkciou zloženou z 2 goniom. funkcií so spoločným argumentom: Reálnou zložkou fázora je pôvodný harmonický signál, jeho imaginárnou zložkou je pôvodný signál fázovo posunutý o uhol -90° (v časovom zmysle imaginárny signál mešká za reálnym signálom). Dôvodom používania fázorov v elektrodynamike je fakt, že násobenie a delenie **komplexných** harmonických signálov je triviálne jednoduché.  
Osobitným prípadom fázora je podiel dvoch harmonických signálov rovnakej frekvencie. Tu sa jedná o komplexnú funkciu (len) uhlovej rýchlosti - napr. impedancia, admitancia, prenos dvojbrány.  
Matematicky je komplexné číslo príbuzné s dvojrozmerným vektorom: Obe majú zhodne definované operácie súčet, rozdiel, absolútna hodnota. Nzov fázor je odvodený z pojmu fázový vektor. V elektrických obvodoch je však fázor komplexnou reprezentáciou skalárnych veličín u(t), i(t), alebo ich podielu resp. súčinu. Preto v elektrických obvodoch považujeme fázor za skalár.  
<br>  
**Ďalej uvádzame fyzikálne veličiny**, ktoré súvisia s analýzou elektrických obvodov. Základné veličiny definujeme detailným vysvetlením a tie ostatné potom matematicky odvodíme zo základných. Názvy podkapitol jednotlivých veličín sú uvedené názvom veličiny a jej fyzikálnou jednotkou. Samostatné kapitoly sú venované elektrickým prvkom rezistor, kapacitor, induktor a tam sú vysvetlené aj ich elektrické parametre. "Neelektrické" fyzikálne veličiny vysvetľujeme len do takej hĺbky, aby sme mohli odvodiť elektrické veličiny od nich závislé. V prípadoch, keď úplné vysvetlenie neelektrickej veličiny presahuje rozsah tohoto textu, treba siahnuť po učebnici fyziky.   

### Dĺžka [m]
je základnou fyzikálnou veličinou. Bežne býva konštantná (nemení sa v čase). Dĺžka nemusí byť výhradne mierou lineárneho útvaru, ale môže vyjdrovať napríklad dĺžku vodiča zvinutého do cievky a pod.  

- jednotka: 1 meter = 1m (základná jednotka v sústave SI)  
- typ: vektor
- označenie: l, (skratka z lat. longitudo), ale aj s, r, a, b, c, d atď. malé písmená z fyziky

### Čas [s]
je základnou fyzikálnou veličinou.  

- jednotka: 1 sekunda = 1s (základná jednotka v sústave SI)  
- typ: skalár
- označenie premennej: t  (skratka z lat. tempus)
- konštantný čas: t~1~, t~2~,  a pod. (malé písmeno, lebo...pozri ďalej)  
- časový interval: Δt, T (napr. T = perióda harmonického signálu)  

***POZOR:*** Symbolmi t, T sa označuje aj teplota!  

### Rýchlosť [m/s]
je vektorová veličina odvodená z dĺžky a z času. Vyjadruje pohybový stav telesa, resp. intenzitu zmeny polohy telesa v priebehu času: Ak sa teleso pohybuje rovnomerným priamočiarym pohybom, potom v ľubovoľnom čase t stanovíme polohu telesa na priamke vzťahom s = v * t . Dĺžka s je vzdialenosť telesa od bodu, v ktorom sa nachádzalo v čase t=0 a konštanta v je jeho rýchlosť. Ak poznáme vzdialenosť Δs prejdenú telesom  za časový interval Δt, potom jeho priemernú rýchlosť počas tohoto intervalu vypočítame: v = Δs/Δt.  

- jednotka: 1m/s
- typ: vektor
- označenie: v  (skratka z lat. velocitas. Používame malé písmeno, V označuje objem. Premennú rýchlosť označujeme v(t).)

### Hmotnosť [kg]
je fundamentálnou mierou hmoty a fyzikálne vyjadruje mieru jej zotrvačnosti. Vysveľujú to 2 Newtonove pohybové zákony, ktoré dávajú do vzťahu hmotnosť a silu: Podľa zákona zotrvačnosti zotrvá hmotné teleso v pokoji alebo v rovnomernom priamočiarom pohybe práve vtedy, ak naň nepôsobí sila. Veľkosť hmoty meriame fyzikálnou veličinou hmotnosť.  

- jednotka: 1 kilogram = 1kg (základná jednotka v sústave SI je 1kg, a nie 1g)
- typ: skalár
- označenie veličiny: m (skratka z lat. moles, fyzika používa malé písmeno)

### Sila [N]
je vektorová veličina odvodená z hmotnosti, dĺžky a času. Newtonov pohybový zákon sily definuje silu F jej pôsobením na teleso hmotnosti m: Teleso mení rýchlosť svojho pohybu zrýchlením *a = F/m*, pričom *F* je veľkosť pôsobiacej sily na teleso, zrýchlenie *a = Δv/Δt* je zmena rýchlosti telesa *Δv* za časový interval *Δt*. Predpokladajme, že počas intervalu *Δt* je sila *F* konštantná. Potom hovoríme, že počas intervalu *Δt* je pohyb telesa rovnomerne zrýchlený.  

- odvodenie: *F = m\*a*
- jednotka: 1 Newton = 1N = 1kg\*m\*s^-2^
- typ: vektor
- označenie: *F* (z lat. fortis. Používame veľké písmeno, pretože f označuje frekvenciu.)

Podľa Newtonovho gravitačného zákona je tiažová sila *G* výsledkom vzájomného pôsobenia dvoch telies hmotností *m* a *M*, pričom veľkosť *G* je priamo úmerná súčinu hmotností *m\*M*. Znamená to, že *G* je priamo úmerná hmotnosti telesa *m* a teda existuje konštanta úmernosti (pomenujeme ju gravitačné zrýchlenie *g*) taká, že platí: *G = m\*g*. Aj keď my nepozorujeme, že by teleso hmotnosti *m* ležiace na zemi menilo svoju rýchlosť, pomocou gravitačného zákona sme dokázali, že jeho tiažová sila *G* je kompatibilná so zákonom sily, ktorý silu definuje matematicky.  
Elektrickú silu medzi 2 nábojmi q, Q (pozri ďalej) popisuje Coulombov zákon matematicky rovnako, ako gravitačný zákon popisuje príťažlivú silu telies m, M. Rozdiel oproti gravitácii je len v tom, že elektrická sila môže byť nielen príťažlivá, ale aj odpudivá. (Zatiaľ čo hmotnosť je vždy kladná, elektrický náboj nadobúda obe znamienka.) Vektor el. sily teda môže mať aj odpudivú orientáciu, resp. v skalárnom tvare má odpudivá sila záporné znamienko. Zhodnosť matematickej formulácie Coulombovho a gravitačného zákona dokazuje, že aj elektrická sila je kompatibilná s jej definíciou zákonom sily.   
Ďalej naznačíme, ako pomocou sily vzniká kruhový pohyb hmotného telesa. Pomocou sily si odvodíme prácu z nej následne elektrické napätie. Rýchlosť, sila a zrýchlenie sú vektorové veličiny (majú veľkosť aj smer) a preto existujú 2 rôzne prejavy sily pôsobiacej na hmotné teleso:  

1. Ak vektory sily aj rýchlosti telesa majú zhodný smer, teleso rovnomerne zrýchľuje (*a > 0*) alebo spomaľuje (*a < 0*) a jeho pohyb ostane priamočiary.
2. V prípade rôznobežných smerov oboch vektorov bude rýchlosť meniť svoj smer aj veľkosť.  

V prvom prípade teleso zotrvá v priamočiarom pohybe. Vektor sily nemení pohybovú trajektóriu telesa, môže však zmeniť jeho orientáciu v danom smere. Ak je v 2. prípade vektor sily kolmý na vektor rýchlosti, vtedy sila mení len smer rýchlosťi, nie veľkosť. Ak je smer sily ***vždy kolmý*** na vektor rýchlosti a veľkosť sily je pritom konštantná, takáto sila zmení pohyb telesa na kruhový a silu nazývyme dostredivou. Veľkosť rýchlosti telesa sa nemení (obvodová rýchlosť je konštantná) a smer rýchlosti sa mení "rovnomerne" vďaka "dostredivému zrýchleniu" konštantnej veľkosti vyplývajúcemu z dostredivej sily. Keďže dostredivá sila ovplyvňuje len tvar dráhy telesa (nie dĺžku), táto nevykonáva prácu, resp. nespotrebúva žiadnu energiu.  

### Frekvencia, uhlová rýchlosť [s^-1^]
Predstavme si rovnomerný pohyb bodu po kružnici, tzv. rovnomerný kruhový pohyb. Časový interval jednoho obehu bodu kružnicou sa nazýva perióda T. Počet obehov (cyklov) za jednotku času je frekvencia f, čiže platí T = 1/f. Uhlová rýchlosť je uhol prejdený sprievodičom pohybujúceho sa bodu po kružnici za jednotku času. Je teda intenzitou časovej zmeny uhla sprievodiča. Keďže uhol 1 cyklu je 2π radiánov a počet cyklov za 1 sekundu je frekvencia, uhol prejdený za 1s je súčinom týchto dvoch.  

- označenie frekvencie: f (z lat. frequentia)
- odvodenie frekvencie: f = 1/T
- jednotka frekvencie: 1 Hertz = 1Hz = 1s^-1^
- označenie uhlovej rýchlosti: ω (malé grécke písmeno omega)
- odvodenie uhlovej rýchlosti: ω = 2π\*f = 2π/T
- jednotka uhlovej rýchlosti: 1s^-1^
- typ oboch veličín: skalár

Názov Hertz bol jednotke frekvencie udelený na počesť nemeckého fyzika Heinricha Rudolfa Hertza, ktorý ako prvý experimentálne uskutočnil bezdrôtový prenos signálu rádiovými vlnami. Experimentálne potvrdil teóriu šírenia elektromagnetických vĺn - tzv. Maxwellove rovnice.

***Poznámka:*** Uhol je matematickou jednotkou a nemá fyzikálny rozmer, preto nefiguruje vo fyzikálnej jednotke. Napriek tomuto faktu pri uhlovej rýchlosti odporúčame pužívať jednotku ***rad/s*** kvôli riziku jej zámeny s frekvenciou. Frekvencia je počet cyklov za jednotku času, zatiaľ čo uhlová rýchlosť je počet radiánov za jednotku času. Tak cyklus aj radián majú význam uhla, ale vo fyzikálnej jednotke uhol nevidieť, pretože uhol nemá fyzikálny rozmer. Napriek tomu, že obe veličiny f, ω majú rovnakú fyzikálnu jednotku, majú rôzny kvantitatívny význam...

### Energia, práca [J]
Energia je schopnosť konať prácu. Jedna veličina sa môže recipročne meniť na druhú, teda práca dokáže akumulovať energiu. Ak konštantná sila F pôsobí na pohybujúce sa hmotné teleso v smere jeho pohybu (t.j. vektory sily a rýchlosti sú neustále rovnobežné), potom je vykonaná práca A rovná súčinu F\*s, kde s je vzdialenosť prejdená telesom. Práca je premena zdrojovej energie W na jej inú formu. Napríklad tepelná energia W, ktorá sa uvoľnila horením plynu, sa následne prácou A zmení na mechanickú energiu W~m~ a tepelnú energiu W~t~, pričom platí zákon zachovania energie: W = W~m~ + W~t~. Prácou nadobudnutá mechanická energia W~m~ môže byť buď kinetická, alebo potenciálna.  

- označenie energie: W (fyzika používa aj symbol E, ale v TE je E = intenzita elektrického poľa = sila akou pôsobí elektrické pole na náboj 1C - pozri Coulombov zákon)
- označenie práce: A
- odvodenie práce: A = F*s za predpokladu platnosti horeuvedených podmienok
- vzťah práce a energie: W = F\*s + W~t~ , pričom W~t~ je zostatková energia pracovnej premeny energie (najčastejšie je tepelná)
- jednotka: 1 Joule = 1J = kg\*m^2^\*s^-2^ (odvodená zo zákl. jednotiek v SI)
- typ: skalár 

James Prescott Joule bol anglický fyzik 19.storočia, zakladateľ termodynamiky.

### Elektrický náboj [C]
je fundamentálnou mierou elektriny.

- jednotka: 1 Coulomb = 1C (v sústave SI odvodená z prúdu a času: 1C = 1A \* 1s)  
- typ: skalár
- označenie: Q, q  

Elementárny náboj elektrónu Q~e~=-1,602x10^-19^C, náboj protónu Q~p~=1,602x10^-19^C. Fyzikálna jednotka je pomenovaná na počeť francúzskeho fyzika 18. storočia Charlesa-Augustina de Coulomba, autora fyzikálneho zákona o vzájomnom silovom pôsobení elektricky-nabitých telies.

### Elektrický prúd [A]
Aj keď jednotka prúdu je základnou v sústave fyzikálnych jednotiek SI, elektrický prúd je odvodený ako množstvo elektrického náboja pretekajúceho vodičom za jednotku času. Je to intenzita toku náboja vodičom.  

- označenie veličiny: I, i
- odvodenie: Pri konštantnej intenzite toku náboja je množstvo pretečeného náboja vodičom priamo úmerné časovému intervalu a intenzite toku, počas ktorého tok sledujeme. Ak za časový interval Δt pretiekol vodičom náboj ΔQ, potom hodnota prúdu je I = ΔQ/Δt.  
- jednotka: 1 Ampér = 1A (základná jednotka v sústave SI)  
- typ: skalár

Fyzikálna jednotka je pomenovaná na počesť francúzskeho fyzika 18. storočia André-Marie Ampére, zakladateľa teórie elektromagnetizmu. Ako prvý popísal silu pôsobiacu na pohybujúci sa náboj v magnetickom poli (Ampérov záklon).

### Elektrické napätie [V]
"Mechanické" veličiny sila, energia, práca sme uviedli preto, aby sme mohli definovať veličinu elektrické napätie. Predstavme si elektrický dvojpól ako "blackbox" s dvoma el. kontaktami (pólmi), každý s rozdielnym elektrickým nábojom. Je zrejmé, že medzi nabitými pólmi dvojpólu existuje nenulová elektrická sila. Napätie medzi pólmi je práca, resp. energia W

- potrebná na "dobitie" dvojpólu o náboj 1C, t.j. na prenesenie 1C vodivou cestou medzi jeho pólmi proti existujúcej elektrickej sile danej celkovým nábojom dvojpólu, alebo
- ktorú dvojpól vykoná resp. vydá "vybitím sa" o náboj 1C, ktorý prenesie vodivou cestou medzi pólmi vlastnou elektrickou silou vyplývajúcou z jeho celkového náboja.  

Elektrické napätie sa ekvivalentne definuje ako rozdiel potenciálov medzi 2 pólmi trojpólu, pričom potenciál každého z jeho pólov 1 a 2 je rovný práci potrebnej na prenesenie náboja 1C zo vzťažného (nultého) pólu do daného pólu.  

- označenie: U, u, v angl. dokumentácii V (skratka Voltage)
- odvodenie: Elektrický dvojpól si reálne možno predstaviť ako [kapacitor](https://mhrons.github.io/L_C_skok/#kapacita). Náboj 1C je pomerne veľký a dobitie bežnej kapacity o takýto náboj by významne zmenilo elektrickú silu medzi pólmi kapacitora. V takom prípade by sa práca vykonaná na prenesenie prvého elektrónu (náboj = 1e) výrazne líšila od práce potrebnej na prenesenie posledného elektrónu. Aby sme sa tomu vyhli, prenesieme iba tak malé množstvo náboja ΔQ << 1C, pri ktorom sa práca na prenesenie jednotlivých elektrónov  zmení iba zanedbateľne málo oproti svojej priemernej hodnote. Napätie U dvojpólu potom definujeme pomocou energie ΔW potrebnej na prenesenie "malého" náboja ΔQ takto: U = ΔW/ΔQ .
- jednotka:  1V = 1J/1C = kg\*m^2^\*A^-1^s^-3^ 
- typ: skalár

Elektrické napätie sa často (najmä v angl. textoch) označuje pojmom elektromotorická sila. Tento pojem si však nezamieňajme s elektrickou silou. Je tam podobnosť názvov, pretože medzi oboma veličinami existuje príčinná súvislosť: Tak napätie, ako aj elektrická sila medzi 2 pólmi sú priamo úmerné náboju dvojpólu.

### Elektrický výkon [W]
je množstvo práce vykonané elektrickým zdrojom za jednotku času, teda intenzita práce. Elementárna práca vykonaná zdrojom je rovná súčinu jeho napätia U a "vytečeného" elementárneho náboja ΔQ. (Elementárny náboj je tak malý, aby sme jeho vybitím len zanedbateľne málo pozmenili napätie kapacitora, alebo chemického článku.) Príslušný elektrický výkon P je potom daný súčinom napätia zdroja a elektrického prúdu, pretože prúd je intenzita toku náboja.

- označenie: P, p
- odvodenie: P = U \* I
- jednotka: 1 Watt = 1W = J/s = kg\*m^2^\*s^-3^
- typ: skalár

Jednotka výkonu je pomenovaná na počesť škótskeho vynálezcu a inžiniera Jamesa Watta - samouka 18. storočia, ktorý významne zdokonalil parný stroj. Okrem iného je vynálezcom odstredivého regulátora výkonu parného stroja. Odstredivý regulátor sa donedávna používal aj v benzínových spaľovacích motoroch.
