from datetime import datetime as dt
import sqlite3


class Database:

    def __init__(self, file: str):
        self.file: str = file

    def read_data(self):
        """
        Read database and return a list.
        """

        connection = sqlite3.connect(self.file)
        data = connection.execute("""
        SELECT * FROM "Data"
        """)
        data_list: list[str] = data.fetchall()
        # print(data)
        connection.commit()
        connection.close()
        datas = {}
        for data in data_list:
            datas[data[1]] = {'id': data[0],
                              'password': data[2],
                              'create_date': data[3]}
        return datas


class UpdateDatabase(Database):

    def __init__(self, file, email, password):
        super().__init__(file)
        self.email = email
        self.password = password

    def add_new_user(self):
        """
        Add new user to database
        """
        date = dt.now().strftime('%d-%m-%Y')
        connection = sqlite3.connect(self.file)
        connection.execute(f"""
        INSERT INTO "Data" ("email", "password", "creation_date")
        VALUES ("{self.email}", "{self.password}", "{date}")
        """)
        connection.commit()
        connection.close()
        return 'Done'

    def delete_user(self):
        """
        This method allow to delete user. Before we need give email and password
        """
        connection = sqlite3.connect(self.file)
        connection.execute(f"""
        DELETE FROM "Data" 
        WHERE "email" = "{self.email}" and "password" = "{self.password}"
        """)
        connection.commit()
        connection.close()
        return 'User delete!'


class AdminUpdate(Database):

    def __init__(self, file, id):
        super().__init__(file)
        self.id = id

    def delete_account(self):
        connection = sqlite3.connect(self.file)
        connection.execute(f"""
        DELETE FROM "Data" WHERE "id" = {self.id}
        """)
        connection.commit()
        connection.close()
        print('Account is deleted')

    def update_password(self, new_password):
        """
        Update password by admin
        """
        connection = sqlite3.connect('instance/data.sql')
        connection.execute(f"""
                        UPDATE "Data" SET "password" = "{new_password}" WHERE "id" = "{self.id}"
                        """)
        connection.commit()
        connection.close()

    def update_email(self, new_email):
        """
        User can update a email
        """
        connection = sqlite3.connect('instance/data.sql')
        connection.execute(f"""
        UPDATE "Data" SET "email" = "{new_email}" WHERE "id" = "{self.id}"
        """)
        connection.commit()
        connection.close()

# new_user = UpdateDatabase('instance/data.sql', 'artur.ss@gmail.com', 'Waasdir12aa')
# result = new_user.add_new_user()
# print(result)
# read = Database('instance/data.sql').read_data()
# print(read['arturosz10@wp.pl'])
# delete = UpdateDatabase('instance/data.sql', 'artur.ss@gmail.com', 'Waasdir12aa')
# result = delete.delete_user()
# print(result)