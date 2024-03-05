from django.shortcuts import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
def about(request):
    return render(request,'about.html')

def register(request):
    if(request.method=="POST"):
        data=request.POST
        firstname=data.get('textfirstname')
        lastname=data.get('textlastname')
        if('buttonsubmit' in request.POST):
            result=firstname+lastname
            return render(request,'register.html',context={'result':result})
    return render(request,'register.html')

def employee(request):
    if(request.method=="POST"):
        data=request.POST #stores all the values
        emailid=data.get('textemailid')
        mobileno=data.get('textmobileno')
        if('buttonsubmit' in request.POST):
            result=emailid+mobileno
            return render(request,'employee.html',context={'result':result})
    return render(request,'employee.html')

def calci(request):
    if(request.method=="POST"):
        data=request.POST #stores all the values
        firstnumber=data.get('textfirstnumber')
        secondnumber=data.get('textsecondnumber')
        if('buttonadd' in request.POST):
             result=int(firstnumber)+int(secondnumber)
             return render(request,'calci.html',context={'result':result})
        if('buttonsub' in request.POST):
             result=int(firstnumber)-int(secondnumber)
             return render(request,'calci.html',context={'result':result})
        if('buttonmul' in request.POST):
             result=int(firstnumber)*int(secondnumber)
             return render(request,'calci.html',context={'result':result})
        if('buttondiv' in request.POST):
             result=int(firstnumber)/int(secondnumber)
             return render(request,'calci.html',context={'result':result})
    return render(request,'calci.html')

def index(request):
    return render(request,'index.html')

def home(request):
    if(request.method=="POST"):
        data=request.POST
        area=data.get('textarea')
        price=data.get('textprice')
        if('buttonsubmit' in request.POST):
            result=int(area)*int(price)
            return render(request,'home.html',context={'result':result})
    return render(request,'home.html')

def marks(request):
    if(request.method=="POST"):
        data=request.POST
        hours=data.get('textmarks')
        age=data.get('textage')
        internet=data.get('textinternet')
        if('buttonpredict' in request.POST):
                import pandas as pd
                path="C:\\Users\\User\\Desktop\\IS\\Data\\Exammarks.csv"
                data=pd.read_csv(path)
                #print(data)
                #print(data.info())
                #print(data.shape)
                #print(data.isnull().sum())

                medianvalue=data.hours.median()
                #print(medianvalue)

                data.hours=data.hours.fillna(medianvalue)
                #print(data)
                #print(data.isnull().sum())

                inputs=data.drop('marks',axis=1)
                #print(inputs)
                output=data.drop(['hours','age','internet'],axis=1)
                #print(output)

                import sklearn
                import math
                from sklearn import linear_model
                model=linear_model.LinearRegression()
                model.fit(inputs,output)

                result=model.predict([[float(hours),int(age),int(internet)]])
                return render(request,'marks.html',context={'result':result})
    return render(request,'marks.html')

def salary(request):
    if(request.method=="POST"):
        data=request.POST
        company=data.get('textcompany')
        job=data.get('textjob')
        degree=data.get('textdegree')
        if('buttonsubmit' in request.POST):
            import pandas as pd
            path="C:\\Users\\User\\Desktop\\IS\\Data\\salaries.csv"
            data=pd.read_csv(path)
            #print(data)
            #print(data.info())
            #print(data.isnull().sum())
            #print(data['company'].unique())
            #print(data['job'].unique())
            #print(data['degree'].unique())

            import sklearn
            from sklearn.preprocessing import LabelEncoder
            le_company=LabelEncoder()
            le_job=LabelEncoder()
            le_degree=LabelEncoder()

            data['company_n']=le_company.fit_transform(data['company'])
            data['job_n']=le_company.fit_transform(data['job'])
            data['degree_n']=le_company.fit_transform(data['degree'])

            inputs=data.drop(['company','job','degree','salary_more_then_100k'],axis=1)
            output=data.drop(['company','job','degree','company_n','job_n','degree_n'],axis=1)
            #print(inputs)
            #print(output)

            import sklearn
            from sklearn import tree
            model=tree.DecisionTreeClassifier()
            model.fit(inputs,output)

            #company=int(input("Enter the company(0-abc,1-facebook,2-google)"))
            #job=int(input("Enter the job(business manager,1-computer programmer,2-sales executive)"))
            #degree=int(input("Enter the degree(0-bachulers,1-master)"))


            result=model.predict([[int(company),int(job),int(degree)]]) #1-facebook,2-b.manager,1-master
            print(result)
            if result==1:
                print("salary is more than 100k")
            else:
                print("salary is less than 100k")
            return render(request,'salary.html',context={'result':result})
                
            #acc=model.score(inputs,output)
            #print(acc*100)
           
    return render(request,'salary.html')

def network(request):
    if(request.method=="POST"):
        data=request.POST
        portnumber=data.get('textportnumber')
        receivedpackets=data.get('textreceivedpackets')
        receivedbytes=data.get('textreceivedbytes')
        sentbytes=data.get('textsentbytes')
        sentpackets=data.get('textsentpackets')
        portaliveduration=data.get('textportaliveduration')
        packetsrxdropped=data.get('textpacketrxdropped')
        packetstxdropped=data.get('textpacketstxdropped')
        packetsrxerrors=data.get('textpacketsrxerrors')
        packetstxerrors=data.get('textpacketstxerrors')
        deltareceivedpackets=data.get('textdeltareceivedpackets')
        deltareceivedbytes=data.get('textdeltareceivedbytes')
        deltasentbytes=data.get('textdeltasentbytes')
        deltasentpackets=data.get('textdeltasentpackets')
        deltaportaliveduration=data.get('textdeltaportaliveduration')
        deltapacketsrxdropped=data.get('textdeltapacketsrxdropped')
        deltapacketstxdropped=data.get('textdeltapacketstxdropped')
        deltapacketsrxerrors=data.get('textdeltapacketsrxerrors')
        deltapacketstxerrors=data.get('textdeltapacketstxerrors')
        connectionpoints=data.get('textconnectionpoints')
        totalloadr=data.get('textloadr')
        totalloadl=data.get('textloadl')
        unknownload=data.get('textUnknownload')
        unknownlatest=data.get('textunknownlatest')
        latestbytescounter=data.get('textlatestbytecounter')
        is_valid=data.get('textisvalid')
        tableid=data.get('texttableid')
        actionflowentries=data.get('textactiveflowentries')
        packetslookedup=data.get('textpacketslookedup')
        packetsmatched=data.get('textpacketsmatched')
        maximumsize=data.get('textmaximumsize')
        if('buttonsubmit' in request.POST):
            import pandas as pd
            path="C:\\Users\\Spoorthi CK\\Desktop\\Inter\\2023_projects\\9_Network Intrusion Detection\\train_dataset.csv"
            data=pd.read_csv(path)
            #print(data)
            #print(data.info())
            
            inputs=data.drop("Label",axis=1)
            output=data['Label']
            #print(inputs)
            #print(output)

            import sklearn
            from sklearn.model_selection import train_test_split
            x_train,x_test,y_train,y_test=train_test_split(inputs,output,train_size=0.8)
            #print(x_train)
            #print(x_test)
            #print(y_train)
            #print(y_test)

            from sklearn.naive_bayes import GaussianNB
            model=GaussianNB()
            model.fit(x_train,y_train)
            y_pred=model.predict(x_test)
           #print(y_pred)
            #print(y_test)

            #res=model.predict([[4,305111,25506841,1E+08,284579,1657,0,0,0,0,2,278,556,4,5,0,0,0,0,4,0,0,0,0,0,1,0,6,992868,992744,-1]])
            #print(res)
            
            result=model.predict([[int(portnumber),int(receivedpackets),int(receivedbytes),float(sentbytes),int(sentpackets),int(portaliveduration),int(packetsrxdropped),int(packetstxdropped),int(packetsrxerrors),int(packetstxerrors),int(deltareceivedpackets),
                                int(deltareceivedbytes),int(deltasentbytes),int(deltasentpackets),int(deltaportaliveduration),int(deltapacketsrxdropped),int(deltapacketstxdropped),int(deltapacketsrxerrors),int(deltapacketstxerrors),int(connectionpoints),
                                int(totalloadr),int(totalloadl),int(unknownload),int(unknownlatest),int(latestbytescounter),int(is_valid),int(tableid),int(actionflowentries),int(packetslookedup),int(packetsmatched),int(maximumsize)]])
            print(result)
            if result==0:
                return HttpResponse("Normal Network Intrusion")
            elif result==1:
                return HttpResponse("Blackhole Network Intrusion")
            elif result==2:
                return HttpResponse("TCP-SYN Network Intrusion")
            elif result==3:
                return HttpResponse("PortScam Network Intrusion")
            elif result==4:
                return HttpResponse("Diversion Network Intrusion")
            else:
                return HttpResponse("Overflow Network Intrusion")
        return render(request,'network.html',context={'result':result})     

    return render(request,'network.html')



def keer(request):
    return render(request,'keer.html')

def drink(request):
    if(request.method=="POST"):
        data=request.POST
        age=data.get('textage')
        height=data.get('textheight')
        weight=data.get('textweight')
        waist=data.get('textwaist')
        eyesightl=data.get('texteyesightl')
        eyesightr=data.get('texteyesightr')
        hearingl=data.get('texthearingl')
        hearingr=data.get('texthearingr')
        systolic=data.get('textsystolic')
        relaxation=data.get('textrelaxation')
        fastingbloodsugar=data.get('textfastingbloodsugar')
        cholesterol=data.get('textcholesterol')
        trigylceride=data.get('texttriglyceride')
        hdl=data.get('texthdl')
        ldl=data.get('textldl')
        hemoglobin=data.get('texthemoglobin')
        urineprotein=data.get('texturineprotein')
        serumcreatinine=data.get('textserumcreatinine')
        ast=data.get('textast')
        alt=data.get('textalt')
        gtp=data.get('textgtp')
        dentalcaries=data.get('textdentalcaries')
        if('buttonsubmit' in request.POST):
            import pandas as pd
            path="C:\\Users\\User\\OneDrive\\Desktop\\IS\\2023_projects\\10_Smoker Status Prediction\\train_dataset.csv"
            data=pd.read_csv(path)
            #print(data)
            #print(data.info())

            inputs=data.drop('smoking',axis=1)
            output=data['smoking']

            #print(inputs)
            #print(output)

            import sklearn
            from sklearn.model_selection import train_test_split
            x_train,x_test,y_train,y_test=train_test_split(inputs,output,train_size=0.8)
            #print(x_train)
            #print(x_test)
            #print(y_train)
            #print(y_test)

            from sklearn.naive_bayes import GaussianNB
            model=GaussianNB()
            model.fit(x_train,y_train)
            y_pred=model.predict(x_test)
            #print(y_pred)
            #print(y_test)

            result=model.predict([[int(age),int(height),int(weight),float(waist),float(eyesightl),float(eyesightr),int(hearingl),int(hearingr),int(systolic),int(relaxation),int(fastingbloodsugar),int(cholesterol),int(trigylceride),int(hdl),int(ldl),float(hemoglobin),int(urineprotein),float(serumcreatinine),int(ast),int(alt),int(gtp),int(dentalcaries)]])
            print(result)
            if result==1:
                return("the person is smoking")
            else:
                return("the person is not smoking")
        return render(request,'drink.html',context={'result':result})
    
    return render(request,'drink.html')

def hello(request):
    return render(request,'hello.html')

def aaa(request):
    return render(request,'aaa.html')
def a1(request):
    return render(request,'a1.html')

def shashi(request):
    if(request.method=="POST"):
        data=request.POST
        age = data.get("textage")
        job = data.get("textjob")
        marital = data.get("textmaterial")
        education = data.get("texteducation")
        default = data.get("textdefault")
        balance = data.get("textbalance")
        housing = data.get("texthousing")
        loan = data.get("textloan")
        contact = data.get("textcontact")
        day = data.get("textday")
        month = data.get("textmonth")
        duration = data.get("textduration")
        campaign = data.get("textcompaign")
        pdays = data.get("textpdays")
        previous = data.get("textprevious")
        poutcome = data.get("textpoutcomes")
        if('buttonsubmit' in request.POST):
            import pandas as pd
            path="C:\\Users\\Spoorthi CK\\OneDrive\\Desktop\\Inter\\2023_projects\\19_SubscriberPrediction.\\train.csv"
            data=pd.read_csv(path)
            #print(data)
            #print(data.info())


            data['job']=data['job'].map({'admin.':0,'blue-collar':1,'services':2,'technician':3,'management':4,'unknown':5,'self-employed':6,'retired':7,'housemaid':8,'entrepreneur':9,'unemployed':10,'student':11,'services':12})
            data['marital']=data['marital'].map({'single':1,'married':2,'divorced':3})
            data['education']=data['education'].map({'primary':0,'secondary':1,'tertiary':2,'unknown':3})
            data['default']=data['default'].map({'yes':1,'no':0})
            data['housing']=data['housing'].map({'yes':1,'no':0})
            data['loan']=data['loan'].map({'yes':1,'no':0})
            data['contact']=data['contact'].map({'cellular':1,'unknown':2,'telephone':3})
            data['month']=data['month'].map({'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12})
            data['poutcome']=data['poutcome'].map({'unknown':1,'success':2,'failure':3,'other':4})

            #print(data)
            #print(data.info())
            inputs=data.drop('y_bool',axis=1)
            output=data['y_bool']
            #print(output)
            #print(inputs)

            import sklearn
            from sklearn.model_selection import train_test_split
            x_train,x_test, y_train, y_test = train_test_split(inputs,output,train_size=0.8)
            #print(x_train)
            #print(x_test)
            #print(y_train)
            #print(y_test)

            from sklearn.naive_bayes import GaussianNB
            model=GaussianNB()
            model.fit(x_train,y_train)
            y_pred=model.predict(x_train)
            #print(y_pred)
            #print(y_test)

            
            '''age=int(input("Enter the Age :"))
            job=float(input("Enter the job role:"))
            marital=float(input("Enter the marital:"))
            education=float(input("Enter the education: "))
            default=int(input("Enter the default value "))
            balance=int(input("Enter the balance value "))
            housing=int(input("Enter the housing value "))
            loan=int(input("Enter the loan value "))
            contact=int(input("Enter the contact value: "))
            day=int(input("Enter the day :"))
            month=int(input("Enter the month :"))
            duration=int(input("Enter the duration :"))
            campaign=int(input("Enter the campaign :"))
            pdays=int(input("Enter the pdays value :"))
            previous=int(input("Enter the previous value:"))
            poutcome=int(input("Enter the poutcome:"))'''
            result=model.predict([[int(age or 0),int(job or 0),(marital or 0),int(education or 0),int(default or 0),int(balance or 0),int(housing or 0),int(loan or 0),int(contact or 0),int(day or 0),int(month or 0),int(duration or 0),int(campaign or 0),int(pdays or 0),int(previous or 0),int(poutcome or 0)]])

            #res=model.predict([[25,0,2,1,0,6658,1,0,1,16,2,197,1,-1,0,1]])
            print(result)

            if result==1:
                return HttpResponse("Subscriber")
            else:
                return HttpResponse("Not a subscriber")
        return render(request,'shashi.html',context={'result':result})
    return render(request,'shashi.html')