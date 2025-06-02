people = [{"name": "Harry", "house":"Gryffinder"},
          {"name": "Cho", "house":"Ravenclaw"},
          {"name": "Draco", "house":"Slytherin"}]    


people.sort(key=lambda person: person["name"])
print(people)

"""
    # another method for the abve
def f(person): 
    return person["name"]    
people.sort(key=f)
print(people)

    #another method
def f(person): 
    return person["house"]    
people.sort(key=f)
print(people)
"""
