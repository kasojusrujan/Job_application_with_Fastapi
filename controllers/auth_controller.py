from auth import AuthHandler
from fastapi import HTTPException
from enum1 import role
import db
import models.auth_model as auth_model
from enum1 import role
import re

auth_handler = AuthHandler()


class auth_role():
    role=" "
    token=''
    data={}


class auth_controller():
    users=[]
    def auth_register(auth_details):
        users=auth_controller.users
        if any(x['username'] == auth_details.username for x in users):
            raise HTTPException(status_code=400, detail='Username is taken')
        hashed_password = auth_handler.get_password_hash(auth_details.password)
        if role['HR'].value==auth_details.role or role['Candidate'].value==auth_details.role:
            n=auth_details.phone
            pattern=re.compile("^[6-9][0-9]{9}$")
            if(pattern.match(n)):
                users.append({
                'username': auth_details.username,
                'password': hashed_password,
                "role" : auth_details.role,
                "fullname" : auth_details.fullname,
                "phone" : auth_details.phone
                })
            else:
                raise HTTPException(status_code=400, detail="Enter Valid 10 digit Number")
        
        else :
            raise HTTPException(status_code=400, detail='Role you have selected is not coorect (OR) use only small letters')
        db.login.insert_one(dict(users[len(users)-1]))

    def auth_login(auth_details):
        user = None
        users=auth_model.login(db.login.find())
        for a in users:
            del a['id']
    
        for x in users:
            if x['username'] == auth_details.username:
                user = x
                break
    
        if (user is None) or (not auth_handler.verify_password(auth_details.password, user['password'])):
            raise HTTPException(status_code=401, detail='Invalid username and/or password')
        auth_role.token = auth_handler.encode_token(user['username'])
        b=user['username']
        a=auth_model.registerdatas(db.login.find({ 'username' : b}))
        auth_role.data=a
        auth_role.role=(a[0]['role'])
        