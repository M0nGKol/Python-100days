# data = {1: 'Dog',2 : 'Cat',3 : 'Shark',4 : 'Tiger'}
# print(data.get(3,'Not found'))

# keys =['Audi','Tesla','Toyota']
# values = ['10k','200k','23k']
# data = dict(zip(keys,values))
# data['Porshce'] = '50k'
# del data['Audi']
# print(data)
# print(data['Toyota'])


car = {'Toyota':{'10k','22k','30k'},'Tesla':'30k','Audi':['18k','24k']}

for i in car.keys():
    print(i)