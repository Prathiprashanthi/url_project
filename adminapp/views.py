from django.shortcuts import render,redirect,get_object_or_404
from adminapp.models import *
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,f1_score, recall_score, precision_score
from mainapp.models import *
from userapp.models import *
from django.contrib import messages
from django.core.paginator import Paginator
# import encode



# Create your views here.
def admin_index(request):
    dataset=Dataset.objects.all().count()
    user=UserModel.objects.all().count()
    return render(request,'admin/admin-index.html',{'Dataset':dataset,'user':user})

def pending_users(request):
    pending = UserModel.objects.filter(User_Status = 'Pending')
    paginator = Paginator(pending, 5) 
    page_number = request.GET.get('page')
    post = paginator.get_page(page_number)
    return render(request,'admin/admin_penndinguser.html', { 'user' : post})

def all_users(request):
    all_users  = UserModel.objects.all()
    paginator = Paginator(all_users, 5)
    page_number =request.GET.get('page')
    post = paginator.get_page(page_number)
    return render(request,'admin/admin_allusers.html',{"allu" : all_users, 'user' : post})

def delete_user(request, id):
    UserModel.objects.get(user_id = id).delete()
    messages.warning(request, 'User was Deleted..!')
    return redirect('all_users')

# Acept users button
def accept_user(request, id):
    status_update =UserModel.objects.get(user_id = id)
    status_update.User_Status = 'accepted'
    status_update.save()
    messages.success(request, 'User was accepted..!')
    return redirect('pending_users')

# Remove user button
def reject_user(request, id):
    status_update2 = UserModel.objects.get(user_id = id)
    status_update2.User_Status = 'removed'
    status_update2.save()
    messages.warning(request, 'User was Rejected..!')
    return redirect('pending_users')
    
def admin_add_data(request):
  
    if request.method == 'POST':
        dataset = request.FILES['dataset']
        data = Dataset.objects.create(data_set = dataset)
        data = data.data_id
        print(type(data),'type')

        return redirect('admin_run_algorithm',data)
 
    return render(request,'admin/admin-add-data.html')

def delete_dataset(request, id):
    dataset = Dataset.objects.get(user_id = id).delete()
    messages.warning(request, 'Dataset was deleted..!')
    return redirect('viewdataset')

from django.urls import reverse

def admin_score(request, id):
    data = Dataset.objects.get(data_id=id)
    admin_run_algorithm_url = reverse('admin_run_algorithm', args=[data.data_id])
    return render(request, 'admin/admin-score.html', {'i': data, 'admin_run_algorithm_url': admin_run_algorithm_url})


def admin_run_algorithm(request,data):
    data = Dataset.objects.get(data_id = data)
    print(data,type(data),'sssss')
    file = str(data.data_set)
    df = pd.read_csv('./media/'+ file)
    table = df.to_html(table_id='data_table')
    
    print(df.iloc[0,[1]])
    print(len(df))
    for i in range(len(df)):
        print(df.iloc[i,[1]],'loop')
    print(df[0:5],type(df),'database tablesssssssssss')

    return render(request,'admin/admin-run-algorithm.html',{'i':data,'t':table})


def LogisticRegression(request,id):
    Accuracy = None
    Precision = None
    Recall = None
    F1_Score = None
    data = Dataset.objects.get(data_id=id)
    id = data.data_id
    file = str(data.data_set)
    df = pd.read_csv('./media/media/url_10k.csv')
  
    
    from sklearn.model_selection import train_test_split
    #converting text into Numbers
    from sklearn.feature_extraction.text import TfidfVectorizer
    vectorizer = TfidfVectorizer()
    from sklearn.feature_extraction.text import TfidfVectorizer
    

    def makeTokens(f):
        tkns_BySlash=str(f.encode('utf-8')).split('/')
        total_Tokens=[]
        for i in tkns_BySlash:
            tokens=str(i).split('-')
            tkns_ByDot=[]
            for j in range(0,len(tokens)):
                temp_Tokens=str(tokens[j]).split('.')
                tkns_ByDot=tkns_ByDot + temp_Tokens
            total_Tokens=total_Tokens + tokens + tkns_ByDot
        total_Tokens= list(set(total_Tokens))
        if 'com' in total_Tokens:
            total_Tokens.remove('com')
        return total_Tokens
    vectorizer=TfidfVectorizer(tokenizer=makeTokens)
    
    X=vectorizer.fit_transform(df["url"])
    print(X.shape,'fgtretyuiokjhnbgffrry')
    y=df["label"]
    print(X.shape,y.shape,'sdgsdfg')
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
    print(X_train.shape,'kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk')
    print(y_train.shape,'ffffffffffffkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk')
    #Machinelearning
    from sklearn.linear_model import LogisticRegression
    model_name = LogisticRegression()
    model_name.fit(X_train,y_train)
    
    prediction = model_name.predict(X_test)
    
    Accuracy=(accuracy_score(prediction,y_test))
    Precision=(precision_score(prediction,y_test,average = 'macro'))
    Recall=(recall_score(prediction,y_test,average = 'macro'))
    F1_Score=(f1_score(prediction,y_test,average = 'macro'))
    print(Accuracy,Precision,Recall,F1_Score,'Scoreeeeeeeeeeeee lr')
    data.Accuracy = Accuracy
    data.Precision = Precision
    data.Recall = Recall
    data.F1_Score = F1_Score
    data.algo = "Logistic Regression"
    data.save(update_fields=["Accuracy","Precision","Recall","F1_Score","algo"])
    data.save()
    return redirect('admin_score',id=id)

def RandomForest(request,id):
    Accuracy = None
    Precision = None
    Recall = None
    F1_Score = None
    data = Dataset.objects.get(data_id=id)
    id = data.data_id
    file = str(data.data_set)
    # df = pd.read_csv('./media/'+ file)
    df = pd.read_csv('./media/media/url_10k.csv')

    from sklearn.model_selection import train_test_split
    #converting text into Numbers
    from sklearn.feature_extraction.text import TfidfVectorizer
    

    def makeTokens(f):
        tkns_BySlash=str(f.encode('utf-8')).split('/')
        total_Tokens=[]
        for i in tkns_BySlash:
            tokens=str(i).split('-')
            tkns_ByDot=[]
            for j in range(0,len(tokens)):
                temp_Tokens=str(tokens[j]).split('.')
                tkns_ByDot=tkns_ByDot + temp_Tokens
            total_Tokens=total_Tokens + tokens + tkns_ByDot
        total_Tokens= list(set(total_Tokens))
        if 'com' in total_Tokens:
            total_Tokens.remove('com')
        return total_Tokens
    vectorizer=TfidfVectorizer(tokenizer=makeTokens)
    
    X=vectorizer.fit_transform(df["url"])
    import joblib
    file=open('vc_rf.pkl','wb')
    joblib.dump(X,file)
    print(X.shape,'fgtretyuiokjhnbgffrry')
    
    y=df["label"]
    print(X.shape,y.shape,'sdgsdfg')
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
    print(X_train.shape,'kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk')
    print(y_train.shape,'ffffffffffffkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk')
    #Mchinelearning
    from sklearn.ensemble import RandomForestClassifier
    
    model_name = RandomForestClassifier()
    model_name.fit(X_train,y_train)
    
    prediction = model_name.predict(X_test)
    
    Accuracy=(accuracy_score(prediction,y_test))
    Precision=(precision_score(prediction,y_test,average = 'macro'))
    Recall=(recall_score(prediction,y_test,average = 'macro'))
    F1_Score=(f1_score(prediction,y_test,average = 'macro'))
    print(Accuracy,Precision,Recall,F1_Score,'Scoreeeeeeeeeeeee lr')
    data.Accuracy = Accuracy
    data.Precision = Precision
    data.Recall = Recall
    data.F1_Score = F1_Score
    data.algo = "Random Forest"
    data.save(update_fields=["Accuracy","Precision","Recall","F1_Score","algo"])
    data.save()
    import joblib
    file=open('url_rf.pkl','wb')
    joblib.dump(prediction,file)    
   
    return redirect('admin_score',id=id)



def KNeighborsRegressor(request,id):
    Accuracy = None
    Precision = None
    Recall = None
    F1_Score = None
    data = Dataset.objects.get(data_id=id)
    id = data.data_id
    file = str(data.data_set)
    # df = pd.read_csv('./media/'+ file)
    df = pd.read_csv('./media/media/url_10k.csv')

    from sklearn.model_selection import train_test_split
    from sklearn.feature_extraction.text import TfidfVectorizer
    # vectorizer = TfidfVectorizer()
    

    def makeTokens(f):
        tkns_BySlash=str(f.encode('utf-8')).split('/')
        total_Tokens=[]
        for i in tkns_BySlash:
            tokens=str(i).split('-')
            tkns_ByDot=[]
            for j in range(0,len(tokens)):
                temp_Tokens=str(tokens[j]).split('.')
                tkns_ByDot=tkns_ByDot + temp_Tokens
            total_Tokens=total_Tokens + tokens + tkns_ByDot
        total_Tokens= list(set(total_Tokens))
        if 'com' in total_Tokens:
            total_Tokens.remove('com')
        return total_Tokens
    vectorizer=TfidfVectorizer(tokenizer=makeTokens)
    
    X=vectorizer.fit_transform(df["url"])
    print(X.shape,'fgtretyuiokjhnbgffrry')
    y=df["label"]
    print(X.shape,y.shape,'sdgsdfg')
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
    print(X_train.shape,'kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk')
    print(y_train.shape,'ffffffffffffkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk')
    #Mchinelearning
    from sklearn.neighbors import KNeighborsClassifier
    
    model_name = KNeighborsClassifier()
    model_name.fit(X_train,y_train)
    
    prediction = model_name.predict(X_test)
    
    Accuracy=(accuracy_score(prediction,y_test))
    Precision=(precision_score(prediction,y_test,average = 'macro'))
    Recall=(recall_score(prediction,y_test,average = 'macro'))
    F1_Score=(f1_score(prediction,y_test,average = 'macro'))
    print(Accuracy,Precision,Recall,F1_Score,'Scoreeeeeeeeeeeee lr')
    data.Accuracy = Accuracy
    data.Precision = Precision
    data.Recall = Recall
    data.F1_Score = F1_Score
    data.algo = "KNeighborsClassifier"
    data.save(update_fields=["Accuracy","Precision","Recall","F1_Score","algo"])
    data.save()

    return redirect('admin_score',id=id)

def SVM(request,id):
    Accuracy = None
    Precision = None
    Recall = None
    F1_Score = None
    data = Dataset.objects.get(data_id=id)
    id = data.data_id
    file = str(data.data_set)
    # df = pd.read_csv('./media/'+ file)
    df = pd.read_csv('./media/media/url_10k.csv')
    from sklearn.model_selection import train_test_split
    from sklearn.feature_extraction.text import TfidfVectorizer
    # vectorizer = TfidfVectorizer()
    

    def makeTokens(f):
        tkns_BySlash=str(f.encode('utf-8')).split('/')
        total_Tokens=[]
        for i in tkns_BySlash:
            tokens=str(i).split('-')
            tkns_ByDot=[]
            for j in range(0,len(tokens)):
                temp_Tokens=str(tokens[j]).split('.')
                tkns_ByDot=tkns_ByDot + temp_Tokens
            total_Tokens=total_Tokens + tokens + tkns_ByDot
        total_Tokens= list(set(total_Tokens))
        if 'com' in total_Tokens:
            total_Tokens.remove('com')
        return total_Tokens
    vectorizer=TfidfVectorizer(tokenizer=makeTokens)
    
    X=vectorizer.fit_transform(df["url"])
    print(X.shape,'fgtretyuiokjhnbgffrry')
    y=df["label"]
    print(X.shape,y.shape,'sdgsdfg')
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
    print(X_train.shape,'kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk')
    print(y_train.shape,'ffffffffffffkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk')
    #Mchinelearning
    from sklearn.svm import SVC
    
    model_name = SVC()
    model_name.fit(X_train,y_train)
    
    prediction = model_name.predict(X_test)
    
    Accuracy=(accuracy_score(prediction,y_test))
    Precision=(precision_score(prediction,y_test,average = 'macro'))
    Recall=(recall_score(prediction,y_test,average = 'macro'))
    F1_Score=(f1_score(prediction,y_test,average = 'macro'))
    print(Accuracy,Precision,Recall,F1_Score,'Scoreeeeeeeeeeeee lr')
    data.Accuracy = Accuracy
    data.Precision = Precision
    data.Recall = Recall
    data.F1_Score = F1_Score
    data.algo = "SVM"
    data.save(update_fields=["Accuracy","Precision","Recall","F1_Score","algo"])
    data.save()
    return redirect('admin_score',id=id)

def LSTM(request,id):
    return redirect('admin_score',id=id)

def admin_graph_analysis(request):
    sv = Dataset.objects.filter(algo='SVM').first()
    sv_ac = sv.Accuracy * 100 if sv else 0  # Handle the case when sv is None
    
    nb = Dataset.objects.filter(algo='KNeighborsClassifier').first()
    nb_ac = nb.Accuracy * 100 if nb else 0  # Handle the case when nb is None

    lr = Dataset.objects.filter(algo='Logistic Regression').first()
    lr_ac = lr.Accuracy * 100 if lr else 0  # Handle the case when lr is None

    rf = Dataset.objects.filter(algo='Random Forest').first()
    rf_ac = rf.Accuracy * 100 if rf else 0  # Handle the case when rf is None

    context = {
        'lr_ac': lr_ac,
        'nb_ac': nb_ac,
        'rf_ac': rf_ac,
        'sv_ac': sv_ac,
    }
    return render(request, 'admin/admin-graphanalysis.html', context)
