name = input('Введите имя: ')
surname = input('Введите фамилия: ')
year = input('Введите год рождения: ')
city = input('Введите город проживания: ')
email = input('Введите email: ')
tel = input('Введите телефон: ')


def my_func(*args):
    print(f"Имя: {name}, Фамилия: {surname}, Год рождения: {year}, Город проживания: {city}, email: {email}, телефон: {tel}")


my_func(name, surname, year, city, email, tel)
