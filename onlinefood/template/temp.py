def my_req(list1,list2):
    if(len(list1) > len(list2)):
        lenghts=len(list1)
    else :
        lenghts=len(list2)
    count=0
    while count<lenghts:
        print(list1[count])
        print(list2[count])
        count+=1

list1=['a1','a2']    
list2=['b1','b2']    
my_req(list1,list2)
    