from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer, util
import torch
import re
import random

app = Flask(__name__)

# Load the Sentence Transformer model (you only need to do this once)
model = SentenceTransformer('all-mpnet-base-v2')

def get_agricultural_company_text(products=None):
    """Returns a static text with optional randomized product list."""
    base_text = """
    "Sunrise AgroTech" is a pioneering agricultural company dedicated to sustainable farming practices and innovative solutions. Located in the heart of the fertile Midwest, USA, they specialize in the development and distribution of high-yield, climate-resilient seeds, as well as providing advanced soil analysis and precision irrigation systems.

    With a commitment to empowering farmers, Sunrise AgroTech offers comprehensive consulting services, guiding them through modern agricultural techniques. Their product line includes a range of organic fertilizers and biopesticides, reflecting their dedication to environmentally friendly practices.

    Established in 1985, Sunrise AgroTech has consistently invested in research and development, leading to breakthroughs in crop management and yield optimization. They work closely with local farming communities, providing training and support to ensure the successful adoption of new technologies.

    Their mission is to enhance agricultural productivity while preserving the environment for future generations. Sunrise AgroTech believes in the power of innovation to create a sustainable and prosperous agricultural landscape.
    """

    if products:
        product_string = ", ".join(products)
        base_text = base_text.replace("organic fertilizers and biopesticides", product_string)

    return base_text

def get_random_products():
    """Generates a list of random agricultural products."""
    product_list = ["Organic Fertilizers", "Biopesticides", "Hybrid Corn Seeds", "Soybean Seed Treatments", "Precision Irrigation Kits", "Soil Moisture Sensors", "Drone Spraying Services", "Crop Yield Prediction Software", "Livestock Feed Supplements", "Tractor GPS Navigation Systems"]
    num_products = random.randint(3, 6)
    return random.sample(product_list, num_products)

def calculate_semantic_similarity(company_text, user_query):
    """Calculates the semantic similarity using Sentence Transformers."""
    embeddings1 = model.encode(company_text, convert_to_tensor=True)
    embeddings2 = model.encode(user_query, convert_to_tensor=True)
    cosine_scores = util.cos_sim(embeddings1, embeddings2)
    return cosine_scores.item()

def find_product_keywords(user_query, product_list):
    """Finds product keywords in the user query."""
    found_products = []
    for product in product_list:
        if re.search(r"\b" + re.escape(product.lower()) + r"\b", user_query.lower()):
            found_products.append(product)
    return found_products

def classify_intent(user_query):
    """Simple intent classification (replace with a trained model for better accuracy)."""
    buy_keywords = ["buy", "purchase", "order", "price", "cost"]
    for keyword in buy_keywords:
        if keyword in user_query.lower():
            return "buy"
    return "information"

def process_query(company_text, user_query, product_list):
    """Processes the user query and returns a score."""
    semantic_score = calculate_semantic_similarity(company_text, user_query)
    keyword_matches = find_product_keywords(user_query, product_list)
    intent = classify_intent(user_query)

    final_score = semantic_score

    if intent == "buy":
        final_score += 0.2  # Boost for buy intent
    if keyword_matches:
        final_score += 0.1 * len(keyword_matches)  # Boost for product matches

    return final_score, keyword_matches, intent
@app.route('/')
def test():
  return "<html><body>adfadf</body><html>"
@app.route('/query', methods=['POST'])
def handle_query():
    """Handles user queries via POST request."""
    try:
        data = request.get_json()
        user_query = data['query']

<<<<<<< HEAD
@app.route('/query', methods=['POST'])
def handle_query():
    """Handles user queries via POST request."""
    try:
        data = request.get_json()
        user_query = data['query']

        random_products = get_random_products()
        company_description = get_agricultural_company_text(random_products)

        final_score, keyword_matches, intent = process_query(company_description, user_query, random_products)

        response = {
            'user_query': user_query,
            'similarity_score': final_score,
            'keyword_matches': keyword_matches,
            'intent': intent,
            'company_description': company_description
        }
        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True) #remove debug=true when in production.
=======
        random_products = get_random_products()
        company_description = get_agricultural_company_text(random_products)

        final_score, keyword_matches, intent = process_query(company_description, user_query, random_products)

        response = {
            'user_query': user_query,
            'similarity_score': final_score,
            'keyword_matches': keyword_matches,
            'intent': intent,
            'company_description': company_description
        }
        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)}), 400

>>>>>>> 4079962f729239949ea5775d482eec8e2f5c002b
