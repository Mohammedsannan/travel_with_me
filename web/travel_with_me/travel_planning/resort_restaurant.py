from scipy import spatial
from travel_planning.dbconnection import *
def recommendor(id):
    stuentid=id
    q="select * from travel_planning_resorts"
    rescrs=selectall(q)
    q2="SELECT * FROM `travel_planning_userregistration` WHERE `lid_id` != "+str(stuentid)
    resusers=selectall(q2)
    crslist=[]
    for i in rescrs:
        crslist.append(str(i[0]))
    dataset=[]
    for i in resusers:
        row=[]
        crsrow=[]
        qry="SELECT `resortid_id` FROM `travel_planning_resortreviewrating` WHERE `uid_id`="+str(i[11])
        crssele=selectall(qry)
        for ii in crssele:
            crsrow.append(str(ii[0]))
        for ii in crslist:
            if ii in crsrow:
                row.append(1)
            else:
                row.append(0)
        dataset.append(row)
    qry = "SELECT `resortid_id` FROM `travel_planning_resortreviewrating` WHERE `uid_id`=" + str(id)
    crssele = selectall(qry)
    crsrow=[]
    row=[]
    for ii in crssele:
        crsrow.append(str(ii[0]))
    for ii in crslist:
        if ii in crsrow:
            row.append(1)
        else:
            row.append(0)

    print(row)
    # dataset.append(row)
    print(dataset)
    distributions = []
    for i in range(0,len(dataset)):
        sd=spatial.distance.euclidean(row,dataset[i])
        # print(sd)
        # print(i,resusers[i])
        distributions.append([sd, resusers[i][0]])
    results = [i[1] for i in sorted(distributions)[:3]]
    print(distributions)
    print(results)
    lis=[]
    for i in results:
        lis.append(str(i))
    result=','.join(lis)
    print(result)
    return result
res=recommendor(1)



