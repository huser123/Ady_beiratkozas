# Ady_beiratkozas

Az Adysuliba történő beiratkozási adatlapokat kigeneráló fájl

1. Az alap adatokat táblázatkezelő formátumban kell bekérni
2. Az adatokat át kell konvertálni JSON formátumra
2.1 Ehhez jön jól a Google Drive-on található JSON converter
3. A JSON-t hozzá kell adni a mappához a megfelelő formátumban
3.1 A JSON-ban tömbként kell menteni az adatokat
4. A Python fájl segítségével kigenerálni a LaTeX fájlt
5. A script Linux rendszerekkel kompatibilis (tesztvelve: Fedora 37.)
