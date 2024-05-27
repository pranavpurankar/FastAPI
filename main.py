from fastapi import FastAPI,Response,status,HTTPException
# from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional     #This for optional field see class BaseModel
from random import randrange


app = FastAPI()

# Pydantic validation base class what kind of data send to us
class Post(BaseModel):
    title: str
    content: str
    published: bool=True    #optional field if user didn't provided default=True
    rating: Optional[int]=None #Totaly optional field no default value

# global_variable to store posts
# we're hard-coding post params; bcz whenever we shutdown our program it is everything
# gets vanished that is why I am doing below things keep mind once db attach best
# practises will be started. Right now we're keeping things at simple level

my_posts = [{"title": "title of post of 1","content":"content of post 1","id":1},
{"title": "favorite foods", "content":"I like karela","id":2}]

def find_post(id):
    for post in my_posts:
        if post["id"] == id:
            return post

# Part_1: Initial setup and GET_Request

@app.get("/")
def root():
    return {"message":"Welcome to my API"}

@app.get("/posts")
def get_post():
    return {'data':my_posts}
'''
# Path_Operation: 
One thing to keep in mind that whenever we provide same path/url FastApi will
execute the first match. It means order does matter.
'''
# ================ Covered 1 Hour/ Completed Get_reqst and path_oepration ===

# Part_2: POST_request and data retrieval
'''
Imported body from fastapi.params to retrieve data
1. Create a post request at path /createposts
2. Inside body option postman created a JSON data
3. Retieval is done through property payLoad var -> printed payLoad
'''
# @app.post("/createposts")
# def create_posts(payLoad:dict=Body(...)):
#     print(payLoad)
#     return {"new_post":f"title: {payLoad['title']} content: {payLoad['content']}"}

'''
Why we need schema (I am performing operation using body is good for learning)
• It's pain to get all the values from the body
• The client can send whatever data they want
• The data isn't getting validated
• We ultimatetly want to force the client to send data in a schema that we expect

=> Pydantic (not specific to fastAPI can used with other python libraries)
Pydantic Pydantic is a Python library for data validation, serialization, 
and documentation (using JSON Schema) based on Python type hints. It is designed 
to simplify the process of creating and validating data models, and to make it 
easier to share and reuse those models.
'''
# Now using pydantic we've data validation and re-creating the createposts
@app.post("/posts")
def create_posts(post:Post):
    post_dict = post.dict()
    post_dict['id']=randrange(0,100000000) 
    my_posts.append(post_dict)
    return {"data":post_dict}

'''
In the real application we store data in the database right now we're not ready
for that. So storing our data in the global variable, called "my_posts" an array
This array stores a whole bunch of options, and inside it is a dictonary
'''

# Functionality for retrieving the single post (it is singular-> get_post)
# This {id} represents the path parameter
# We should manipulate the response 
'''
@app.get("/posts/{id}")
def get_post(id:int,response:Response):
    post = find_post(id)
    if not post:
        response.status_code=status.HTTP_404_NOT_FOUND
        return {'Message':f'post with id: {id} was not found'}
    return {"post_detail":post}

'''
# Instead of doing it like above we can do it little bit cleaner for above & below 
# we have imported Response,status,HTTPException modules

@app.get("/posts/{id}")
def get_post(id:int):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"post with id: {id} was not found")
    return {"post_detail":post}

# Checking whether I am in a virtual environment
import sys # noqa: E402
if sys.prefix != sys.base_prefix:
    print("You're in a virtual environment")
else:
    print("Not in Virtual Enviroment")
