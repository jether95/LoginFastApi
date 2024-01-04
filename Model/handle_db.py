import sqlite3

class HandleDB():
    def __init__(self):
        self._con = sqlite3.connect("./users.db")
        self._cur = self._con.cursor()

    def getAllUsers(self):
        data = self._cur.execute("SELECT * FROM users")
        return data.fetchall()

    def getOnly(self, data_user):
        data = self._cur.execute("SELECT * FROM users where username = '{}'".format(data_user))
        return data.fetchone();

    ##Para no pasar cada parametro para insertar datos, se pasa una lista como parametro
    ##la cual es fomateada con sus objetos en .format
    def insert(self, data_user):
        self._cur.execute("INSERT INTO users VALUES('{}','{}','{}','{}','{}','{}')".format(
            data_user["id"],
            data_user["firstname"],
            data_user["lastname"],
            data_user["username"],
            data_user["country"],
            data_user["password_user"]
        ))
        self._con.commit()

    def __del__(self):
        self._con.close()


'''db = HandleDB()
print(db.getAllUsers())
print(db.getOnly("Greyvic"))'''
'''
#Estructura para agregar data con un diccionario y db.insert
data = {
    "id": 3,
    "firstname": "John2",
    "lastname": "Sanchez2",
    "username": "Greyvic2",
    "country": "Colombia2",
    "password_user": "12342"
}
db.insert(data)
print(db.getAllUsers())'''