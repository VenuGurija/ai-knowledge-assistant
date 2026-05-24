from fastapi import APIRouter, UploadFile, File, HTTPException, status
from app.config import settings
import os

router = APIRouter(prefix="/upload", tags=["Upload"])

@router.post("", status_code=status.HTTP_201_CREATED)
async def upload_pdf(file: UploadFile = File(...)):
    # 1. Verification Block: Enforce Content-Type / File Extension
    if not file.filename.endswith(".pdf"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Invalid file type. Only PDF documents are allowed."
        )
    
    try:
        # Resolve target storage destination using dynamic settings parameters
        file_path = os.path.join(settings.UPLOAD_DIR, file.filename)
        
        # 2. Asynchronous Streamed Write Block with Active Boundary Validation
        file_size = 0
        with open(file_path, "wb") as buffer:
            while chunk := await file.read(1024 * 64):  # Parse in optimized 64KB buffers
                file_size += len(chunk)
                if file_size > settings.max_file_size_bytes:
                    # Clean up the partial leak immediately before crashing out
                    buffer.close()
                    if os.path.exists(file_path):
                        os.remove(file_path)
                    raise HTTPException(
                        status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
                        detail=f"File size exceeds the enterprise limit of {settings.MAX_FILE_SIZE_MB}MB."
                    )
                buffer.write(chunk)
            
        return {
            "status": "success",
            "filename": file.filename,
            "saved_path": file_path,
            "message": "File successfully uploaded, validated, and staged for RAG processing."
        }
    except HTTPException as http_ex:
        raise http_ex
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"Secure file-system stream write failure: {str(e)}"
        )