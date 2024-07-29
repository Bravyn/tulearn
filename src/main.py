import openai
from flask import Flask, request, jsonify
from config import OPENAI_API_KEY

# Load your API key from an environment variable or secret management service
openai.api_key = OPENAI_API_KEY

app = Flask(__name__)

# Function to retrieve fine-tuning job details (optional)
def get_fine_tune_job_details(fine_tune_id):
    return openai.FineTuningJob.retrieve(fine_tune_id)

# Endpoint for inference
@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Marv is a factual chatbot that is also sarcastic."},
            {"role": "user", "content": user_message}
        ]
    )

    response_message = completion.choices[0].message['content']
    return jsonify({"response": response_message})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
