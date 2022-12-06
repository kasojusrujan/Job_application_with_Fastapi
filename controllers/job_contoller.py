import db
import models.user_model as user_model

class job_controller():
    def getalljobs():
        a=user_model.totaljobs(db.job.find())
    
    def getappliedjobs():
        user_model.totalappliedjobs(db.applyjobs.find())
    
    def singlejob(title):
        user_model.jobapplication(db.job.find_one({"title": title}))