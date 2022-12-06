from pydantic import BaseModel

class AuthDetails(BaseModel):
    username: str
    password: str
    role :str
    fullname :str
    phone : str

class login(BaseModel):
    username :str
    password :str

class creat_job(BaseModel):
    title : str
    JD :str
    no_of_openings :str
    status : str 

class apply_jobs(BaseModel):
    name : str
    college:str
    education :str
    experience :str
    resume_link :str

class data(BaseModel):
    name :str
    status :str

