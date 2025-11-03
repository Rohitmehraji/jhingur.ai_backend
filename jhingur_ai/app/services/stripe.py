import stripe
from app.core.config import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

def create_charge(amount: int, currency: str, source: str):
    charge = stripe.Charge.create(
        amount=amount,
        currency=currency,
        source=source,
    )
    return charge
