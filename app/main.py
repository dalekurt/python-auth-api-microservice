from fastapi import FastAPI
from app.core import config
# from uvicorn import Config
# from uvicorn.server import Server

# app = FastAPI()
app = FastAPI(title=config.PROJECT_NAME,
              openapi_url=f"{config.API_V1_PREFIX}/openapi.json",
              version=config.VERSION,
              debug=config.DEBUG)


@app.get("/", tags=["Health check"])
async def health_check():
    return {"name": config.PROJECT_NAME,
            "type": "auth-api",
            "description": config.PROJECT_DESC,
            "documentation": "/docs",
            "version": config.VERSION}

# if __name__ == '__main__':
#     server = Server(
#         Config(
#             config.APP_MODULE,
#             host="0.0.0.0",
#             log_level="DEBUG",
#             port=3000,
#             reload=True
#         )
#     )
