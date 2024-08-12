from openai import OpenAI
from pymongo import MongoClient

# MongoDB Client
mongo_client = MongoClient('mongodb://localhost:27017/')
db = mongo_client['mongodb_name']
orders_collection = db['collection_name'] 

# OpenAI API Client
client = OpenAI(api_key='api-key') 

def parse_order_text(order_text):
    prompt = f"Extract the order details from the following text and format it as JSON:\n\n{order_text}\n\n"

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    # Correctly access the message content
    structured_data = response.choices[0].message.content.strip()
    return eval(structured_data)  

def insert_order_to_mongo(order_data):
    orders_collection.insert_one(order_data)  
    print(f"Order inserted into MongoDB with ID: {order_data['_id']}")

def main():
    order_text = """

    """

    
    order_data = parse_order_text(order_text)
    
    
    insert_order_to_mongo(order_data)

if __name__ == "__main__":
    main()
