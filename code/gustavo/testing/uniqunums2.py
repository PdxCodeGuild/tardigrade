def unique_in_order(iterable):
    ls=[]
    ls2=[]
    inds = len(iterable)-1
    print(inds)
    for its in iterable:
        if its not in ls:
            ls.append(its)
            print(ls)
    # for ind in str(inds):
    #     if str(ls[inds]) != str(ls)[inds+1]:
    #         ls2.append(ls[inds])
    #         print(ls2)
    
    
    return ls
    

print(unique_in_order('AABBBBCCCCCCCCCCCCDEFGHAAbBBDCC'))