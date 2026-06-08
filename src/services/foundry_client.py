import os
from dotenv import load_dotenv

load_dotenv()

def get_foundry_endpoint() -> str:
    endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT")
    if not endpoint:
        raise ValueError("AZURE_AI_PROJECT_ENDPOINT is not configured.")
    return endpoint
