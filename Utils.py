def getFacultywiseDepartments():
    depts=open("templates/includes/depatments.txt").read().split("#")
    l=list()
    for d in depts:
        x=d.split("\n")
        l.append((x[0].strip(),[y.strip() for y in x[1:] if y!=""]))
    return dict(l)