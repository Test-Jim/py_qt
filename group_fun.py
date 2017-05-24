__author__ = 'jzs'
def init_compute(tup_mouth,tup_all):
    bug,case,gub,score=0,0,0,0
    if tup_mouth==None:
        for index in tup_all:
            bug+=index[0]
            case+=index[1]
            gub+=index[2]
            score+=index[3]
        return str(bug),str(case),str(gub),str(score)
    else:
        for index in tup_mouth:
            bug+=index[0]
            case+=index[1]
            gub+=index[2]
        return str(bug),str(case),str(gub)
def init_compute_user(tup,flag):
    namelist=[]
    buglist,caselist,gublist,scorelist=[],[],[],[]
    for index in tup:
        namelist.append(index[0])
        buglist.append(index[1])
        caselist.append(index[2])
        gublist.append(index[3])
        scorelist.append(index[4])
    if flag==True:
        return namelist
    else:
        return buglist,caselist,gublist,scorelist

