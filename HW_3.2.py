def my_func(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])


print(my_func(surname='Yudin', name='Maxim', year='1998', city='Saint-Petersburg', email='hack@mail.ru',
              telephone='8-999-532-02-03'))
