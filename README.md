# Tulearn
Teaching kids how to code


This project is a Flask-based web application that leverages OpenAI's GPT model to enable users learn in a fun and interactive way.

## Table of Contents

- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Configuration](#configuration)
- [FAQ Data Structure](#faq-data-structure)
- [License](#license)

## Getting Started

These instructions will help you set up and run the project on your local machine for development and testing purposes.

### Prerequisites

- Python 3.7 or higher
- An OpenAI API key
- Flask

### Project Directory Structure

Here's the markdown format of the project directory structure:

```markdown
# Project Directory Structure

![directory structure](data/directory-structure.png)

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/tulearn.git
    cd tulearn
    ```

2. Create and activate a virtual environment:
    ```sh
    virtualenv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

### Configuration

1. Add your OpenAI API key in a `.env` file:
    ```python
    OPENAI_API_KEY = 'your-openai-api-key'
    ```

2. Define your Data Science data in a `ds_data.py` file:
    ```python
    ds_data = [
        {
            'question': 'How do I reset my password?',
            'answer': 'To reset your password, click on the "Forgot password" link on the login page and follow the instructions.'
        },
        # Add more data as needed
    ]
    ```

## Usage

1. Run the Flask application:
    ```sh
    python app.py
    ```

2. The application will start on `http://127.0.0.1:5000/`.

### API Endpoints

#### `/chatbot`

- **Method:** `POST`
- **Description:** This endpoint accepts a user's query and returns the response generated by the OpenAI GPT model along with navigation details if available.

- **Request Body:**
    ```json
    {
        "query": "Your question here"
    }
    ```

- **Response:**
    ```json
    {
        "response": "The answer to your question"
    }
    ```

## Data Structure

The FAQ data should be structured as a list of dictionaries, where each dictionary contains the following keys:

- `question`: The question.
- `answer`: The corresponding answer to the question.

Example:
```python
ds_data = [
    {
        'question': 'How do I reset my password?',
        'answer': 'To reset your password, click on the "Forgot password" link on the login page and follow the instructions.'
    },
    # Add more data as needed
]
