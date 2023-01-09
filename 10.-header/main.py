from fastapi import FastAPI, Header

app = FastAPI()


@app.get('/')
async def get_user_agent(user_agent:None|str = Header(default=None)):
    print(user_agent)
    return {"User-Agent":user_agent}

@app.get('/token')
async def get_token(x_authorization:list[str] |None =Header(default=None)):

    print(x_authorization)
    return {"X-Authorization values":x_authorization}
