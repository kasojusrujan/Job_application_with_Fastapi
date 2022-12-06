from fastapi import APIRouter,Depends,HTTPException
import db
import models.user_model as user_model 
from schemas import creat_job,data
from controllers.auth_controller import auth_handler,auth_role
from enum1 import msg

job_route=APIRouter(
    prefix='/job',
    tags=['Job']
)


@job_route.post("/createjob")
async def create_job(data :creat_job,username=Depends(auth_handler.auth_wrapper)):
    if auth_role.role=="hr":
        db.create_job(data)
        return " created job"
    else:
        raise HTTPException(status_code=401, detail=msg['message'].value)
    

@job_route.get("/getalljobs")
async def get_job(username=Depends(auth_handler.auth_wrapper)):
    if auth_role.role=='hr':
        a=user_model.totaljobs(db.job.find())  
        return  a
    else:
        raise HTTPException(status_code=401, detail=msg['message'].value)

@job_route.get('/allapplies_jobs')
async def get_applied_jobs(username=Depends(auth_handler.auth_wrapper)):
    if auth_role.role=='hr':
        b=user_model.totalappliedjobs(db.applyjobs.find())
        return b
    else:
        raise HTTPException(status_code=401, detail=msg['message'].value)

@job_route.get("/single_created_job/{title}")
async def singlejob(title,username=Depends(auth_handler.auth_wrapper)):
    if auth_role.role=='hr':
        a =user_model.jobapplication(db.job.find_one({"title": title}))
        return a
    else:
        raise HTTPException(status_code=401, detail=msg['message'].value)

@job_route.put("/update/")
async def update(name, data1 :data,username=Depends(auth_handler.auth_wrapper)):
    if auth_role.role=='hr':
        db.status.find_one_and_update({"name": name}, {
        "$set": dict(data1)
        })
        return "status updated"
    else:
        raise HTTPException(status_code=401, detail=msg['message'].value)
