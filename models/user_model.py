def jobapplication(data) -> dict:
    return {
        "id": str(data['_id']),
        "title": data['title'],
        "JD" : data['JD'],
        "no_of_openings": data['no_of_openings'],
        "status" : data['status']
    }

def totaljobs(datas) -> list:
    return [jobapplication(data) for data in datas]

def appliedjobs(data1) -> dict:
    return {
        "id": str(data1['_id']),
        "name": data1['name'],
        "college" : data1['college'],
        "education" :data1['education'],
        "experience": data1['experience'],
        "resume_link" : data1['resume_link']
    }

def totalappliedjobs(datas) -> list:
    return [appliedjobs(data1) for data1 in datas]



def statusdata(data3) -> dict:
    return {
        "id": str(data3['_id']),
        "name" : data3['name'],
        "status": data3['status']
        
    }

def statusdatas(datas) -> list:
    return [statusdata(data3) for data3 in datas]
