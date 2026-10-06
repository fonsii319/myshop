from database import get_connection, init_database


def seed_products():
    connection = get_connection()

    products = [
        (
            "Auriculares Urban Sound",
            "Auriculares inalámbricos ligeros con conexión Bluetooth y batería de larga duración.",
            39.99,
            "headphones.jpg",
            "Electrónica",
            15
        ),
        (
            "Teclado Compact Pro",
            "Teclado compacto para escritorio con diseño moderno y teclas de perfil bajo.",
            49.99,
            "keyboard.jpg",
            "Electrónica",
            10
        ),
        (
            "Mochila Everyday",
            "Mochila resistente para uso diario, trabajo o estudio.",
            34.50,
            "backpack.jpg",
            "Accesorios",
            20
        ),
        (
            "Botella Thermal",
            "Botella reutilizable de acero inoxidable con aislamiento térmico.",
            24.99,
            "bottle.jpg",
            "Hogar",
            25
        ),
        (
            "Lámpara Desk Light",
            "Lámpara de escritorio con diseño minimalista para espacios de trabajo.",
            29.95,
            "lamp.jpg",
            "Hogar",
            8
        )
    ]

    existing_products = connection.execute(
        "SELECT COUNT(*) FROM products"
    ).fetchone()[0]

    if existing_products == 0:
        connection.executemany("""
            INSERT INTO products (
                name,
                description,
                price,
                image,
                category,
                stock
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, products)

        connection.commit()
        print("Productos de prueba creados.")
    else:
        print("Los productos ya existen. No se agregaron duplicados.")

    connection.close()


if __name__ == "__main__":
    init_database()
    seed_products()
