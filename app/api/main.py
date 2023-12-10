from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.api.exceptions import SQLAlchemyException
from app.api.user import router as user_router
from sqlalchemy.exc import SQLAlchemyError

app = FastAPI()
app.include_router(user_router)


@app.exception_handler(SQLAlchemyError)
async def sql_alchemy_exception_handler(request: Request, exc: SQLAlchemyError):
    status_code = SQLAlchemyException.status_code(exc)
    return JSONResponse(status_code=status_code, content={"detail": str(exc)})


@app.get("/")
async def root():
    return {"message": "Welcome to slots"}