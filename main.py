from fastapi import FastAPI

app = FastAPI()

# Part_1: Initial setup and GET_Request

@app.get("/")
def root():
    return {"message":"Welcome to my API"}

@app.get("/post")
def get_post():
    return {'data':'This is your data'}
'''
# Path_Operation: 
One thing to keep in mind that whenever we provide same path/url FastApi will
execute the first match. It means order does matter.
'''
# ================ Covered 1 Hour/ Completed Get_reqst and path_oepration ===

# Part_2: POST_request and data retrieval

