

class Item:

	def __init__(self, name, group=[], weight=1, recipe=[]):
		self.name 	= name
		self.group  = group
		self.weight = weight
		self.recipe = recipe

	def __str__(self):
		return 'Name: {}\nGroup(s): {}\nWeight: {}\nCraftable: {}'.format(
			self.name, self.group, self.weight, self.recipe != [])


def read_items_from_json(filename):

	with open(filename) as f:

		data = eval(f.read())

	items = {}
	for item in data:
		items[item['name']] = Item(**item)

	return items
			

def get_recipe(item, level=0):
		
	# sort by name
	item.recipe.sort(key=lambda x: x[0])

	# print item name if level 0
	if level == 0: print(item.name)

	for name, amount in item.recipe:
		print('  ' * level, f'{amount} x {name}')
		other = items[name]
		if other.recipe != []:
			get_recipe(other, level + 1)


if __name__ == '__main__':
	
	items = read_items_from_json('items.json')

	for key in items.keys():
		print(items[key], end='\n\n')