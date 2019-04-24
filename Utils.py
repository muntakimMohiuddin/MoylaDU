from firebase import firebase
firebase=firebase.FirebaseApplication('https://fir-basic-9a5d7.firebaseio.com/')
def getFacultywiseDepartments():
    depts=open("templates/includes/depatments.txt").read().split("#")
    l=list()
    for d in depts:
        x=d.split("\n")
        l.append((x[0].strip(),[y.strip() for y in x[1:] if y!=""]))
    return ( dict(l))
    return firebase.get("/Departments",None)
# def dictToList(d):
#     l=list()
#     for k,v in d.items():
#         l.append(v)
#     return l
def getHalls():
    return firebase.get("/Halls",None)
    return open("templates/includes/halls.txt").read().split("\n")
def getFaculties():
    depts=open("templates/includes/depatments.txt").read().split("#")
    l=list()
    for d in depts:
        x=d.split("\n")
        l.append((x[0].strip(),[y.strip() for y in x[1:] if y!=""]))
    return list(dict(l).keys())
    return firebase.get("/Faculties",None)
def getFacultyFromDepartment(department):
    faculties=getFacultywiseDepartments()
    for faculty,departments in faculties.items():
        if department in departments or department in short(departments):
            return faculty

def short(departments):
    l=list()
    d=list()
    for x in departments:
        try:
            l.append(x.split("Department of ")[1])
        except IndexError:
            l.append(x)
    for depts in l:
        temp=''
        for c in depts.split(" "):
            if c[0].isupper():
                temp+=c[0]
        d.append(temp)
    # print(d)
    return d
def resolve(department):
    faculties = getFacultywiseDepartments()
    for faculty, departments in faculties.items():
        if department in departments :
            return department
        elif department in short(departments):
            for i  in range(len(short(departments))):
                if department==short(departments)[i]:
                    return departments[i]
print(getFaculties())