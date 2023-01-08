from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float

class Customer(Base):
    __tablename__="customer_dataset"
    customer_id=Column(Integer,primary_key=True)
    customer_zip_code=Column(Integer)
    customer_city=Column(String)
    customer_state=Column(String)

class Order(Base):
    __tablename__="order_dataset"
    order_id=Column(Integer,primary_key=True)
    customer_id=Column(Integer,ForeignKey("customer_dataset.customer_id"))
    order_status=Column(String)
    order_purchase_timestamp=Column(DateTime)
    order_approved_timestamp=Column(DateTime)
    order_delivered_customer_date=Column(DateTime)
    order_estimated_delivery_date=Column(DateTime)

class Product(Base):
    __tablename__="product_dataset"
    product_id=Column(Integer,primary_key=True)
    product_category_name=Column(String)
    product_name_length=Column(Integer)
    product_description_length=Column(Integer)
    product_weight_g=Column(Float)
    product_length_cm=Column(Float)
    product_height_cm=Column(Float)
    product_width_cm=Column(Float)

class OrderItem(Base):
    __tablename__="orderitem_dataset"
    order_id=Column(Integer,ForeignKey("order_dataset.order_id"))
    orderitem_id=Column(Integer,primary_key=True)
    product_id=Column(Integer,ForeignKey("product_dataset.product_id"))
    shipping_limit_date=Column(DateTime)
    price=Column(Float)
    freight_value=Column(Float)

class Payment(Base):
    __tablename__="payment_dataset"
    payment_id=Column(Integer,primary_key=True)
    order_id=Column(Integer,ForeignKey("order_dataset.order_id"))
    payment_sequential=Column(Integer)
    payment_type=Column(String)
    payment_instalments=Column(Integer)
    payment_value=Column(Float)

    