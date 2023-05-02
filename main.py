import os
import json
from dotenv import load_dotenv
import paypalrestsdk

load_dotenv()

PAYPAL_CLIENT_ID = os.getenv("PAYPAL_CLIENT_ID")
PAYPAL_CLIENT_SECRET = os.getenv("PAYPAL_CLIENT_SECRET")
PAYPAL_MODE = "sandbox"  # Set to "live" for production

CLIENTS_FILE = "clients.json"

# Configure the PayPal SDK
paypalrestsdk.configure({
    "mode": PAYPAL_MODE,
    "client_id": PAYPAL_CLIENT_ID,
    "client_secret": PAYPAL_CLIENT_SECRET
})

def load_clients():
    try:
        with open(CLIENTS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def create_paypal_invoice(client_email, item, quantity, price, has_tax, description):
    invoice = paypalrestsdk.Invoice({
        "merchant_info": {
            "email": "your-paypal-email@example.com"  # Replace with your PayPal email
        },
        "billing_info": [{
            "email": client_email
        }],
        "items": [{
            "name": item,
            "quantity": quantity,
            "unit_price": {
                "currency": "USD",
                "value": price
            },
            "tax_inclusive": has_tax,
            "description": description
        }],
        "note": "This is a draft invoice."
    })

    if invoice.create():
        print(f"Draft invoice created with ID: {invoice.id}")
    else:
        print(f"Error creating invoice: {invoice.error}")

def select_client():
    clients = load_clients()

    if not clients:
        print("No clients found.")
        return

    for idx, client in enumerate(clients, start=1):
        print(f"{idx}. {client['name']}")

    client_idx = int(input("Select a client by entering the number: ")) - 1
    return clients[client_idx]

def main():
    client = select_client()
    if not client:
        return

    item = input("Enter item: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))
    has_tax = input("Has tax? (yes/no): ").lower() == "yes"
    description = input("Enter description: ")

    create_paypal_invoice(client['email'], item, quantity, price, has_tax, description)

if __name__ == "__main__":
    main()
