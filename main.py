from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="MedAssist AI")
app.include_router(router)

from fastapi import FastAPI
from api.routes import router

