from fastapi import FastAPI,HTTPException,Depends
from typing import List
from sqlalchemy.orm import Session
from . import models,schemas,crud
from .database import SessionLocal,engine

models.Base.metadata.create_all(bind=engine)

app=FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/customer/{customer_id}",response_model=schemas.Customer)
def read_customer(customer_id:int,db:Session=Depends(get_db)):
    cus=crud.get_customer_by_id(db,customer_id)
    if cus is None:
        raise HTTPException(status_code=404,detail="Customer not found")
    return cus

@app.get("/order/{order_id}",response_model=schemas.Order)
def read_order(order_id:int,db:Session=Depends(get_db)):
    ord=crud.get_order_by_id(db,order_id)
    if ord is None:
        raise HTTPException(status_code=404,detail="Order not found")
    return ord

@app.get("/product/{product_id}",response_model=schemas.Product)
def read_product(product_id:int,db:Session=Depends(get_db)):
    prod=crud.get_product_by_id(db,product_id)
    if prod is None:
        raise HTTPException(status_code=404,detail="Product not found")
    return prod

@app.get("/orderitem/{orderitem_id}",response_model=schemas.OrderIte)
def read_orderitem(orderitem_id:int,db:Session=Depends(get_db)):
    ord_item=crud.get_orderitem_by_id(db,orderitem_id)
    if ord_item is None:
        raise HTTPException(status_code=404,detail="OrderItems not found")
    return ord_item

@app.get("/payment/{payment_id}",response_model=schemas.Payment)
def read_payment(payment_id:int,db:Session=Depends(get_db)):
    pay=crud.get_payment_by_id(db,payment_id)
    if pay is None:
        raise HTTPException(status_code=404,detail="Payment not found")
    return pay




@app.get("/customer/",response_model=List[schemas.Customer])
def read_customers(skip:int=0,limit:int=100,db:Session=Depends(get_db)):
    return crud.get_customers(db,skip,limit)

@app.get("/order/",response_model=List[schemas.Order])
def read_orders(skip:int=0,limit:int=100,db:Session=Depends(get_db)):
    return crud.get_orders(db,skip,limit)

@app.get("/product/",response_model=List[schemas.Product])
def read_products(skip:int=0,limit:int=100,db:Session=Depends(get_db)):
    return crud.get_products(db,skip,limit)

@app.get("/orderitem/",response_model=List[schemas.OrderItem])
def read_orderitems(skip:int=0,limit:int=100,db:Session=Depends(get_db)):
    return crud.get_orderitems(db,skip,limit)

@app.get("/payment/",response_model=List[schemas.Payment])
def read_payments(skip:int=0,limit:int=100,db:Session=Depends(get_db)):
    return crud.get_payments(db,skip,limit)


