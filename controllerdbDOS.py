import sqlite3 as sql

#agregando datos a segunda tabla en base de datos 1 

def insertRow(Name, Obligaciones, Fecha):
    conn= sql.connect("dbUNO.db")
    cursor = conn.cursor()
    instruction = f"INSERT INTO obligaciones VALUES ('{Name}', '{Obligaciones}', {Fecha})"
    cursor.execute(instruction)
    conn.commit()
    conn.close()
    
if __name__ == "__main__":
    #createDB()
    #createTable()
    
    insertRow("Roberto", "35K/MONTH", 202501)
    
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

