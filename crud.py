from databaseConnection import connection, cursor
import schemas

def get_item(item_id: int):

    cursor.execute("SELECT * FROM items WHERE id = %s", (item_id,))
    return cursor.fetchone()

def get_items(skip: int = 0, limit: int = 10):
     
    cursor.execute("SELECT * FROM items ORDER BY id OFFSET %s LIMIT %s", (skip, limit))
    return cursor.fetchall()

def create_item(item: schemas.ItemCreate):
    
    cursor.execute(
        "INSERT INTO items (name, description, price, quantity) VALUES (%s, %s, %s, %s) RETURNING *",
        (item.name, item.description, item.price, item.quantity),
    )
    connection.commit()
    return cursor.fetchone()

def update_item(item_id: int, item: schemas.ItemUpdate):
    
    cursor.execute(
        "UPDATE items SET name = %s, description = %s, price = %s, quantity = %s WHERE id = %s RETURNING *",
        (item.name, item.description, item.price, item.quantity, item_id),
    )
    connection.commit()
    return cursor.fetchone()

def delete_item(item_id: int):
 
    cursor.execute("DELETE FROM items WHERE id = %s RETURNING *", (item_id,))
    connection.commit()
    return cursor.fetchone()