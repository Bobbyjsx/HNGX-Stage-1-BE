from fastapi import FastAPI
import datetime

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

@app.get("/api")
async def user(slack_name: str, track: str):
    current_day = datetime.datetime.utcnow().strftime('%A')
    utc_time = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    return {
            "slack_name": f"{slack_name}",
            "current_day": current_day,
            "utc_time": utc_time,
            "track": f"{track}",
            "github_file_url": "https://github.com/Bobbyjsx/HNGX-Stage-1-BE/blob/main/main.py",
            "github_repo_url": "https://github.com/Bobbyjsx/HNGX-Stage-1-BE",
            "status_code": 200,
            }