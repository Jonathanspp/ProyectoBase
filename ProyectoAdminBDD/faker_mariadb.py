from faker import Faker
import mariadb
import schedule
import time

fake = Faker('es_ES')

def insertar_siniestro():
    try:
        conn = mariadb.connect(
            user="admin",
            password="Admin123!",
            host="192.168.1.129",
            port=33061,
            database="siniestros"
        )
        cursor = conn.cursor()

        descripcion = fake.sentence()
        fecha = fake.date()
        monto = round(fake.pyfloat(left_digits=4, right_digits=2, positive=True), 2)

        cursor.execute("""
            INSERT INTO siniestros (descripcion, fecha, monto_estimado)
            VALUES (?, ?, ?)
        """, (descripcion, fecha, monto))

        conn.commit()
        print(f"[MariaDB] Siniestro insertado: {descripcion} | {fecha} | {monto}")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"[MariaDB] Error: {e}")

schedule.every(1).minutes.do(insertar_siniestro)

print("⏳ MariaDB: ejecutando cada minuto...")
while True:
    schedule.run_pending()
    time.sleep(1)
