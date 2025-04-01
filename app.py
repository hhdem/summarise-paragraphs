from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv
import os
from openai import AzureOpenAI

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__, static_folder='static')
CORS(app)  # Enable CORS for all routes

# Configure Azure OpenAI
client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2023-07-01-preview"  # Update to the latest version as needed
)

@app.route('/', methods=['GET'])
def home():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/summarize', methods=['POST'])
def summarize():
    try:
        data = request.get_json()
        
        if not data or 'text' not in data:
            return jsonify({"error": "Text is required"}), 400
        
        text = data['text']
        
        # Call Azure OpenAI API to summarize the text
        response = client.chat.completions.create(
            deployment_id=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes text. Provide a concise summary of the given text."},
                {"role": "user", "content": text}
            ],
            max_tokens=150,
            temperature=0.5,
        )
        
        summary = response.choices[0].message.content.strip()
        
        return jsonify({"summary": summary})
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": "Failed to summarize text"}), 500

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
