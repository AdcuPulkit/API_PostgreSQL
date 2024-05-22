from fastapi import FastAPI, Depends, HTTPException
import schemas, crud

app = FastAPI()

@app.post("/items/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate):
    db_item = crud.create_item(item)
    return db_item

@app.get("/items/{item_id}", response_model=schemas.Item)
def read_item(item_id: int): 
    db_item = crud.get_item(item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 10):
    items = crud.get_items(skip=skip, limit=limit)
    return items

@app.put("/items/{item_id}", response_model=schemas.Item)
def update_item(item_id: int, item: schemas.ItemUpdate):
    db_item = crud.update_item(item_id=item_id, item=item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.delete("/items/{item_id}", response_model=schemas.Item)
def delete_item(item_id: int):
    db_item = crud.delete_item(item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item
