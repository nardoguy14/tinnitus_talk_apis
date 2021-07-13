import stripe
import json

stripe.api_key = "sk_test_51J4YG5EtXr3xL8O5KlVhKkTEjL6MZPOkpij6GQfDtmTRGqhwMbSg3H2XjUrbuCM47MDrqAtRdmedTFlIMU6VveOv00BroWSSMl"


def create_payment(amount: float):
    try:
        intent = stripe.PaymentIntent.create(
            amount=int(amount * 100),
            currency='usd'
        )
        return {
            'clientSecret': intent['client_secret']
        }
    except Exception as e:
        print(e)