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

print(f"The fourth nearest star is {fourth_star}")

for location in peaks:
    if location == 'Pacific':
        print(peaks[location])