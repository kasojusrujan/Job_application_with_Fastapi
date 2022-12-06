import pymongo
from enum1 import Status
from dotenv import load_dotenv
import os 

load_dotenv()
link=os.getenv("mongodb")
client=pymongo.MongoClient(link)
db =client['Job_search']
job=db['total_jobs']
applyjobs=db['applied_jobs']
login=db['login_details']
status=db['status_details']



def create_job(data):
    data=dict(data)
    job.insert_one(data)

def apply_job(data):
    data=dict(data)
    applyjobs.insert_one(data)
    status.insert_one(
        {   "name"  : data["name"],
            "status" : Status.under_process}
    )

    

