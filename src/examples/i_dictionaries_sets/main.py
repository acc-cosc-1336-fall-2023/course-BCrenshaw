import dictionaries as d

phone_book = {'Chris':'555-1111',
             'Katie':'555-2222',
             'Chris':'555-3333'}

#print(phone_book)
#print(phone_book['Chris'])
#print(phone_book['Katie'])

#for n in phone_book:
#    print(n + '\t' + phone_book[n])

#print('values only')
#for n in phone_book.values():
#    print(n)

#print('dictionary items')
#for n in phone_book.items():
#    print(n)

#print(d.is_key_in_dictionary('Chris', phone_book))

for n, i in phone_book.items():
    print(n + '\t' + i)