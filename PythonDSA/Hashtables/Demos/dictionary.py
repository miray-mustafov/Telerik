dictionary = {}
dictionary['hello'] = 'Здрасти'
dictionary['bye'] = 'Чао'

print(dictionary)
print('hello' in dictionary)

class Location:
    def __init__(self, lat, long):
        self.latitude = lat
        self.longitude = long

    def __eq__(self, other):
        if not isinstance(other, Location):
            return False
        
        return self.latitude == other.latitude and self.longitude == other.longitude

    def __hash__(self):
        return hash((self.latitude, self.longitude))

    def __str__(self):
        return f'{self.latitude},{self.longitude}'

locations = {
    Location(42.70, 23.33): 'Sofia',
    Location(40.25, 3.43): 'Madrid',
}

for location, city in locations.items():
    print(f'{location} = {city}')

# try the same after commenting out __hash__ and __eq__ in the Location class
print(Location(40.25, 3.43) in locations)