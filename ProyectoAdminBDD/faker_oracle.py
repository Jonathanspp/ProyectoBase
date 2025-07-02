from faker import Faker
import cx_Oracle
import schedule
import time
import os

os.environ["PATH"] = r"C:\oracle\instantclient_19_21" + ";" + os.environ["PATH"]

fake = Faker('es_ES')

def insertar_agente():
    try:
        conn = cx_Oracle.connect("polizasyfinanzas", "oracle", "192.168.1.132:1521/pdb1.udla.edu.ec")
        cursor = conn.cursor()

        nombre = fake.name()
        zona = fake.city()
        cursor.execute("INSERT INTO agentes (nombre, zona) VALUES (:1, :2)", (nombre, zona))
        conn.commit()

        print(f"[Oracle] Agente insertado: {nombre}, {zona}")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"[Oracle] Error: {e}")

schedule.every(1).minutes.do(insertar_agente)

print("⏳ Oracle: ejecutando cada minuto...")
while True:
    schedule.run_pending()
    time.sleep(1)
