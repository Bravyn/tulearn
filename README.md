# Tulearn
Teaching kids how to code

This project is a Flask-based web application that leverages OpenAI's GPT model to enable users learn in a fun and interactive way.
Here is a detailed `README.md` for your project:

## Introduction

### Fine-Tuned GPT-3.5 Turbo Chatbot

This project demonstrates how to fine-tune OpenAI's GPT-3.5 Turbo model on a custom dataset and deploy a Flask endpoint to serve the inference. The example provided is for a chatbot named "Marv," which is factual and sarcastic.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Training the Model](#training-the-model)
  - [Starting the Flask Server](#starting-the-flask-server)
  - [Using the Endpoint](#using-the-endpoint)
- [Configuration](#configuration)
- [Contribution](#contribution)
- [License](#license)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/fine-tuned-gpt3.5-chatbot.git
   cd fine-tuned-gpt3.5-chatbot
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your OpenAI API key:
   - Create a file named `config.py` in the project root directory.
   - Add your OpenAI API key to the file:
     ```python
     OPENAI_API_KEY = 'your-openai-api-key'
     ```

## Usage

### Training the Model

1. Prepare your dataset in JSONL format. Ensure it is located at `B:/ai/tulearn/src/app/data/data_science_faq.jsonl`.

2. Run the training script:
   ```bash
   python train.py
   ```

3. The script will upload the dataset and create a fine-tuning job. The job ID will be printed in the console.

### Starting the Flask Server

1. Ensure the fine-tuning process is complete and the model is ready for inference.

2. Start the Flask server:
   ```bash
   python main.py
   ```

3. The server will start on `http://0.0.0.0:5000`.

### Using the Endpoint

You can now send POST requests to `http://localhost:5000/chat` with a JSON payload containing the user's message. For example:
```json
{
  "message": "What's the capital of France?"
}
```

The server will respond with the chatbot's reply.

## Configuration

Ensure you have a `config.py` file with your OpenAI API key:
```python
OPENAI_API_KEY = 'your-openai-api-key'
```

## Contribution

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
   ```bash
   git checkout -b feature-name
   ```
3. Make your changes and commit them with descriptive messages.
4. Push your changes to your forked repository.
   ```bash
   git push origin feature-name
   ```
5. Create a pull request to the main repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.



### `requirements.txt`
Make sure you have a `requirements.txt` file that includes the necessary dependencies:

```plaintext
openai==
flask
```

This `README.md` provides a comprehensive guide to installing, configuring, and using your project, as well as instructions for contributing and information about the license.