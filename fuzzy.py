
def fuzzificationFollower(list,x1,x2,i):
    follower = []
    if list[i][1] <=x1[1]:
        a="Average"
        miux1=1
        follower.append(a)
        follower.append(miux1)
    elif list[i][1] >=x2[2]:
        a="High"
        miux1=1
        follower.append(a)
        follower.append(miux1)
    elif list[i][1] > x1[1] and list[i][1]<=x2[1]:
        a="Average"
        miux1=((x1[2]- list[i][1])/(x1[2]-x1[1])) 
        follower.append(a)
        follower.append(miux1)
    elif list[i][1] <= x2[2] and list[i][1]>x1[2]:
        a="High"
        miux1=((list[i][1]-x2[1])/(x2[2]-x2[1]))
        follower.append(a)
        follower.append(miux1)
    else:
        a="Average"
        b="High"
        miux1=((x1[2]- list[i][1])/(x1[2]-x1[1])) 
        miux2=((list[i][1]-x2[1])/(x2[2]-x2[1]))
        follower.append(a)
        follower.append(miux1)
        follower.append(b)
        follower.append(miux2)
    return follower
 
def fuzzificationEngagement(list,x3,x4,i):
    engagement = []
    if list[i][2] <=x3[1]:
        a="Average"
        miux1=1
        engagement.append(a)
        engagement.append(miux1)

    elif list[i][2] >=x4[2]:
        a="High"
        miux1=1
        engagement.append(a)
        engagement.append(miux1)

    elif list[i][2] > x3[1] and list[i][2]<=x4[1]:
        a="Average"
        miux1=((x3[2]- list[i][2])/(x3[2]-x3[1])) 
        engagement.append(a)
        engagement.append(miux1)
    elif list[i][2] <= x4[2] and list[i][2]>x3[2]:
        a="High"
        miux1=((list[i][2]-x4[1])/(x4[2]-x4[1]))
        engagement.append(a)
        engagement.append(miux1)
    else:
        a="Average"
        b="High"
        miux1=((x3[2]- list[i][2])/(x3[2]-x3[1])) 
        miux2=((list[i][2]-x4[1])/(x4[2]-x4[1]))
        engagement.append(a)
        engagement.append(miux1)
        engagement.append(b)
        engagement.append(miux2)
    return engagement

def inference(list1,list2,p):
    follower = list1
    engagement = list2
    fuzzy = []
    for h in range(int(len(follower[p])/ 2)): 
        k=0
        a=0
        for i in range(int(len(engagement[p])/2)):
            if follower[p][a]== "Average" and engagement[p][k]=="Average":
                fuzzy.append("Nano")
                if follower[p][a+1]>engagement[p][k+1]:
                    fuzzy.append(engagement[p][k+1])
                else:
                    fuzzy.append(follower[p][a+1])
            elif follower[p][a]== "Average" and engagement[p][k]=="High":
                fuzzy.append("Micro")
                if follower[p][a+1]>engagement[p][k+1]:
                    fuzzy.append(engagement[p][k+1])
                else:
                    fuzzy.append(follower[p][a+1])                    
            elif follower[p][a]== "High" and engagement[p][k]=="Average":
                fuzzy.append("Micro")
                if follower[p][a+1]>engagement[p][k+1]:
                    fuzzy.append(engagement[p][k+1])
                else:
                    fuzzy.append(follower[p][a+1])  
            elif follower[p][a]== "High" and engagement[p][k]=="High":
                fuzzy.append("Medium")
                if follower[p][a+1]>engagement[p][k+1]:
                    fuzzy.append(engagement[p][k+1])
                else:
                    fuzzy.append(follower[p][a+1]) 
            k=2
        a=2
    return fuzzy  

def Disconjunction(list1,p):
    fuzzy = list1
    kelayakan = []
    k=0
    if len(fuzzy[p]) == 2:
        kelayakan.append(fuzzy[p][0])
        kelayakan.append(fuzzy[p][1])
    elif len(fuzzy[p]) == 8:
        l=0
        for i in range(int(len(fuzzy[p])/ 2)):
            m=0
            for j in range(4-(l+1)):
                if fuzzy[p][l]==fuzzy[p][m+2]:
                    if fuzzy[p][l+1]>fuzzy[p][m+3]:
                        kelayakan.append(fuzzy[p][l])
                        kelayakan.append(fuzzy[p][l+1])
                    else:
                        kelayakan.append(fuzzy[p][m+2])
                        kelayakan.append(fuzzy[p][m+3])
                m=m+2   
            l=l+1
    elif len(fuzzy[p])==4:
        if fuzzy[p][0]==fuzzy[p][2]:
            if fuzzy[p][1]>fuzzy[p][3]:
                kelayakan.append(fuzzy[p][0]) 
                kelayakan.append(fuzzy[p][1]) 
            else:
                kelayakan.append(fuzzy[p][2]) 
                kelayakan.append(fuzzy[p][3])
        else:
            kelayakan.append(fuzzy[p][0]) 
            kelayakan.append(fuzzy[p][1])
            kelayakan.append(fuzzy[p][2]) 
            kelayakan.append(fuzzy[p][3])               
    return kelayakan

def Defuzzyfication(list1,i):
    y=[]
    kelayakan=list1
    if len(kelayakan[i])==2:
        if(kelayakan[i][0]=="Nano"):
            temp=(kelayakan[i][1]*100)/(4*kelayakan[i][1])
        elif(kelayakan[i][0]=="Micro"):
            temp=(kelayakan[i][1]*330)/(6*kelayakan[i][1])   
        else:
            temp=(kelayakan[i][1]*340)/(4*kelayakan[i][1])  
    elif len(kelayakan[i])==4:
        if(kelayakan[i][0]=="Nano" and kelayakan[i][2]=="Micro"):
            temp=((kelayakan[i][1]*100)+(kelayakan[i][3]*330))/((4*kelayakan[i][1])+(6*kelayakan[i][3]))
        elif(kelayakan[i][0]=="Nano" and kelayakan[i][2]=="Medium"):
            temp=((kelayakan[i][1]*100)+(kelayakan[i][3]*340))/((4*kelayakan[i][1])+(4*kelayakan[i][3]))
        elif(kelayakan[i][0]=="Micro" and kelayakan[i][2]=="Nano"):
            temp=((kelayakan[i][1]*330)+(kelayakan[i][3]*100))/((6*kelayakan[i][1])+(4*kelayakan[i][3]))
        elif(kelayakan[i][0]=="Medium" and kelayakan[i][2]=="Nano"):
            temp=((kelayakan[i][1]*340)+(kelayakan[i][3]*100))/((4*kelayakan[i][1])+(4*kelayakan[i][3]))
        elif(kelayakan[i][0]=="Medium" and kelayakan[i][2]=="Micro"):
            temp=((kelayakan[i][1]*340)+(kelayakan[i][3]*330))/((4*kelayakan[i][1])+(6*kelayakan[i][3]))
        elif(kelayakan[i][0]=="Micro" and kelayakan[i][2]=="Medium"):
            temp=((kelayakan[i][1]*330)+(kelayakan[i][3]*340))/((6*kelayakan[i][1])+(4*kelayakan[i][3]))
    y.append(temp)
    return y

def main():
    import os
    import pandas as pd
    import matplotlib.pyplot as plt 
    follower=[]
    engagement=[]
    fuzzy = []
    kelayakan = []
    y=[]
    x1 = [0,15000,75000,100000] 
    y1 = [1,1,0,0] 
    x2 = [0,15000,80000,100000] 
    y2 = [0,0,1,1]  

    x3 = [0,1,7,10] 
    y3 = [1,1,0,0] 
    x4 = [0,2,8,10] 
    y4 = [0,0,1,1] 

    x5 = [0,30,40,100]
    y5 = [1,1,0,0]
    x6 = [0,30,41,70,80,100]
    y6 = [0,0,1,1,0,0]
    x7 = [0,70,80,100]
    y7 = [0,0,1,1]

    df = pd.read_csv(os.path.join(os.path.dirname(__file__), "../41INT01_1301170493/influencers.csv"))
    list1=df.values.tolist()
    for i in range(len(list1)):
        follower.append(fuzzificationFollower(list1,x1,x2,i))
        engagement.append(fuzzificationEngagement(list1,x3,x4,i))
    for j in range(len(follower)):
        fuzzy.append(inference(follower,engagement,j))
    for k  in range(len(fuzzy)):
        kelayakan.append(Disconjunction(fuzzy,k))
    for l in range(len(kelayakan)):
        y.append(Defuzzyfication(kelayakan,l))
    for m in range(len(y)):
        df.loc[[m],'Eligibility'] = y[m]
    a=df.nlargest(20, ['Eligibility'])
    a.to_csv(os.path.join(os.path.dirname(__file__), "../41INT01_1301170493/chosen.csv"))

main()