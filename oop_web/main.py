from oop_web.data_base import DataBase
from oop_web.data_parser import DataParser

db = DataBase()
products = DataParser()
#print(products.get_products_list())
#products.get_all_promo_page()
f = products.get_all_promo_pages()
d = products.get_prod()
print(1)