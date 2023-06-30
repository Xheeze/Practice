#!/usr/bin/python3

# Nearest stars to Earth
# star1 = 'Sol'
# star2 = 'Alpha Centauri'
# star3 = 'Barnard'
# star4 = 'Wolf 359'

# Replacing with list method
stars = [
    "Sol",
    "Alpha Centauri",
    "Barnard",
    "Wolf 359"]
print('''\nwe've found the stars:

Alpha Centauri....
Sol...............
Wolf 359.......... 
Barnard...........

\t........and the fourth nearest star is known as:''',stars[3],"........")

# Highest peak on each tectonic plate
# African = 'Kilimanjaro'
# Antarctic = 'Vinson'
# Australian = 'Puncak Jaya'
# Eurasian = 'Everest'
# North_American = 'Denali'
# Pacific = 'Mauna Kea'
# South_American = 'Aconcagua'

peaks = {
    "African" : 'Kilimanjaro',
    "Antarctic" : 'Vinson',
    "Australian" : 'Puncak Jaya',
    "Eurasian" : 'Everest',
    "North_American" : 'Denali',
    "Pacific" : 'Mauna Kea',
    "South_American" : "Aconcagua"
    }
print('''\namongst these peaks:

North America's most wanted DENALI.
Africa's KILIMANJARO...............
the Pacific MAUNA KEA    .......... 
EVEREST of Euraisa ................
the Antarctic VINSON  .............
South america's ACONCAGUA .........
       &
the PUNCAK JAYA of Australasia.....
\n        the Highest is:''',peaks["Eurasian"],"         ")