# Azure OpenAI Service Setup Guide

This guide will help you set up Azure OpenAI Service and integrate it with our paragraph summarization API.

## Step 1: Get Access to Azure OpenAI Service

1. Ensure you have a valid Azure subscription
2. Visit [Azure OpenAI Service Access Request](https://aka.ms/oai/access) to fill out the application form
3. Wait for approval (typically takes a few days to weeks)

## Step 2: Create an Azure OpenAI Resource

1. Log in to the [Azure Portal](https://portal.azure.com/)
2. Click "Create a resource"
3. Search for "Azure OpenAI"
4. Click "Create"
5. Fill in the following information:
   - Subscription: Choose your Azure subscription
   - Resource group: Create a new one or select an existing one
   - Region: Select a region that supports Azure OpenAI
   - Name: Specify a unique name for your resource
   - Pricing tier: Choose a pricing tier that suits your needs
6. Click "Review + create", then "Create"

## Step 3: Deploy a Model

1. In the Azure Portal, navigate to your newly created Azure OpenAI resource
2. In the left menu, click "Model deployments"
3. Click "Create new deployment"
4. Select a model (e.g., gpt-35-turbo or gpt-4)
5. Specify a name for your deployment (this will be your `AZURE_OPENAI_DEPLOYMENT_NAME`)
6. Click "Create"

## Step 4: Get API Keys and Endpoint

1. In the Azure Portal, navigate to your Azure OpenAI resource
2. In the left menu, click "Keys and Endpoint"
3. Copy "Key 1" or "Key 2" (this will be your `AZURE_OPENAI_API_KEY`)
4. Copy the "Endpoint" (this will be your `AZURE_OPENAI_ENDPOINT`)

## Step 5: Configure Your Application

1. Open the `.env` file in your project
2. Update the following environment variables:
   ```
   AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
   AZURE_OPENAI_API_KEY=your_azure_openai_api_key_here
   AZURE_OPENAI_DEPLOYMENT_NAME=your_deployment_name_here
   ```

## Step 6: Run Your Application

1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Start the application:
   ```
   python app.py
   ```

3. Access the web interface at http://localhost:5000/

## Step 7: Test the API

You can test the API using the web interface or the provided `test_api.py` script:

```
python test_api.py "Your text to summarize goes here."
```

## Troubleshooting

### Common Issues

1. **Authentication Error**: Ensure your API key is correct and properly formatted in the `.env` file.

2. **Deployment Not Found**: Verify that your `AZURE_OPENAI_DEPLOYMENT_NAME` matches exactly the name you gave your model deployment in the Azure Portal.

3. **Region Availability**: If you encounter errors about model availability, try deploying in a different Azure region.

4. **Rate Limiting**: Azure OpenAI Service has rate limits. If you're making too many requests, you might be temporarily rate-limited.

### Getting Help

- Check the [Azure OpenAI Service Reference Documentation](AZURE_OPENAI_REFERENCE.md) for more information
- Visit the [Azure OpenAI Service documentation](https://learn.microsoft.com/en-us/azure/ai-services/openai/) for official guidance
- For issues specific to this application, check the project's README or open an issue in the repository

## Next Steps

- Consider implementing authentication for your API
- Set up monitoring for your Azure OpenAI usage
- Explore other Azure OpenAI models and features
- Optimize your prompts for better summarization results
