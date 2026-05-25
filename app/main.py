from fastapi import FastAPI
from app.routes.upload import router as upload_router
from app.config import settings

# Initialize application instance bound strictly to centralized configurations
app = FastAPI(title=settings.APP_TITLE, debug=settings.DEBUG)

# Register our operational sprint endpoints (File upload & text chunker)
app.include_router(upload_router)

@app.get("/")
def home():
    return {"message": "AI Knowledge Assistant API Sandbox Running"}

@app.get("/health")
def health():
    return {"status": "healthy"}