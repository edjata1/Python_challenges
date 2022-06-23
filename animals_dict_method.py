# Dictionary Method and how to use them

animals = { 'A':'Ant', 'B':'Bat', 'c':'calf', 'd':'doll', 'e':'elephant',
            'f':'flight', 'g':'gem', 'h':'hall', 'i':'ignite', 'j':'jump'}

print('Dictionary:', animals)

# copy()
wild_animals = animals.copy()
print('Just a copy:', wild_animals)
# update()
animals.update({'A': 'Djata'})
print('update:', animals)
# get()
print('get:', animals.get('h'))
# pop()
animals.pop('c')
print('pop:', animals)
# value()
print('All values:', animals.values())
# keys()
print('Keys:', animals.keys())
# items()
print('items:', animals.items())
# sort()
print('sort:', sorted(animals.items()))
# len()
print('lem:', len(animals))
# str()
print('str:', str(animals))
animals.clear()
print(animals)

