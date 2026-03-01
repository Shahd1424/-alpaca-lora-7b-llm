from pydantic import BaseModel

class SymptomRequest(BaseModel):
    symptoms: dict

class LabRequest(BaseModel):
    labs: dict

class FullRequest(BaseModel):
    symptoms: dict
    labs: dict
    context: dict

class ResponseModel(BaseModel):
    result: str