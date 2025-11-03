import razorpay
from app.core.config import settings

client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

def create_order(amount: int, currency: str):
    order = client.order.create(
        dict(amount=amount * 100, currency=currency)
    )
    return order
