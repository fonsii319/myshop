from database import get_connection


def get_all_products(search=None, category=None):
    connection = get_connection()

    query = """
        SELECT *
        FROM products
        WHERE 1 = 1
    """

    parameters = []

    if search:
        query += """
            AND (
                name LIKE ?
                OR description LIKE ?
            )
        """

        search_value = f"%{search}%"
        parameters.extend([search_value, search_value])

    if category:
        query += """
            AND category = ?
        """

        parameters.append(category)

    query += """
        ORDER BY created_at DESC
    """

    products = connection.execute(query, parameters).fetchall()

    connection.close()

    return products


def get_product_by_id(product_id):
    connection = get_connection()

    product = connection.execute("""
        SELECT *
        FROM products
        WHERE id = ?
    """, (product_id,)).fetchone()

    connection.close()

    return product


def get_categories():
    connection = get_connection()

    categories = connection.execute("""
        SELECT DISTINCT category
        FROM products
        ORDER BY category
    """).fetchall()

    connection.close()

    return categories


def add_product(name, description, price, image, category, stock):
    connection = get_connection()

    connection.execute("""
        INSERT INTO products (
            name,
            description,
            price,
            image,
            category,
            stock
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        name,
        description,
        price,
        image,
        category,
        stock
    ))

    connection.commit()
    connection.close()





