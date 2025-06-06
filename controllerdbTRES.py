import sqlite3 as sql

#creando tabla 3 udemy SEC29NO212
def createTable():
    conn= sql.connect("dbUNO.db")
    cursor = conn.cursor()
    cursor.execute(
            """CREATE TABLE AGENDA (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                Nombre TEXT 
            )"""
    )
    conn.commit()
    conn.close()

#agregando datos a tercer tabla en base de datos 1 

def insertRegister(Nombre):
    conn= sql.connect("dbUNO.db")
    cursor = conn.cursor()
    instruction = f"INSERT INTO AGENDA (Nombre) VALUES ('{Nombre}')"
    cursor.execute(instruction)
    conn.commit()
    conn.close()

#LEYENDO DATOS 

def readRows():
    conn= sql.connect("dbUNO.db")
    cursor = conn.cursor()
    instruction = f"SELECT * FROM AGENDA"
    cursor.execute(instruction)
    datos=cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)

def dropTable():
    conn= sql.connect("dbUNO.db")
    cursor = conn.cursor()
    cursor.execute(
            """DROP TABLE AGENDA"""
    )
    conn.commit()
    conn.close()

def deleteRow():
    conn= sql.connect("dbUNO.db")
    cursor = conn.cursor()
    instruction = f"DELETE FROM AGENDA WHERE Edad=0"
    cursor.execute(instruction)
    conn.commit()
    conn.close()



#renombrando tabla AGENDA udemy SEC29NO220
def renameTable():
    conn= sql.connect("dbUNO.db")
    cursor = conn.cursor()
    instruction = f"ALTER TABLE tmp RENAME TO AGENDA"
    cursor.execute(instruction)
    conn.commit()
    conn.close()

#renombrando tabla AGENDA udemy SEC29NO220
def addColumna():
    conn= sql.connect("dbUNO.db")
    cursor = conn.cursor()
    instruction = f"ALTER TABLE tmp ADD COLUMN EdadeS INT"
    cursor.execute(instruction)
    conn.commit()
    conn.close()



if __name__ == "__main__":
    
    
    #createDB()
    #createTable()
    
    #dropTable()
    #renameTable()
    
    #addColumna()
    #insertRegister("Juan")

    #4#actualizaciones = [
    #    ("Gerardo", 27, 0),
    #    ("Minerva", 50, 35),
    #    ("Toledo", 31, 10)]
    #4#insertRows(actualizaciones)

    #readRows()
    #6#readOrdered("subs")
    deleteRow()

    #7#search()    
    #8#updateField()    
    
    