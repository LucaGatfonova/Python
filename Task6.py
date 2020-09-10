product_dict = []
product_list = []
product_analysis = {}
while True:
    n = int(input('Введите номер товара'))
    product_dict = dict({'название': input("Введите название "), 'цена': input("Введите цену "),
                                   'количество': input('Введите количество '),
                                   'eд': input("Введите единицу измерения ")})
    product_list.append((n, product_dict))
    q = (input("Закончить ввод товаров? Введите да, нет. ")).lower()
    if q == "да":
        break
    product_analysis = dict({'название': product_dict.get('название'), 'цена': product_dict.get('цена'),
                           'количество': product_dict.get('количество'),
                           'ед': product_dict.get('ед')})
print(product_list)
print(product_analys)
