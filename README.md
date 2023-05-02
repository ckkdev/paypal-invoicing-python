# PayPal Invoicing Python Script

This Python script allows you to create draft invoices using the PayPal API. The script prompts you to select a client, enter item details, and create an invoice. The invoice is then saved as a draft in your PayPal account.

## Setup

1. Create a `.env` file in the same directory as your script, and include your PayPal API credentials:
PAYPAL_CLIENT_ID=your_paypal_client_id
PAYPAL_CLIENT_SECRET=your_paypal_client_secret


2. Install the required packages:
pip install python-dotenv
pip install paypalrestsdk


3. Update the `CLIENTS_FILE` JSON format to include the client's name and email:
json
```
[
    {
        "id": 1,
        "name": "Client A",
        "email": "client-a@example.com"
    },
    {
        "id": 2,
        "name": "Client B",
        "email": "client-b@example.com"
    }
]
```

4. Replace your-paypal-email@example.com in the script with your actual PayPal email.

## Usage

Run the script using Python 3:

```
python invoice_script.py || py invoice_script.py
```

The script will prompt you to select a client, enter item details, and create an invoice. The invoice will be saved as a draft in your PayPal account. To view the created invoices, log in to your PayPal Developer dashboard and navigate to the sandbox account that you used for the API credentials.
