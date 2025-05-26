class Pet :
    all=[]
    PET_TYPES=["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    def __init__(self,name,pet_type,owner =None):
        if pet_type  not in Pet.PET_TYPES:
            raise Exception(f"Invalud pet type:{pet_type}.Must be in {Pet.PET_TYPES} ")
        if owner is not None and not isinstance(owner, Owner):
            raise TypeError("owner must be an instance of Owner class or None")

        self.name=name
        self.pet_type=pet_type
        self._owner=None

        Pet.all.append(self)


        if owner:
            self.owner = owner
      
    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self,new_owner):
        if not isinstance(new_owner, Owner):
            raise TypeError("owner must be an instance of Owner class")
        self._owner = new_owner


        

class Owner:
    def __init__(self,name):
        self.name=name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
          raise TypeError("pet must be an instance of the Pet class")
        pet.owner = self
    
    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)


      
