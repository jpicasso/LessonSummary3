from database import CursorFromConnectionFromPool

class User:
    def __init__(self, email, first_name, last_name, id):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    def __repr__(self):
        return "<User {}>".format(self.email)

    def save_to_db(self):
        with CursorFromConnectionFromPool() as cursor:
            # this is similar to the .format method; it is also more secure than doing it in other ways
            cursor.execute('INSERT INTO users (email, first_name, last_name) VALUES (%s, %s, %s)', (self.email, self.first_name, self.last_name))
            # cursor.execute('SELECT * FROM purchases')

        # alternative longer code...
        # connection = psycopg2.connect(user='postgres', password='Apple2017', database='learning', host='localhost')
        # with connection.cursor() as cursor:
        #     # this is similar to the .format method; it is also more secure than doing it in other ways
        #     cursor.execute('INSERT INTO users (email, first_name, last_name) VALUES (%s, %s, %s)',
        #     (self.email, self.first_name, self.last_name))
        #     cursor.execute('SELECT * FROM purchases')
        #     for row in cursor:
        #         print(row)
        # connection.commit()
        # connection.close()

    @classmethod
    def print_user_db(cls):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('SELECT * FROM users;')
            for record in cursor:
                print(record)
            
            # cursor.execute('SELECT * FROM users WHERE id=%s', (x,))
            # user_db_data = cursor.fetchone()
            # print(user_db_data[0], user_db_data[2], user_db_data[3], user_db_data[1])

    @classmethod
    def load_from_db_by_email(cls, email):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('SELECT * FROM users WHERE email=%s', (email,))
            user_data = cursor.fetchone()
            return cls(user_data[1], user_data[2], user_data[3], user_data[0])





