import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI

# FastAPI app initialization
app = FastAPI(title="Mind Map Generator API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# OpenAI API configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise HTTPException(status_code=500, detail="OpenAI API key not found in environment variables")

openai_client = OpenAI(api_key=OPENAI_API_KEY)

# Pydantic model for request body
class MindMapRequest(BaseModel):
    course_title: str
    key_concepts: str
    granularity_level: str
    course_duration: str
    target_audience: str
    learning_objectives: str

# Function to call OpenAI API
def call_openai_api(prompt: str) -> str:
    try:
        response = openai_client.chat.completions.create(
            model="o1-preview",
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"OpenAI API call failed: {str(e)}")

# Function to generate mind map using OpenAI API
def generate_mindmap(request: MindMapRequest) -> str:
    prompt = f"""
    As an expert educator and curriculum designer, create a comprehensive and well-structured mind map for the course titled '{request.course_title}'. The mind map should be tailored for a {request.course_duration} course and designed for {request.target_audience}.

    Key details:
    1. Course duration: {request.course_duration}
    2. Target audience: {request.target_audience}
    3. Key concepts, themes and central ideas: {request.key_concepts}
    4. Desired level of detail: {request.granularity_level}
    5. Learning objectives: {request.learning_objectives}

    Guidelines for mind map creation:
    1. Start with the course title as the central node.
    2. Create main branches for major units or modules.
    3. For each main branch, create sub-branches for topics within that unit.
    4. Further break down topics into subtopics based on the desired level of detail ({request.granularity_level}).
    5. Ensure that the content aligns with the specified course duration and is appropriate for the target audience.
    6. Incorporate the key concepts and themes throughout the mind map.
    7. Structure the content to support the achievement of the stated learning objectives.
    8. Use concise, clear language for each node.
    9. Maintain a logical flow and hierarchy in the mind map structure.
    10. Aim for a balanced distribution of content across the main branches.

    Present the mind map in Markdown format only, without additional explanations or text. Use proper indentation to represent the hierarchy. Do not use "```markdown" tags.

    Ensure the mind map is comprehensive, accurate, and tailored to the specific course requirements provided. Only use the proper markdown format with hashes (#), etc. Don't use  "```" anywhere. Start with markdown directly without ```.
    """
    return call_openai_api(prompt)

# API endpoint to generate mind map
@app.post("/generate-mindmap/")
async def create_mindmap(request: MindMapRequest):
    try:
        markdown_content = generate_mindmap(request)
        return {"markdown": markdown_content}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to the Mind Map Generator API"}
