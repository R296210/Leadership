import sqlite3 as sql

def createDB():
    conn= sql.connect("dbUNO.db")
    conn.commit()
    conn.close()

def createTable():
    conn= sql.connect("dbUNO.db")
    cursor = conn.cursor()
    cursor.execute(
            """CREATE TABLE obligaciones (
                Name text,
                Obligaciones text,
                Fecha integer
            )"""
    )
    conn.commit()
    conn.close()

def insertRow(name, followers, subs):
    conn= sql.connect("dbUNO.db")
    cursor = conn.cursor()
    instruction = f"INSERT INTO pendientes VALUES ('{name}', {followers}, {subs})"
    cursor.execute(instruction)
    conn.commit()
    conn.close()

def insertRows(pendientesList):
    conn= sql.connect("dbUNO.db")
    cursor = conn.cursor()
    instruction = f"INSERT INTO pendientes VALUES (?, ?, ?)"
    cursor.executemany(instruction, pendientesList)
    conn.commit()
    conn.close()

def readRows():
    conn= sql.connect("dbUNO.db")
    cursor = conn.cursor()
    instruction = f"SELECT * FROM pendientes"
    cursor.execute(instruction)
    datos=cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)

def readOrdered(field):
    conn= sql.connect("dbUNO.db")
    cursor = conn.cursor()
    instruction = f"SELECT * FROM pendientes ORDER BY {field} DESC"
    cursor.execute(instruction)
    datos=cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)

def search():
    conn= sql.connect("dbUNO.db")
    cursor = conn.cursor()
    #EXACTAMENTE COMO SE ESCRIBE 
    #instruction = f"SELECT * FROM pendientes WHERE name='robert'"
    #BUSCA ALGO SIMILAR EN LA FORMA DE ESCRIBIR
    #instruction = f"SELECT * FROM pendientes WHERE name like 'j%'"
    instruction = f"SELECT * FROM pendientes WHERE subs < 10"
    cursor.execute(instruction)
    datos=cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)

def updateField():
    conn= sql.connect("dbUNO.db")
    cursor = conn.cursor()
    instruction = f"UPDATE pendientes SET subs=12 WHERE name like 'Gerardo'"
    cursor.execute(instruction)
    conn.commit()
    conn.close()

def deleteRow():
    conn= sql.connect("dbUNO.db")
    cursor = conn.cursor()
    instruction = f"DELETE FROM pendientes WHERE name='Toledo'"
    cursor.execute(instruction)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    #1#createDB()

    createTable()
    #3#insertRow("Roberto", 32, 3)
    
    #4#actualizaciones = [
    #    ("Gerardo", 27, 0),
    #    ("Minerva", 50, 35),
    #    ("Toledo", 31, 10)]
    #4#insertRows(actualizaciones)
    
    #5#readRows()
    #6#readOrdered("subs")
    #7#search()
    #8#updateField()
    #9#deleteRow()

