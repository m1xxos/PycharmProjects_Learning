def select_dates(potential_dates):
    names = []
    for key in potential_dates:
        if key['age'] > 30 and 'art' in key['hobbies'] and key['city'] == 'Berlin':
            names.append(key['name'])
    return str(', '.join(str(name) for name in names))


# dates = [{"name": "Julia", "gender": "female", "age": 29,
#                     "hobbies": ["jogging", "music"], "city": "Hamburg"},
#                    {"name": "Sasha", "gender": "male", "age": 18,
#                     "hobbies": ["rock music", "art"], "city": "Berlin"},
#                    {"name": "Maria", "gender": "female", "age": 35,
#                     "hobbies": ["art"], "city": "Berlin"},
#                    {"name": "Daniel", "gender": "non-conforming", "age": 50,
#                     "hobbies": ["boxing", "reading", "art"], "city": "Berlin"},
#                    {"name": "John", "gender": "male", "age": 41,
#                     "hobbies": ["reading", "alpinism", "museums"], "city": "Munich"}]
#
# print(select_dates(dates))
