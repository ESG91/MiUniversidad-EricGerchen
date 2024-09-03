import sqlite3

def delete_invalid_records(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Encuentra los IDs de estudiante inválidos
    cursor.execute("""
    SELECT estudiante_id
    FROM Academica_matricula
    WHERE estudiante_id NOT IN (
        SELECT dni
        FROM Academica_estudiante
    )
    """)
    invalid_ids = cursor.fetchall()

    # Elimina los registros inválidos
    for estudiante_id, in invalid_ids:
        cursor.execute("""
        DELETE FROM Academica_matricula
        WHERE estudiante_id = ?
        """, (estudiante_id,))

    conn.commit()
    conn.close()
    print("Registros inválidos eliminados con éxito.")

# Ruta a tu base de datos
db_path = 'MiUniversidad.db'
delete_invalid_records(db_path)
