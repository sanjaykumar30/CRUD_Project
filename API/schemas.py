from pydantic import BaseModel
from datetime import datetime



class Customer(BaseModel):
    customer_id:int
    customer_zip_code:int
    customer_city:str
    customer_state:str

class Order(BaseModel):
    order_id:int
    customer_id:int
    order_status:str
    order_purchase_timestamp:datetime
    order_approved_timestamp:datetime
    order_delivered_customer_date:datetime
    order_estimated_delivery_date:datetime

class Product(BaseModel):
    product_id:int
    product_category_name:str
    product_name_length:int
    product_description_length:int
    product_weight_g:float
    product_length_cm:float
    product_height_cm:float
    product_width_cm:float

class OrderItem(BaseModel):
    order_id:int
    orderitem_id:int
    product_id:int
    shipping_limit_date:datetime
    price:float
    freight_value:float

class Payment(BaseModel):
    payment_id:int
    order_id:int
    payment_sequential:int
    payment_type:str
    payment_instalments:int
    payment_value:float




