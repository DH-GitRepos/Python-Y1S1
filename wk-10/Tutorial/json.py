import simplejson

book_data = {
    "title": "Data Access",
    "date": "1999-11-01",
    "price": 26.00,
    "discount": 6.5
    }

# serialise data
with open('book.json', 'w') as json_out:
    simplejson.dump(book_data, json_out, indent=2)

# deserialise data
with open('book.json') as json_in:
    book_data1 = simplejson.load(json_in)

print(book_data)
print(book_data1)

