import os
from google.adk.agents import Agent
from toolbox_core import ToolboxSyncClient
from google.genai import types
import warnings
import logging
# Load environment variables from .env file
from dotenv import load_dotenv

load_dotenv()

warnings.filterwarnings("ignore")
GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]
STORAGE_BUCKET = os.environ["STORAGE_BUCKET"]
GOOGLE_CLOUD_PROJECT = os.environ["GOOGLE_CLOUD_PROJECT"]
GOOGLE_CLOUD_LOCATION = os.environ["GOOGLE_CLOUD_LOCATION"]
GOOGLE_GENAI_USE_VERTEXAI=os.environ["GOOGLE_GENAI_USE_VERTEXAI"]
# CHECK_ORDER_STATUS_ENDPOINT = os.environ["CHECK_ORDER_STATUS_ENDPOINT"]
STAGING_BUCKET = "gs://" + STORAGE_BUCKET
ROOT_AGENT_NAME = "adk_renovation_agent"
PROJECT_ID = GOOGLE_CLOUD_PROJECT
staging_bucket = STAGING_BUCKET
logger = logging.getLogger(__name__)

USER_ID = "user123"
SESSION_ID = "demo"
PROPOSAL_DOCUMENT_FILE_NAME =  "proposal_document_for_user.pdf"
MODEL_NAME = "gemini-2.0-flash"
from fastapi import HTTPException
toolbox = ToolboxSyncClient("https://toolbox-686047971523.us-central1.run.app/")
get_order_status_by_name = toolbox.load_tool('get-order-data')


'''
# Root Agent Definition
'''
root_agent = Agent(
   model=MODEL_NAME,
   name=ROOT_AGENT_NAME,
   description=("Agent that finds order status for a material used in the building renovation for a home owner."),

# Instructions for intent detection: Combine guardrails string
# and the sub-agent routing instruction

   instruction=(
   """ 
    **********************************************************************************************************
    **********************************************************************************************************
    - If the user wants to know the status of order of a SPECIFIC MATERIAL or ITEM,
    then directly use the tool "get_order_status_by_name"
    to get the status of the object by contextually extracting the name of the material 
    from the user's input text. Remember the material name is used in direct comparison 
    in the database against the material_name field so make sure you extract the name 
    of the material for which the user is looking to find the status, correctly.
    **********************************************************************************************************
    **********************************************************************************************************
   """),

    generate_content_config=types.GenerateContentConfig(temperature=0.2),


    tools = [
        get_order_status_by_name
        ]
)