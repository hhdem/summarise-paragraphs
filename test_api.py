#!/usr/bin/env python3
"""
A simple script to test the paragraph summarization API using Azure OpenAI.
Usage: python test_api.py "Your text to summarize goes here."
"""

import sys
import requests
import json

def summarize_text(text, api_url="http://localhost:5000/api/summarize"):
    """
    Send a request to the Azure OpenAI-powered summarization API and return the result.
    
    Args:
        text (str): The text to summarize
        api_url (str): The URL of the API endpoint
        
    Returns:
        str: The summarized text or error message
    """
    try:
        response = requests.post(
            api_url,
            headers={"Content-Type": "application/json"},
            data=json.dumps({"text": text})
        )
        
        if response.status_code == 200:
            return response.json()["summary"]
        else:
            return f"Error: {response.json().get('error', 'Unknown error')}"
    
    except requests.exceptions.RequestException as e:
        return f"Connection error: {str(e)}"
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    # Check if text was provided as a command-line argument
    if len(sys.argv) < 2:
        print("Please provide text to summarize.")
        print("Usage: python test_api.py \"Your text to summarize goes here.\"")
        return
    
    # Get the text from command-line arguments
    text = " ".join(sys.argv[1:])
    
    print("Sending text to API for summarization...")
    summary = summarize_text(text)
    
    print("\nSummary:")
    print("-" * 50)
    print(summary)
    print("-" * 50)

if __name__ == "__main__":
    main()
