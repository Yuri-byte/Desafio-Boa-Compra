from pprint import pprint
from company import Company
from product import Product
from calculator import Calculator
import csv

def main():
    c = Calculator()
    # setting currency as an integer to have more precision than float type
    boa_dex = Company('BoaDex', 1000, 5)
    boa_log = Company('BoaLog', 430, 12)
    max5 = Company('Transboa (ate 5Kg)', 210, 110, 5, 0)
    min5 = Company('Transboa (+5Kg)', 1000, 1, None, 5)
    products_csv = open('products_csv.csv', 'r')
    reader = csv.reader(products_csv)
    products = []
    for row in reader:
        products.append(Product(row[0], int(row[1]), int(row[2])))
    #end for
    for product in products:
        prices = []
        prices.append({'Company': boa_dex.name, 'Price': c.calculate(boa_dex, product)})
        prices.append({'Company': boa_log.name, 'Price': c.calculate(boa_log, product)})
        prices.append({'Company': min5.name, 'Price': c.calculate(min5, product)})
        prices.append({'Company': max5.name, 'Price': c.calculate(max5, product)})
        print('--------------------------------------------------------')
        print(str(product) + ' ->')
        pprint(sorted(list(filter(filter_by_price, prices)), key=sort_by_key))
    #end for
#end main     

def sort_by_key(list):
    return list['Price']

def filter_by_price(list):
    if list['Price'] is not None:
        return True
    else:
        return False


if __name__ == "__main__":
    main()