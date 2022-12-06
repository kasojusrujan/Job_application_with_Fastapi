import db 
import models.user_model as user_model

class candidate_controller():
    def applyjob(data):
        db.apply_job(data)
    
    def get_applied_jobs():
        user_model.totalappliedjobs(db.applyjobs.find())
    
    def singlecandidate(name):
        user_model.appliedjobs(db.applyjobs.find_one({"name": name}))
    
    def viewstatus(name):
        user_model.statusdata(db.status.find_one({"name" : name}))
