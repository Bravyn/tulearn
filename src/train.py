import openai
import json
from config import OPENAI_API_KEY

# Load your API key from an environment variable or secret management service
openai.api_key = OPENAI_API_KEY

def fine_tune_model():
    # Upload the file
    json_response = openai.File.create(
        file=open("D:/tulearn/tulearn/src/app/data/data_science_faq.jsonl", "rb"),
        purpose='fine-tune'
    )

    # Access the file ID
    file_id = json_response['id']

    # Create the fine-tuning job
    fine_tune_response = openai.FineTuningJob.create(
        training_file=file_id,
        model="gpt-3.5-turbo"
    )

    fine_tune_id = fine_tune_response['id']
    return fine_tune_id

if __name__ == "__main__":
    fine_tune_id = fine_tune_model()
    print(f"Fine-tuning job created with ID: {fine_tune_id}")
