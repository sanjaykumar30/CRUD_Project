from . import models, schemas
from sqlalchemy.orm import Session

def get_customer_by_id(db:Session,customer_id:int):
    return db.query(models.Customer).filter(models.Customer.customer_id==customer_id).first()

def get_order_by_id(db:Session,order_id:int):
    return db.query(models.Order).filter(models.Order.order_id==order_id).first()

def get_product_by_id(db:Session,product_id:int):
    return db.query(models.Product).filter(models.Product.product_id==product_id).first()

def get_payment_by_id(db:Session,payment_id:int):
    return db.query(models.Payment).filter(models.Payment.payment_id==payment_id).first()

def get_orderitem_by_id(db:Session,orderitem_id:int):
    return db.query(models.OrderItem).filter(models.OrderItem.orderitem_id==orderitem_id).first()



def get_customers(db:Session,skip:int=0,limit:int=100):
    return db.query(models.Customer).offset(skip).limit(limit).all()

def get_products(db:Session,skip:int=0,limit:int=100):
    return db.query(models.Product).offset(skip).limit(limit).all()

def get_orders(db:Session,skip:int=0,limit:int=100):
    return db.query(models.Order).offset(skip).limit(limit).all()

def get_orderitems(db:Session,skip:int=0,limit:int=100):
    return db.query(models.OrderItem).offset(skip).limit(limit).all()

def get_payments(db:Session,skip:int=0,limit:int=100):
    return db.query(models.Payment).offset(skip).limit(limit).all()



def create_customer(db:Session,customer:schemas.Customer):
    cus=models.Customer(**customer.dict())
    db.add(cus)
    db.commit()
    db.refresh(cus)
    return cus

def create_order(db:Session,order:schemas.Order):
    ord=models.Order(**order.dict())
    db.add(ord)
    db.commit()
    db.refresh(ord)
    return ord

def create_product(db:Session,product:schemas.Product):
    prod=models.Product(**product.dict())
    db.add(prod)
    db.commit()
    db.refresh(prod)
    return prod

def create_orderitem(db:Session,orderitem:schemas.OrderItem):
    ord_item=models.OrderItem(**orderitem.dict())
    db.add(ord_item)
    db.commit()
    db.refresh(ord_item)
    return ord_item

def create_payment(db:Session,payment:schemas.Payment):
    pay=models.Payment(**payment.dict())
    db.add(pay)
    db.commit()
    db.refresh(pay)
    return pay



def update_customer(db:Session,customer:schemas.Customer):
    cus=get_customer_by_id(db,customer.customer_id)
    cus=models.Customer(**customer.dict())
    db.commit()
    db.refresh(cus)
    return cus
 


def update_order(db:Session,order:schemas.Order):
    ord=get_order_by_id(db,order.order_id)
    ord=models.Order(**order.dict())
    db.commit()
    db.refresh(ord)
    return ord

def update_product(db:Session,product:schemas.Product):
    prod=get_product_by_id(db,product.product_id)
    prod=models.Product(**product.dict())
    db.commit()
    db.refresh(prod)
    return prod

def update_orderitem(db:Session,orderitem:schemas.OrderItem):
    ord_item=get_orderitem_by_id(db,orderitem.orderitem_id)
    ord_item=models.OrderItem(**orderitem.dict())
    db.commit()
    db.refresh(ord_item)
    return ord_item

def update_payment(db:Session,payment:schemas.Payment):
    pay=get_payment_by_id(db,payment.payment_id)
    pay=models.Payment(**payment.dict())
    db.commit()
    db.refresh(pay)
    return pay




def delete_customer(db:Session,customer_id:int):
    cus=get_customer_by_id(db,customer_id)
    db.delete(cus)
    db.commit()

def delete_order(db:Session,order_id:int):
    ord=get_order_by_id(db,order_id)
    db.delete(ord)
    db.commit()

def delete_product(db:Session,product_id:int):
    prod=get_product_by_id(db,product_id)
    db.delete(prod)
    db.commit()

def delete_orderitem(db:Session,orderitem_id:int):
    ord_item=get_orderitem_by_id(db,orderitem_id)
    db.delete(ord_item)
    db.commit()

def delete_payment(db:Session,payment_id:int):
    pay=get_payment_by_id(db,payment_id)
    db.delete(pay)
    db.refresh()


 

    
