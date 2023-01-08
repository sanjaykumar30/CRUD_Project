from fastapi import FastAPI,HTTPException,Depends
from typing import List
from sqlalchemy.orm import Session
from . import models,schemas,crud
from .database import SessionLocal,engine,Base

Base.metadata.create_all(bind=engine)

app=FastAPI()

#Dependency 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Get request
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

@app.get("/orderitem/{orderitem_id}",response_model=schemas.OrderItem)
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

#Post request
@app.post("/customer/",response_model=schemas.Customer)
def create_customer(customer:schemas.Customer,db:Session=Depends(get_db)):
    cus=crud.get_customer_by_id(db,customer.customer_id)
    if cus:
        raise HTTPException(status_code=400,detail="Customer id already found")
    return crud.create_customer(db,customer)

@app.post("/order/",response_model=schemas.Order)
def create_order(order:schemas.Order,db:Session=Depends(get_db)):
    ord=crud.get_order_by_id(db,order.order_id)
    if ord:
        raise HTTPException(status_code=400,detail="Order id already found")
    return crud.create_order(db,order)

@app.post("/product/",response_model=schemas.Product)
def create_product(product:schemas.Product,db:Session=Depends(get_db)):
    prod=crud.get_product_by_id(db,product.product_id)
    if prod:
        raise HTTPException(status_code=400,detail="Product id already found")
    return crud.create_product(db,product)

@app.post("/orderitem/",response_model=schemas.OrderItem)
def create_orderitem(orderitem:schemas.OrderItem,db:Session=Depends(get_db)):
    ord_item=crud.get_orderitem_by_id(db,orderitem.orderitem_id)
    if ord_item:
        raise HTTPException(status_code=400,detail="OrderItem id already found")
    return crud.create_orderitem(db,orderitem)

@app.post("/payment/",response_model=schemas.Payment)
def create_payment(payment:schemas.Payment,db:Session=Depends(get_db)):
    pay=crud.get_payment_by_id(db,payment.payment_id)
    if pay:
        raise HTTPException(status_code=400,detail="Payment id already found")
    return crud.create_payment(db,payment)


#Put request
@app.put("/customer/",response_model=schemas.Customer)
def update_customer(customer:schemas.Customer,db:Session=Depends(get_db)):
    cus=crud.get_customer_by_id(db,customer.customer_id)
    if cus is None:
        raise HTTPException(status_code=404,detail="Customer id not found")
    return crud.update_customer(db,customer)

@app.put("/order/",response_model=schemas.Order)
def update_order(order:schemas.Order,db:Session=Depends(get_db)):
    ord=crud.get_order_by_id(db,order.order_id)
    if ord is None:
        raise HTTPException(status_code=404,detail="Order id not found")
    return crud.update_order(db,order)

@app.put("/product/",response_model=schemas.Product)
def update_product(product:schemas.Product,db:Session=Depends(get_db)):
    prod=crud.get_product_by_id(db,product.product_id)
    if prod is None:
        raise HTTPException(status_code=404,detail="Product id not found")
    return crud.update_product(db,product)

@app.put("/orderitem/",response_model=schemas.OrderItem)
def update_orderitem(orderitem:schemas.OrderItem,db:Session=Depends(get_db)):
    ord_item=crud.get_orderitem_by_id(db,orderitem.orderitem_id)
    if ord_item is None:
        raise HTTPException(status_code=404,detail="OrderItem id not found")
    return crud.update_orderitem(db,orderitem)

@app.put("/payment/",response_model=schemas.Payment)
def update_payment(payment:schemas.Payment,db:Session=Depends(get_db)):
    pay=crud.get_payment_by_id(db,payment.payment_id)
    if pay is None:
        raise HTTPException(status_code=404,detail="Payment id not found")
    return crud.update_payment(db,payment)

#Delete request
@app.delete("/customer/{customer_id}")
def delete_customer(customer_id:int,db:Session=Depends(get_db)):
    cus=crud.get_customer_by_id(db,customer_id)
    if cus is None:
        raise HTTPException(status_code=404,detail="Customer id not found")
    crud.delete_customer(db,customer_id)
    return {"Table":"customer_dataset","Customer Id":customer_id,"Message":"Successfully Deleted"}

@app.delete("/order/{order_id}")
def delete_order(order_id:int,db:Session=Depends(get_db)):
    ord=crud.get_order_by_id(db,order_id)
    if ord is None:
        raise HTTPException(status_code=404,detail="Order id not found")
    crud.delete_order(db,order_id)
    return {"Table":"order_dataset","Order Id":order_id,"Message":"Successfully Deleted"}

@app.delete("/product/{product_id}")
def delete_product(product_id:int,db:Session=Depends(get_db)):
    prod=crud.get_product_by_id(db,product_id)
    if prod is None:
        raise HTTPException(status_code=404,detail="Product id not found")
    crud.delete_product(db,product_id)
    return {"Table":"product_dataset","product Id":product_id,"Message":"Successfully Deleted"}

@app.delete("/orderitem/{orderitem_id}")
def delete_orderitem(orderitem_id:int,db:Session=Depends(get_db)):
    ord_item=crud.get_orderitem_by_id(db,orderitem_id)
    if ord_item is None:
        raise HTTPException(status_code=404,detail="OrderItem id not found")
    crud.delete_orderitem(db,orderitem_id)
    return {"Table":"orderitem_dataset","OrderItem Id":orderitem_id,"Message":"Successfully Deleted"}

@app.delete("/payment/{payment_id}")
def delete_payment(payment_id:int,db:Session=Depends(get_db)):
    pay=crud.get_payment_by_id(db,payment_id)
    if pay is None:
        raise HTTPException(status_code=404,detail="Payment id not found")
    crud.delete_payment(db,payment_id)
    return {"Table":"payment_dataset","Payment Id":payment_id,"Message":"Successfully Deleted"}









