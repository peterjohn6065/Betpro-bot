from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "✅ BetPro Bot is live and running"}

def start_webserver():
    uvicorn.run(app, host="0.0.0.0", port=8080)
