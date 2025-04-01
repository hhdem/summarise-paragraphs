# Paragraph Summarization API with Azure OpenAI

This is a Python Flask API that uses Azure OpenAI Service to summarize paragraphs of text. The API is designed to be accessible externally while maintaining data privacy through Azure's enterprise-grade security.

## Features

- Summarize paragraphs using Azure OpenAI Service
- Enhanced data privacy and security through Azure
- Simple web interface for testing
- RESTful API endpoint for integration with other applications
- CORS enabled for cross-origin requests

## Prerequisites

- Python 3.6 or higher
- Azure subscription
- Azure OpenAI Service resource

## Installation

1. Clone this repository:
   ```
   git clone <repository-url>
   cd summarise-paragraphs
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your Azure OpenAI Service:
   - Create an Azure OpenAI resource in the Azure portal
   - Deploy a model in your Azure OpenAI resource
   - Rename `.env.example` to `.env` (if it exists)
   - Edit the `.env` file and update the following values:
     - `AZURE_OPENAI_ENDPOINT`: Your Azure OpenAI endpoint URL
     - `AZURE_OPENAI_API_KEY`: Your Azure OpenAI API key
     - `AZURE_OPENAI_DEPLOYMENT_NAME`: The name of your model deployment

## Running the Application

Run the application with:

```
python app.py
```

The server will start on port 5000 by default (you can change this in the `.env` file).

- Web interface: http://localhost:5000/
- API endpoint: http://localhost:5000/api/summarize

## API Usage

### Summarize Text

**Endpoint:** `POST /api/summarize`

**Request Body:**
```json
{
  "text": "Your paragraph to summarize goes here. It can be a long text that you want to get a concise summary of."
}
```

**Response:**
```json
{
  "summary": "Concise summary of the provided text."
}
```

**Example using cURL:**
```bash
curl -X POST http://localhost:5000/api/summarize \
  -H "Content-Type: application/json" \
  -d '{"text":"Your paragraph to summarize goes here."}'
```

**Example using JavaScript:**
```javascript
fetch('http://localhost:5000/api/summarize', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({ text: 'Your paragraph to summarize goes here.' }),
})
.then(response => response.json())
.then(data => console.log(data.summary));
```

## Setting Up Azure OpenAI Service

1. **Create an Azure Account**:
   - If you don't have an Azure account, sign up at [azure.microsoft.com](https://azure.microsoft.com)

2. **Request Access to Azure OpenAI Service**:
   - Azure OpenAI Service requires approval. Apply for access at [azure.microsoft.com/products/cognitive-services/openai-service](https://azure.microsoft.com/products/cognitive-services/openai-service)

3. **Create an Azure OpenAI Resource**:
   - In the Azure portal, create a new Azure OpenAI resource
   - Select your subscription, resource group, region, and name
   - Choose a pricing tier (typically starting with Standard)

4. **Deploy a Model**:
   - In your Azure OpenAI resource, go to "Model Deployments"
   - Create a new deployment
   - Select a model (e.g., gpt-35-turbo or gpt-4)
   - Note the deployment name for your `.env` file

5. **Get Your API Keys and Endpoint**:
   - In your Azure OpenAI resource, go to "Keys and Endpoint"
   - Copy Key 1 or Key 2 for your `AZURE_OPENAI_API_KEY`
   - Copy the endpoint for your `AZURE_OPENAI_ENDPOINT`

## Making the API Accessible Externally

To make the API accessible externally while maintaining security, you have several options:

### 1. Using ngrok (for development/testing)

[ngrok](https://ngrok.com/) creates a secure tunnel to your localhost. Install ngrok and run:

```bash
ngrok http 5000
```

This will give you a public URL that forwards to your local server.

### 2. Deploying to a Cloud Provider

For production use, deploy the application to a cloud provider:

#### Heroku
```bash
# Install Heroku CLI and login
heroku create your-app-name
git push heroku main
```

#### AWS, Google Cloud, or Azure
Follow the respective platform's instructions for deploying Flask applications.

### 3. Self-hosting

If you have a server with a public IP:

1. Deploy the application to your server
2. Configure your firewall to allow traffic on port 5000 (or your chosen port)
3. Set up a reverse proxy (like Nginx) to forward requests to your Flask application
4. Consider setting up HTTPS for secure connections

## Security and Privacy Considerations

- Keep your Azure OpenAI API key secure and never expose it in client-side code
- Azure OpenAI Service provides additional security features:
  - Data residency in your chosen Azure region
  - No data used for model training (unless explicitly opted in)
  - Compliance with Azure's security and privacy standards
  - Integration with Azure Active Directory for authentication
  - Network isolation options with Virtual Networks
- Consider implementing rate limiting to prevent abuse
- Add authentication if the API will be used in a production environment
- Use HTTPS for all external access to protect data in transit

## License

[MIT License](LICENSE)
