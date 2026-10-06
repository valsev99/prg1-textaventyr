# handlar på willis

def läs_int(prompt="Ange ett heltal: "):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Inte ett heltal. Försök igen.")


namn = (input("Hej vad heter du? ")).capitalize()
print ("Ok hej "+ namn +"  ")


bilval = läs_int("Du ska handla på Willis du ska välja vilken bil du ska åka med klicka 1 för din monster truck klicka 2 för din golfbil och klicka 3 för din JAS39Gripen. ")


if bilval == 1:
    print("" \
    "Du hoppar in i monstertrucken och kör över 34 personer på vägen för att dom var i vägen. ")
if bilval == 2:
    print("" \
    "Du går in i golfbilen men fassnar på en trotoarkant så då går hela vägen. ")
if bilval == 3:
    gripenjakt = läs_int("Du tar JAS39Gripen men du ser några ryska plan i luften klicka 1 om du vill sjuta ner dom klicka 2 iffal du vill undvika dom och vara tråkig. ")
    if gripenjakt == 1:
         print("Du kör mot dom ryska planen och spränger dom sedan kör du till Willis. ")
    if gripenjakt == 2:
         print("Du försöker undvika dom ryska planen men då så anfaller dom dig backifrån du blir smatrad i 1000 bitar och dit plan krasha du överlevde men då fick du gå till willis du skulle har sjutit ner dom. ")

val1afären = läs_int("Nu är du inne i Willis vad gör du först klicka 1 om du springer till ninjago legot det första du gör klicka 2 iffal du är tråkig och går och handlar riktig mat som potatis och grönsaker klicka 3 iffal du drar fram en bassuka och kräver alla pengar från kassörerna och alla där inne. ")

if val1afären == 1:
    print("" \
    "Du springer det snabbaste du kan till ninjago legot och tar allt ninjago lego och då börjar en 7åring gråta och såga till sin mamma att du är dum så du slår han och springer videre ")
    ninjagojakt = läs_int("Du springer ut ur Willis fast någon ringde polisen så du snor någons bil och börjar åka men sedan så ser du en massa polisbilar som blokerar vägen klicka 1 för att åka rakt in i dom och hoppas nått bra händer klicka 2 för att åka av bron och hoppas du är som mcmissil from blixten mcqueen klicka 3 för att dra fram en basuka och sjuta på polisbliarna och köra igenom. ")
    if ninjagojakt == 1:
        print("Du dog ")
    if ninjagojakt == 2:
        print("Du drunkna det här är inte bilar2 ")
    if ninjagojakt == 3:
        print("Du spränger bilarna och poliserna och du flyr hela vägen till Ninjago city där poliserna inte vågar åka till så du van! ")
if val1afären == 2:
    print("" \
    "Du är jättetråkig och går SUPER LÅNGSAMT till grönsakerna och du ingnorerar godiset och ninjagolegot och bara köper en massa äklig dålig mat som havregrynsgröt och selleri. ")
    tråkigt = läs_int("Du går ut ur affären och går på några blomor och spräker några basketbollar som några barn leker med när du kommer hem så ska du gå och sova eller läsa en tråkig bajs bok klicka 1 för att sova klicka 2 för att läsa den tråkiga bajsboken. ")
    if tråkigt == 1:
        print("Du går och läger dig och sover.")
    if tråkigt == 2:
        print("Du läser bajsboken och går och sover.")

if val1afären == 3:
    basukajakt = läs_int("Du drar fram en bassuka från din framficka och skricker NER NER JAG HAR EN BASSUKA GE MIG ALLA PENGAR ANDARS SÅ SKUTER JAG VAR INTE EN HJÄLTE alla ger dig dina pengar och du går ut ur afären och skjuter afären utanför ändå men då börjar polisen jaga dig så du tar någons bil och börjar åka det kommer en rad av polisbilar framfrör dig på en bro du kan inte köra förbi dom klicka 1 iffal du kör in i dom och hoppas för det bästa klicka 2 för att köra av bron och hoppas att din bil är som fin mcmissil klicka 3 för att göra sönder glasrutan på bilen och skjuta din bassuka. ")
    if basukajakt == 1:
        print("" \
        "Du dog ")
    if basukajakt == 2:
        print("" \
            "Du drunkna det här är inte bilar 2. ")
    if basukajakt == 3:
        print("" \
                "Du spränger bilarna och poliserna och du flyr hela vägen till kasakstan där poliserna inte våger åka till så du van! ")



