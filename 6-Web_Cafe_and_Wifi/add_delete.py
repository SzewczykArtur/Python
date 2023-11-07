import sqlite3


class Insert:

    def __init__(self, name, map_url, img_url, location, has_sockets, has_toilet, has_wifi, can_take_calls, seats,
                 coffe_price):
        self.name = name
        self.map_url = map_url
        self.img_url = img_url
        self.location = location
        self.has_sockets = has_sockets
        self.has_toilet = has_toilet
        self.has_wifi = has_wifi
        self.can_take_calls = can_take_calls
        self.seats = seats
        self.coffe_price = coffe_price

    def insert_coffeehouse(self):
        connection = sqlite3.connect('instance/cafes.db')
        connection.execute(f"""
        INSERT INTO "cafe" ("name", "map_url", "img_url", "location", "has_sockets", "has_toilet", "has_wifi", 
        "can_take_calls", "seats", "coffee_price") VALUES ("{self.name}", "{self.map_url}", "{self.img_url}", "{self.location}",
        "{self.has_sockets}", "{self.has_toilet}", "{self.has_wifi}", "{self.can_take_calls}", "{self.seats}",
        "{self.coffe_price}")
        """)
        connection.commit()
        connection.close()


class Delete:

    def __init__(self, name):
        self.name = name

    def delete_coffeehouse(self):
        connection = sqlite3.connect('instance/cafes.db')
        check = connection.cursor()
        check_if_exist = check.execute(f"""
        SELECT * FROM "cafe" WHERE "name" = "{self.name}"
        """).fetchall()
        if check_if_exist == []:
            return False
        else:
            connection.execute(f"""
            DELETE FROM "cafe" WHERE "name" = "{self.name}"
            """)
            connection.commit()
            connection.close()
            return True