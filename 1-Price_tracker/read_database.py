import sqlite3


class Data:
    """
    Open database and create a list.
    """

    def __init__(self, file: str):
        self.file = file

    def item_data(self):
        connection = sqlite3.connect(self.file)
        data = connection.execute("""
        SELECT shop.shop_name, product.product_name, data.link, data.price 
        FROM 'data' 
        LEFT JOIN 'shop' ON data.id_shop = shop.id
        LEFT JOIN 'product' ON data.id_product = product.id
        ORDER BY product.product_name ASC
        """)
        data_list: list[str] = data.fetchall()
        connection.commit()
        connection.close()
        return data_list

    def shop_data(self):
        shop_dict = {}
        connection = sqlite3.connect(self.file)
        data = connection.execute("""
                SELECT * FROM 'shop' 
                """)
        data_list: list[str] = data.fetchall()
        connection.commit()
        connection.close()
        for shop in data_list:
            shop_dict[shop[1]] = {'tag': shop[2], 'tag_name': shop[3]}
        return shop_dict


class AddNewItem:
    """
    Add new item to database, which can be searched by program
    """
    def __init__(self, file: str, shop_name: str, product_name: str, link: str, price: str):
        self.file = file
        self.shop_name = shop_name
        self.product_name = product_name
        self.link = link
        self.price = price

    def shops_list(self):
        connection = sqlite3.connect(self.file)
        data = connection.execute("""
        SELECT * FROM 'shop'
        """)
        data_list: list[str] = data.fetchall()
        connection.commit()
        connection.close()

        shops_list: list[str] = [shop[1].lower() for shop in data_list]
        return shops_list

    def products_list(self):
        connection = sqlite3.connect(self.file)
        data = connection.execute("""
                SELECT * FROM 'product'
                """)
        data_list: list[str] = data.fetchall()
        connection.commit()
        connection.close()

        products_list: list[str] = [product[1].lower() for product in data_list]
        return products_list

    def add_new_shop(self):
        tag = input('What type tag has the price?: ')
        tag_name = input('What is class name?: ')
        connection = sqlite3.connect(self.file)
        connection.execute(f"""
                INSERT INTO "shop" ("shop_name", "tag", "tag_name") 
                VALUES ("{(self.shop_name).lower().captalize()}","{tag}", "{tag_name}")
                """)
        connection.commit()
        connection.close()

    def add_new_item(self):
        connection = sqlite3.connect(self.file)
        connection.execute(f"""
                INSERT INTO "product" ("product_name") VALUES ("{self.product_name}")
                """)
        connection.commit()
        connection.close()

    def add(self):
        """
        First check if this shop is on the database. If not add new shop.
        Second check if this item is in the database. If not add new item.
        If everthing is fine, add new row to tabel 'data'
        """
        if self.shop_name.lower() not in self.shops_list():
            self.add_new_shop()
        if self.product_name.lower() not in self.products_list():
            self.add_new_item()
        print(self.shops_list())
        shop_id = int(self.shops_list().index(self.shop_name.lower())) + 1
        print(shop_id)
        product_id = int(self.products_list().index(self.product_name)) + 1
        connection = sqlite3.connect(self.file)
        connection.execute(f"""
                        INSERT INTO "data" ("id_shop", "id_product", "link", "price") 
                        VALUES ("{shop_id}", "{product_id}", "{self.link}", "{self.price}")
                        """)
        connection.commit()
        connection.close()

