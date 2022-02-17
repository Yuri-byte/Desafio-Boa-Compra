class Product:
    def __init__(self, name, distance, weight):
        self.name = name
        self.distance = distance
        self.weight = weight
    
    def __repr__(self) -> str:
        return self.name + ', Distance: ' + str(self.distance) + 'km, Weight: ' + str(self.weight) + 'kg'