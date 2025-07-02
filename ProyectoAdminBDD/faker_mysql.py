from faker import Faker
import mysql.connector
import schedule
import time

fake = Faker('es_ES')

def insertar_cliente():
    try:
        conn = mysql.connector.connect(
            user="admin",
            password="Admin123!",
            host="192.168.1.130",
            port=33063,
            database="crm"
        )
        cursor = conn.cursor()

        nombre = fake.name()
        email = fake.email()
        telefono = fake.phone_number()

        cursor.execute("""
            INSERT INTO clientes (nombre, email, telefono)
            VALUES (%s, %s, %s)
        """, (nombre, email, telefono))

        conn.commit()
        print(f"[MySQL] Cliente insertado: {nombre} | {email} | {telefono}")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"[MySQL] Error: {e}")

schedule.every(1).minutes.do(insertar_cliente)

print("⏳ MySQL: ejecutando cada minuto...")
while True:
    schedule.run_pending()
    time.sleep(1)
