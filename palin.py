leap=[]
nonleap=[]
count=0
nlmonth=[31,28,31,30,31,30,31,31,30,31,30,31]
lmonth=[31,29,31,30,31,30,31,31,30,31,30,31]
leap_year=[]
nonleap_year=[]
#in the below for loop the parameters are the start year and end year
for i in range(1901,2000):
    if i % 4 == 0 and i %100 != 0 or i % 400 == 0:
         leap.append(i)
    else:
         nonleap.append(i)
for i in range(1001,9999):
    if i in leap:
        for l in range(1,len(lmonth)+1):
            for j in range(1,lmonth[l-1]+1):
                 leap_year.append('{:02}'.format(l)+'{:02}'.format(j)+'{:02}'.format(i))
    else:                
        for l in range(1,len(nlmonth)+1):
            for j in range(1,nlmonth[l-1]+1):
                 nonleap_year.append('{:02}'.format(l)+'{:02}'.format(j)+'{:02}'.format(i))                    
for g in range(len(leap_year)):
    if(leap_year[g][::-1]==leap_year[g][::1]):
        count=count+1
for h in range(len(nonleap_year)):
    if(nonleap_year[h][::-1]==nonleap_year[h][::1]):
        count=count+1
print(count)
