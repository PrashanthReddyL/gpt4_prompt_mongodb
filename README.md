# Order Processing with OpenAI and MongoDB

This project demonstrates how to use OpenAI's GPT model to extract structured data from unstructured order texts and store the extracted data in a MongoDB database.

## Features

- **Order Text Parsing:** Utilizes OpenAI's GPT-4 model to parse unstructured order text and convert it into a structured JSON format.
- **MongoDB Integration:** Stores the structured order data into a MongoDB collection.

## Prerequisites

- Python 3.7+
- MongoDB installed and running locally or accessible remotely.
- OpenAI API key.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/order-processing.git
    cd order-processing
    ```

2. **Install the required Python packages:**

    ```bash
    pip install openai pymongo
    ```

3. **Set up your environment:**

    Replace `'api-key'` with your actual OpenAI API key in the code.

4. **Ensure MongoDB is running:**

    Make sure your MongoDB server is up and running on `localhost:27017` or modify the connection string in the script if it's hosted elsewhere.

## Usage

1. **Prepare your order text:**

    Replace the `order_text` variable with the text of the order you want to process.

2. **Run the script:**

    Execute the script using:

    ```bash
    python main.py
    ```

3. **Check the MongoDB collection:**

    The extracted order data will be stored in the `orders_collection` of your MongoDB database named `db`.

## Example

Here's an example of how you might structure the `order_text`:

```python
order_text = """
Customer: John Doe
Order: 2x iPhone 13, 1x MacBook Pro
Shipping Address: 123 Apple St, Cupertino, CA 95014
Payment Method: Credit Card (Visa ****1234)
"""
```

The script will parse this text and insert a JSON document into MongoDB similar to:

```json
{
    "customer": "John Doe",
    "order": [
        {"item": "iPhone 13", "quantity": 2},
        {"item": "MacBook Pro", "quantity": 1}
    ],
    "shipping_address": "123 Apple St, Cupertino, CA 95014",
    "payment_method": "Credit Card (Visa ****1234)"
}
```
