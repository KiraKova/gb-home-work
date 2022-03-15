def my_f(name, lastname, year, city, email, phone):
    return f"Имя: {name}," \
           f" Фамилия: {lastname}, " \
           f"Год рождения: {year}, " \
           f"Город: {city}, " \
           f"Email: {email}," \
           f"Телефон: {phone}"


print(my_f(name=input('Введите имя: '), lastname=input('Введите фамилию: '), year=input('Год рождения: '),
           city=input('Город проживания: '), email=input('Email: '), phone=input('Телефон: ')))
