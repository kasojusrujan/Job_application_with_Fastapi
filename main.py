from fastapi import FastAPI
from routers.auth_router import auth_route
from routers.job_router import job_route
from routers.candidate_router import candidate_route

app=FastAPI(
    title='Job Application',
    description='This is the Job application website',
)

app.include_router(auth_route)
app.include_router(job_route)
app.include_router(candidate_route)

