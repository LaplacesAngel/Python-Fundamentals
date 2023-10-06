# Nearest stars to Earth
star1 = 'Sol'
star2 = 'Alpha Centauri'
star3 = 'Barnard'
star4 = 'Wolf 359'

# Highest peak on each tectonic plate
African = 'Kilimanjaro'
Antarctic = 'Vinson'
Australian = 'Puncak Jaya'
Eurasian = 'Everest'
North_American = 'Denali'
Pacific = 'Mauna Kea'
South_American = 'Aconcagua'

stars = ['Sol', 'Alpha Centauri', 'Barnard', 'Wolf 359']
fourth_star = stars[3]

peaks = {'African': 'Kilimanjaro', 
         'Antarctic': 'Vinson', 
         'Australian': 'Puncak Jaya',
         'Eurasian' : 'Everest',
         'North_American' : 'Denali',
         'Pacific' : 'Mauna Kea',
         'South_American' : 'Aconcagua'}


def pacific_rim (collection):
    for thing in collection:
        if thing == 'Pacific':
            return collection[thing]


print(f"The fourth nearest star is {fourth_star}")
print(pacific_rim(peaks))