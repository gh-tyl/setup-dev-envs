from fastapi import FastAPI

# from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

# # CORSを回避
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


@app.get("/")
async def root():
    return {"message": "Hello World"}
