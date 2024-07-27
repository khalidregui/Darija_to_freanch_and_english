# Darija Translator

This project is a web application that translates Darija phrases into Arabic, French, and English using the GPT-4 model. The application is built with Streamlit and uses the OpenAI API for translations.

## Prerequisites

- Python 3.7 or higher
- An OpenAI API key

## Installation

1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd <repository_name>
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    ```

3. Activate the virtual environment:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Setting Up the OpenAI API Key

1. Store your OpenAI API key in your operating system's environment variables:
    - On Windows:
        ```sh
        setx OPENAI_API_KEY "your_openai_api_key"
        ```
    - On macOS/Linux:
        ```sh
        export OPENAI_API_KEY="your_openai_api_key"
        ```

## Running the Application

1. Run the Streamlit application:
    ```sh
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501` to access the application.

## Usage

1. Enter a Darija phrase in the input box.
2. Select the target language (Arabic, French, or English).
3. Click the "Translate" button to get the translation.
