from fastapi import APIRouter,File,UploadFile,Depends,HTTPException
import db
import models.user_model as user_model 
from schemas import apply_jobs
from controllers.auth_controller import auth_handler,auth_role
from enum1 import msg
from controllers.candidate_controller import candidate_controller

candidate_route =APIRouter(
    prefix='/candidate',
    tags=['Candidate']
)
1


@candidate_route.post("/resume")
async def resume(res : UploadFile = File(...),username=Depends(auth_handler.auth_wrapper)):
    if auth_role.role=='candidate':
        return "sucessfully resume uploaded"
    else:
        raise HTTPException(status_code=401, detail=msg['message'].value)

@candidate_route.post("/applyjob")
async def apply_job(data : apply_jobs,username=Depends(auth_handler.auth_wrapper)):
    if auth_role.role=='candidate':
        # candidate_controller.applyjob(dict(data))
        db.apply_job(data)
        return " sucessfully applied job"
    else:
        raise HTTPException(status_code=401, detail=msg['message'].value)

@candidate_route.get('/applied_jobs')
async def get_applied_jobs(username=Depends(auth_handler.auth_wrapper)):
    if auth_role.role=='candidate':
        # candidate_controller.get_applied_jobs
        b=user_model.totalappliedjobs(db.applyjobs.find())
        return b
    else:
        raise HTTPException(status_code=401, detail=msg['message'].value)


@candidate_route.get("/singlecandidate/{name}")
async def singlecandidate(name,username=Depends(auth_handler.auth_wrapper)):
    if auth_role.role=='candidate':
        # candidate_controller.singlecandidate(name)
        a =user_model.appliedjobs(db.applyjobs.find_one({"name": name}))
        return a
    else:
        raise HTTPException(status_code=401, detail=msg['message'].value)
      
@candidate_route.get("/veiwstatus/")
async def viewstatus(name,username=Depends(auth_handler.auth_wrapper)):
    if auth_role.role=='candidate':
        # candidate_controller.viewstatus(name)
        a=user_model.statusdata(db.status.find_one({"name" : name}))
        return a
    else:
        raise HTTPException(status_code=401, detail=msg['message'].value)
    


