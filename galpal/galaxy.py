class Galaxy: 
    def __init__(self, number, name, morph_type, distance, stellar_mass, constellation, star_formation): 
        self.number = number 
        self.name = name 
        self.morph_type = morph_type 
        self.distance = distance 
        self.stellar_mass = stellar_mass
        self.constellation = constellation
        self.star_formation = star_formation 
        self.choice = 'None' 
        self.grade = 'None'


    def update_choice(self): 
        pass

        #this function should be called when a button is clicked ('Spiral' or 'Elliptical')
        #to update self.choice to equal the selection
