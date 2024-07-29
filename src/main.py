# Load your API key from an environment variable or secret management service
from flask import Flask, request, jsonify
import openai
from src.config import OPENAI_API_KEY
from app.ds_data import ds_data


# Load your API key from an environment variable or secret management service
openai_api_key = OPENAI_API_KEY
if not openai_api_key:
    raise ValueError("OpenAI API key not found in environment variables.")

# Function to get completion from OpenAI's GPT model based on the query and faq_data
def get_completion(query, faq_data):
    try:
        context = "\n".join([f"Q: {item['question']}\nA: {item['answer']}\nNavigation: {item['navigation']['description']} (Path: {item['navigation']['path']})" for item in faq_data])
        messages = f"{context}\nQ: {query}\nA:"
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": messages}],  # Pass messages as a list of dictionaries
            max_tokens=150,
            temperature=0.7,
            top_p=1,
            n=1,
            stop=["\n"]
        )
        # The response object structure has changed. Access the text like this:
        return response['choices'][0]['message']['content'].strip()  # Access the text from the correct location
    except Exception as e:
        print(f"Error in get_completion: {e}")
        return None

# Function to get navigation details from faq_data based on the query
def get_navigation(query, faq_data):
    try:
        for item in faq_data:
            if item['question'].lower() in query.lower():
                return item['navigation']
        return None
    except Exception as e:
        print(f"Error in get_navigation: {e}")
        return None

# Initialize the Flask app
app = Flask(__name__)

@app.route('/chatbot', methods=['POST'])
def chatbot():
    try:
        data = request.json  # Get the JSON data from the POST request
        if not data:
            return jsonify({'error': 'Invalid input, expected JSON format'}), 400
        
        query = data.get('query')  # Extract the query from the JSON data
        if not query:
            return jsonify({'error': 'No query provided'}), 400
        
        response_text = get_completion(query, faq_data)  # Get the completion from OpenAI's GPT model
        if response_text is None:
            return jsonify({'error': 'Failed to generate response'}), 500
        
        navigation = get_navigation(query, faq_data)  # Get the navigation details
        if navigation:
            response = {
                'navigation': navigation,
                'response': response_text
            }
        else:
            response = {'response': response_text}
        
        return jsonify(response)
    
    except Exception as e:
        print(f"Error in /chatbot route: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode
