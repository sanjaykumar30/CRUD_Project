from . import models, schemas
from sqlalchemy.orm import Session

#Get request
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

#Post request

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

#Put request

def update_customer(db:Session,customer:schemas.Customer):
    cus=get_customer_by_id(db,customer.customer_id)
    cus.customer_id=customer.customer_id
    cus.customer_city=customer.customer_city
    cus.customer_zip_code=customer.customer_zip_code
    cus.customer_state=customer.customer_state
    db.commit()
    db.refresh(cus)
    return cus
 


def update_order(db:Session,order:schemas.Order):
    ord=get_order_by_id(db,order.order_id)
    ord.order_id=order.order_id
    ord.customer_id=order.customer_id
    ord.order_status=order.order_status
    ord.order_approved_timestamp=order.order_approved_timestamp
    ord.order_delivered_customer_date=order.order_delivered_customer_date
    ord.order_estimated_delivery_date=order.order_estimated_delivery_date
    ord.order_purchase_timestamp=order.order_purchase_timestamp
    db.commit()
    db.refresh(ord)
    return ord

def update_product(db:Session,product:schemas.Product):
    prod=get_product_by_id(db,product.product_id)
    prod.product_id=product.product_id
    prod.product_category_name=product.product_category_name
    prod.product_description_length=product.product_description_length
    prod.product_weight_g=product.product_weight_g
    prod.product_height_cm=product.product_height_cm
    prod.product_name_length=product.product_name_length
    prod.product_length_cm=product.product_length_cm
    prod.product_width_cm=product.product_width_cm
    db.commit()
    db.refresh(prod)
    return prod

def update_orderitem(db:Session,orderitem:schemas.OrderItem):
    ord_item=get_orderitem_by_id(db,orderitem.orderitem_id)
    ord_item.order_id=orderitem.order_id
    ord_item.orderitem_id=orderitem.orderitem_id
    ord_item.product_id=orderitem.product_id
    ord_item.shipping_limit_date=orderitem.shipping_limit_date
    ord_item.price=orderitem.price
    ord_item.freight_value=orderitem.freight_value
    db.commit()
    db.refresh(ord_item)
    return ord_item

def update_payment(db:Session,payment:schemas.Payment):
    pay=get_payment_by_id(db,payment.payment_id)
    pay.payment_id=payment.payment_id
    pay.order_id=payment.order_id
    pay.payment_sequential=payment.payment_sequential
    pay.payment_type=payment.payment_type
    pay.payment_instalments=payment.payment_instalments
    pay.payment_value=payment.payment_value
    db.commit()
    db.refresh(pay)
    return pay


#Delete request

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
    db.commit()


 

    
