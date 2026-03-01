from fastapi import APIRouter
from core.llm_client import generate_response
from schemas.models import SymptomRequest, LabRequest, FullRequest, ResponseModel
from services.symptom_reasoning import analyze_symptoms
from services.lab_explanation import explain_labs
from services.next_steps import get_next_steps
from fastapi import APIRouter

router = APIRouter()

@router.post("/generate")
async def generate(data: dict):
    prompt = data.get("prompt", "")
    return {"response": generate_response(prompt)}

@router.post("/reasoning/symptoms", response_model=ResponseModel)
def symptoms_endpoint(req: SymptomRequest):
    result = analyze_symptoms(req.symptoms)
    return ResponseModel(result=result)

@router.post("/reasoning/labs", response_model=ResponseModel)
def labs_endpoint(req: LabRequest):
    result = explain_labs(req.labs)
    return ResponseModel(result=result)

@router.post("/reasoning/full", response_model=ResponseModel)
def full_endpoint(req: FullRequest):
    s = analyze_symptoms(req.symptoms)
    l = explain_labs(req.labs)
    n = get_next_steps(req.context)

    return ResponseModel(result=f"{s}\n\n{l}\n\n{n}")