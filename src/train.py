import openai
import json
import wandb
from config import OPENAI_API_KEY, WANDB_API_KEY 

# Load your API key from an environment variable or secret management service
openai.api_key = OPENAI_API_KEY

# Initialize W&B
wandb.login(key=WANDB_API_KEY)
wandb.init(project="your-wandb-project-name", name="fine-tuning-gpt-3.5")

def fine_tune_model():
    # Upload the file
    json_response = openai.File.create(
        file=open("B:/ai/tulearn/src/app/data/data_science_faq.jsonl", "rb"),
        purpose='fine-tune'
    )

    # Access the file ID
    file_id = json_response['id'] # type: ignore

    # Create the fine-tuning job
    fine_tune_response = openai.FineTuningJob.create(
        training_file=file_id,
        model="gpt-3.5-turbo"
    )

    fine_tune_id = fine_tune_response['id'] # type: ignore
    
    # Log the fine-tuning job details to W&B
    wandb.log({"fine_tune_id": fine_tune_id})
    
    return fine_tune_id

if __name__ == "__main__":
    fine_tune_id = fine_tune_model()
    print(f"Fine-tuning job created with ID: {fine_tune_id}")
