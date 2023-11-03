import mysql.connector
from mysql.connector import Error

class Database:

    def __init__(self, host, database, user, password):

        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if self.connection.is_connected():
                db_Info = self.connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                self.cursor = self.connection.cursor()
                self.cursor.execute("select database();")
                record = self.cursor.fetchone()
                print("You're connected to database: ", record)

        except Error as e:
            print("Error while connecting to MySQL", e)

    def check_credencials_user_in_database(self, user_name, key_pass):
        # retorna uma lista de tuplas
        self.connect()
        command = f"SELECT user_name , key_pass FROM user_table WHERE user_name = '{user_name}' and key_pass = '{key_pass}' ;"
        self.cursor.execute(command)

        return self.cursor.fetchall()

    def get_all_card_before_today(self):
        command = "select * from card WHERE datecheck <= curdate();"
        self.cursor.execute(command)
        return self.cursor.fetchall()

    def update_card_datecheck_by_id(self, idcard, date_for_card_update):
        command = f'UPDATE card SET datecheck = "{date_for_card_update}" WHERE idcard = {idcard}'
        self.cursor.execute(command)
        self.connection.commit()

    def update_card_createdate_by_id(self, idcard, date_for_card_update):
        command = f'UPDATE card SET createdate = "{date_for_card_update}" WHERE idcard = {idcard}'
        self.cursor.execute(command)
        self.connection.commit()


    # ************************** MENU

    def create_card(self, question, answer):
            command = f'INSERT INTO card (question, answer, datecheck, createdate) VALUES ("{question}", "{answer}", curdate(), curdate());'
            self.cursor.execute(command)
            self.connection.commit() # editando o banco

    # UPDATE
    def update_card_by_id(self, id_card, question, answer):
        command = f'UPDATE card SET question = "{question}", answer = "{answer}" WHERE idcard = {id_card};'
        self.cursor.execute(command)
        self.connection.commit()

    # DELETE
    def delete_by_id(self, id_card):
        command = f'DELETE FROM card WHERE idcard = {id_card}'
        self.cursor.execute(command)
        self.connection.commit()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()
        print("MySQL connection is closed")

