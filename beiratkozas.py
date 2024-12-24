#!/bin/python3

# Modulok importálása

import json
import codecs
import os

# JSON fájl megnyitása
f = open('data.json')
w = open("adatlapok.tex","w")
  
# A JSON fájl visszahívása dictionary-ként
data = json.load(codecs.open('data.json', 'r', 'utf-8-sig'))
  
# A LaTeX fejléc és dokumentumkezdés kiírása

w.write("""
    \\documentclass[10pt,a4paper]{article}
    \\usepackage[utf8]{inputenc}
    \\usepackage[magyar]{babel}
    \\usepackage[T1]{fontenc}
    \\usepackage{amsmath}
    \\usepackage{amsfonts}
    \\usepackage{amssymb}
    \\usepackage[left=1cm,right=1.5cm,top=1cm,bottom=1cm]{geometry}
    \\usepackage{tabularx}


    \\pagestyle{empty}

    \\begin{document}
""")

# A JSON fájl feldolozása listaként

for i in data['Munkalap1']:

    # fuggosegi vizsgalatok és a valtozok letrehozasa

    if "apa_nev" in i:
        apa_nev = i["apa_nev"]
    else:
        apa_nev = " "

    if "apa_email" in i:
        apa_email = i["apa_email"]
    else:
        apa_email = " "
    
    if "apa_tel" in i:
        apa_tel = i["apa_tel"]
    else:
        apa_tel = " "

    if "apa_cim" in i:
        apa_cim = i["apa_cim"]
    else:
        apa_cim = " "

    if "anya_nev" in i:
        anya_nev = i["anya_nev"]
    else:
        anya_nev = " "

    if "anya_email" in i:
        anya_email = i["anya_email"]
    else:
        anya_email = " "

    if "anya_tel" in i:
        anya_tel = i["anya_tel"]
    else:
        anya_tel = " "

    if "anya_cim" in i:
        anya_cim = i["anya_cim"]
    else:
        anya_cim = " "

    if "etkezes" in i:
        etkezes = i["etkezes"]
    else:
        etkezes = " "

    if "allergia" in i:
        allergia = i["allergia"]
    else:
        allergia = " "

    if "posta" in i:
        posta = i["posta"]
    else:
        posta = " "

    if "komment" in i:
        komment = i["komment"]
    else:
        komment = " "

    # Az elkeszult adatok kiirasa a képernyőre

    print(i['tanulo_neve'])
    print(i['tanulo_szuletes'])
    print(i['tanulo_szuletesiszam'])
    print(i['tanulo_lakhely'])
    print(i['allampolgarsag'])
    print(i['tanulo_nemzetiseg'])
    print(apa_nev)
    print(apa_email)
    print(apa_tel)
    print(apa_cim)
    print(anya_nev)
    print(anya_email)
    print(anya_tel)
    print(anya_cim)
    print(i['ovi'])
    print(i['osztaly'])
    print(i['tantargy'])
    print(i['napkozi'])
    print(etkezes)
    print(allergia)
    print(i['egyhaz'])
    print(i['kapcsolat'])
    print(i['kapcsolat_tel'])
    print(i['kapcsolat_mail'])
    print(posta)
    print(komment)
    print("IGEN")
    print("")

    # Az adatok kiírása a LaTeX fájlba

    w.write("""
    \\begin{figure}[!ht]
    \\begin{tabular}{|m{\\textwidth}|}
    \\hline \\vspace{3pt}
    """)
    w.write("\\textbf{A tanuló neve:} \\hspace{0.5cm} "+i['tanulo_neve']+" \\vspace{3pt} \\\\"+"\n")
    w.write("\\hline\\vspace{3pt}"+"\n")
    w.write("\\textbf{A tanuló születési helye és dátuma:} \\hspace{0.5cm} "+i['tanulo_szuletes']+" \\vspace{3pt} \\\\"+"\n")
    w.write("\\hline\\vspace{3pt}"+"\n")
    w.write("\\textbf{A tanuló születési száma:} \\hspace{0.5cm} "+i['tanulo_szuletesiszam']+" \\vspace{3pt} \\\\"+"\n")
    w.write("\\hline\\vspace{3pt}"+"\n")
    w.write("\\textbf{A tanuló állandó lakhelye:} \\hspace{0.5cm} "+i['tanulo_lakhely']+" \\vspace{3pt} \\\\"+"\n")
    w.write("\\hline\\vspace{3pt}"+"\n")
    w.write("\\textbf{A tanuló állampolgársága:} \\hspace{0.5cm} "+i['allampolgarsag']+" \\vspace{3pt} \\\\"+"\n")
    w.write("\\hline\\vspace{3pt}"+"\n")
    w.write("\\textbf{A tanuló nemzetisége:} \\hspace{0.5cm} "+i['tanulo_nemzetiseg']+" \\vspace{3pt} \\\\"+"\n")
    w.write("\\hline\\vspace{3pt}"+"\n")
    w.write("\\textbf{Az apa neve:} \\hspace{0.5cm} "+apa_nev+" \\vspace{3pt} \\\\"+"\n")
    w.write("\\hline\\vspace{3pt}"+"\n")
    w.write("\\textbf{Az apa e-mail címe:} \\hspace{0.5cm} "+apa_email+" \\vspace{3pt} \\\\"+"\n")
    w.write("\\hline\\vspace{3pt}"+"\n")
    w.write("\\textbf{Az apa telefonszáma:} \\hspace{0.5cm} "+apa_tel+" \\vspace{3pt} \\\\"+"\n")
    w.write("\\hline\\vspace{3pt}"+"\n")
    w.write("\\textbf{Az apa állandó lakhelye:} \\hspace{0.5cm} "+apa_cim+" \\vspace{3pt} \\\\"+"\n")
    w.write("\\hline\\vspace{3pt}"+"\n")
    w.write("\\textbf{Az anya neve:} \\hspace{0.5cm} "+anya_nev+" \\vspace{3pt} \\\\"+"\n")
    w.write("\\hline\\vspace{3pt}"+"\n")
    w.write("\\textbf{Az anya e-mail címe:} \\hspace{0.5cm} "+anya_email+" \\vspace{3pt} \\\\"+"\n")
    w.write("\\hline\\vspace{3pt}"+"\n")
    w.write("\\textbf{Az anya telefonszáma:} \\hspace{0.5cm} "+anya_tel+" \\vspace{3pt} \\\\"+"\n")
    w.write("\\hline\\vspace{3pt}"+"\n")
    w.write("\\textbf{Az anya állandó lakhelye:} \\hspace{0.5cm} "+anya_cim+" \\vspace{3pt} \\\\"+"\n")
    w.write("\\hline\\vspace{3pt}"+"\n")
    w.write("\\textbf{Melyik óvodába járt a gyermek:} \\hspace{0.5cm} "+i['ovi']+" \\vspace{3pt} \\\\"+"\n")
    w.write("\\hline\\vspace{3pt}"+"\n")
    w.write("\\textbf{Milyen jellegű osztályt választana (több lehetőség is választható):} \\hspace{0.5cm} "+i['osztaly']+" \\vspace{3pt} \\\\"+"\n")
    w.write("\\hline\\vspace{3pt}"+"\n")
    w.write("\\textbf{Választható tantárgy:} \\hspace{0.5cm} "+i['tantargy']+" \\vspace{3pt} \\\\"+"\n")
    w.write("\\hline\\vspace{3pt}"+"\n")
    w.write("\\textbf{Napköziotthon:} \\hspace{0.5cm} "+i['napkozi']+" \\vspace{3pt} \\\\"+"\n")
    w.write("\\hline\\vspace{3pt}"+"\n")
    w.write("\\textbf{Iskolai étkeztetésre igényt tart:} \\hspace{0.5cm} "+etkezes+" \\vspace{3pt} \\\\"+"\n")
    w.write("\\hline\\vspace{3pt}"+"\n")
    w.write("\\textbf{Van a gyermekének allergiája, vagy más betegsége, melyről az iskolálak tudnia kell?:} \\\\ \\hspace{0.5cm} "+allergia+" \\vspace{3pt} \\\\"+"\n")
    w.write("\\hline\\vspace{3pt}"+"\n")
    w.write("\\textbf{A szülők egy háztartásban élnek? } \\hspace{0.5cm} "+i['egyhaz']+" \\vspace{3pt} \\\\"+"\n")
    w.write("\\hline\\vspace{3pt}"+"\n")
    w.write("\\textbf{Elsődleges kapcsolattartási személy vezetékneve és keresztneve (kit kereshetünk iskolai ügyekben):} \\\\ \\hspace{0.5cm} "+i['kapcsolat']+" \\vspace{3pt} \\\\"+"\n")
    w.write("\\hline\\vspace{3pt}"+"\n")
    w.write("\\textbf{Elsődleges kapcsolattartási telefonszám (kit kereshetünk iskolai ügyekben):} \\\\ \\hspace{0.5cm} "+i['kapcsolat_tel']+" \\vspace{3pt} \\\\"+"\n")
    w.write("\\hline\\vspace{3pt}"+"\n")
    w.write("\\textbf{Elsődleges kapcsolattartási e-mail cím (kit kereshetünk iskolai ügyekben):} \\\\ \\hspace{0.5cm} "+i['kapcsolat_mail']+" \\vspace{3pt} \\\\"+"\n")
    w.write("\\hline\\vspace{3pt}"+"\n")
    w.write("\\textbf{Az iskolalátogatásról szóló határozatot, illetve más levelezést az iskola kinek a nevére címezheti?:} \\\\ \\hspace{0.5cm} "+posta+" \\vspace{3pt} \\\\"+"\n")
    w.write("\\hline\\vspace{3pt}"+"\n")
    w.write("\\textbf{Bármilyen egyéb megjegyzés, amiről esetleg tudnunk kellene:} \\\\ \\hspace{0.5cm} "+komment+" \\vspace{3pt} \\\\"+"\n")
    w.write("""
    \\hline \\vspace{3pt}
    A Szlovák Köztársaság Nemzeti Tanácsának 18/2018-as, a személyes adatok védelméről szóló törvénye alapján hozzájárulok, hogy az iskola, mint adatkezelő (név: Ady Endre Alapiskola, statisztikai számjel: 36110744, cím: Ady utca 9, Párkány, 94301), az elektronikus nyomtatványon megadott személyes adatokat gyűjtheti és feldolgozhatja a felvételi eljárással és az iskolalátogatással kapcsolatban.  \\\\
    \\textbf{V zmysle zákona NR SR č. 18/2018 Z. z. o ochrane osobných údajov udeľujem súhlas škole ako spravovateľovi (Základná škola Endre Adyho s vyučovacím jazykom maďarským, IČO: 36110744 adresa: Adyho 9, 94301, Štúrovo), so zberom a spracovaním poskytnutých osobných údajov uvedených v tejto elektronickej prihláške a to za účelom evidencie prihlásených žiakov v súvisloti s prijímacím konaním a školskou dochádzkou žiaka.} \\vspace{3pt} \\\\
    \\hline \\vspace{3pt}
    \\textbf{Elfogadom:} \\hspace{0.5cm} IGEN \\vspace{3pt} \\\\
    \\hline 
    \\end{tabular} 
    \\end{figure}

    \\vfill
    \\textbf{BSz: }"""+i['sorszam']+"\n")

    w.write("\\newpage")

# A LaTeX fájl láblece

w.write("\\end{document}>")

# A fájlok zárása

f.close()
w.close()

# A Linux környezeti parancsok létrehozása és végrehajtása (a LaTeX lefordításához és a segédfájlok törléséhez)

fordit = 'pdflatex *.tex'
torles = 'rm -rf *.aux && rm -rf *.log && rm -rf *.dvi'

os.system(fordit)
os.system(fordit)
os.system(torles)

