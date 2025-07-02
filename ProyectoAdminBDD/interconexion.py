import cx_Oracle
import mysql.connector

def transferir_agentes_a_clientes():
    try:
        # Conexión Oracle
        conn_oracle = cx_Oracle.connect("polizasyfinanzas", "oracle", "192.168.1.132:1521/pdb1.udla.edu.ec")
        cursor_oracle = conn_oracle.cursor()

        # Conexión MySQL
        conn_mysql = mysql.connector.connect(
            host="192.168.1.130",
            user="admin",
            password="Admin123!",
            database="crm"
        )
        cursor_mysql = conn_mysql.cursor()

        cursor_oracle.execute("SELECT nombre FROM agentes")
        for (nombre,) in cursor_oracle.fetchall():
            email = f"{nombre.lower().replace(' ', '')}@mail.com"
            telefono = "0999999999"
            cursor_mysql.execute(
                "INSERT INTO clientes (nombre, email, telefono) VALUES (%s, %s, %s)",
                (nombre, email, telefono)
            )

        conn_mysql.commit()
        print("Datos transferidos correctamente.")

    except Exception as e:
        print(f"Error durante la transferencia: {e}")

    finally:
        cursor_oracle.close()
        cursor_mysql.close()
        conn_oracle.close()
        conn_mysql.close()

if __name__ == "__main__":
    transferir_agentes_a_clientes()
