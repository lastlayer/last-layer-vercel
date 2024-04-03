import last_layer
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from starlette.exceptions import HTTPException

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


class LLMRequest(BaseModel):
    text: str


@app.post("/scan-prompt/")
async def scan_prompt(chunk: LLMRequest) -> last_layer.RiskModel:
    try:
        result = last_layer.scan_prompt(chunk.text)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"An error occurred: {str(e)}")


@app.post("/scan-llm/")
async def scan_llm(chunk: LLMRequest) -> last_layer.RiskModel:
    try:
        result = last_layer.scan_llm(chunk.text)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"An error occurred: {str(e)}")
