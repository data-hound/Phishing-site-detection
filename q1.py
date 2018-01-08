def clasif1():
    i=0
    j=0
    Y=[]
    X=[]
    temp=[]
    count1=count2=0
    accuracy=0.0
    import csv
    with open('trainset1.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            for line in row:
                i=0
                st=line.split(",")
                
                for i in range(0,len(st)-1):
                    if not st[i].isdigit():
                        st[i]=str(ord(st[i][0]))
                
            if j!= 0:
                Y.append(st[30:33])
                X.append(st[0:30])
            else:
                j=j+1


    X_test=[]
    pred=[]

    with open('trainset1.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            for line in row:
                i=0
                st=line.split(",")
                
                for i in range(0,len(st)-1):
                    if not st[i].isdigit():
                        st[i]=str(ord(st[i][0]))
                
            
                #Y.append(st[30:33])
                X_test.append(st[0:30])
            

    


    from sklearn.ensemble import RandomForestClassifier


    clf=RandomForestClassifier()
    clf.fit(X,Y)
    pred=clf.predict(X_test)



    with open('output1.csv','w',newline='') as f:
        writer=csv.writer(f)
        writer.writerows(pred)
