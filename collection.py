#girl = {
#	'name':'daria',
#	'city':'voronezh',
#	'last_name':'yankovskaya',
#	'age':'25',
#	}



#a = girl.get('name', 'petya').title()
#print(a)
#print(girl.get('name','vasya').title())



favorite_language = {
	'andrey':'python',
	'daria':'english',
	'sasha':'python',
	'sanek':'c++',
	'nikita':'russian sheet',
	'anton':'js',
	'petryxa':'broken russia',
	
}

friends = ['toxik', 'alpinist', 'satori']
kit = 'myr-myr myr-myay'
toxik = 'language dolboeba or murloc language (toxic)'
print('Spisok ludey:\n')
for name in sorted(favorite_language.keys()):
	print(f'\t{name.title()}')

	if name not in friends:
		language = favorite_language[name].upper()
	print(f'\nHello! {name.title()}, your language is {language}\n')
for n in friends:
	if n == 'toxik':
		print(f'Hello {n.title()}, your language is {toxik}\n')
	else:
		print(f'Hello {n.title()}, your language is {kit}\n')


for x in favorite_language.values():
	print(f'Languages in collection: \t{x.upper()}')

for y in set(favorite_language.values()):
	print(f'Language in set: \t{y.upper()}')


