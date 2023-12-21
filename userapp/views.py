from django.shortcuts import render,redirect
from django.contrib import messages
from mainapp.models import *
from userapp.models import *
from adminapp.models import *
import math, random
import qrcode
from PIL import Image, ImageDraw
from io import BytesIO
from django.core.files import File
import time
import pytz
from datetime import datetime
import string
import re
from nltk.stem import WordNetLemmatizer
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()

# Create your views here.
def user_index(request):
    images_count = UserModel.objects.all().count()
    print(images_count)
    user_id = request.session["user_id"]
    user = UserModel.objects.get(user_id = user_id)
    prediction_count =  UserModel.objects.all().count()
    
    if user.Last_Login_Time is None:
        IST = pytz.timezone('Asia/Kolkata')
        current_time_ist = datetime.now(IST).time()
        user.Last_Login_Time = current_time_ist
        user.save()
        messages.success(request, 'You are login SUccessfully..')
    return render(request,'user/user-index.html', {'detect' : images_count, 'la' : user,'predictions' : prediction_count,})
from datetime import datetime

def user_myprofile(request):
    user_id = request.session['user_id']
    user = UserModel.objects.get(user_id=user_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age') 
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        contact = request.POST.get('contact')
        Image = request.FILES.get('image')

        if len(request.FILES) != 0:
            image = Image
            user.user_name = name
            user.user_email = email
            user.user_password = password
            user.user_age = age
            user.user_contact = contact
            user.user_address = address
            user.user_image = image
            user.save()
            messages.success(request, 'Updated Successfully...!')

        else:
            user.user_name = name
            user.user_email = email
            user.user_password = password
            user.user_age = age
            user.user_contact = contact
            user.user_address = address
            user.user_image = image
            user.save()
            messages.success(request, 'Updated Successfully...!')

    return render(request, 'user/user-myprofile.html', {'user': user})


def user_url(request):
    user_id = request.session['user_id']
    user = UserModel.objects.get(user_id=user_id)
    if request.method == 'POST':
        u_url = request.POST.get('url')
        print(u_url,'ppppppppppppppppppppppp')
        request.session['u_url'] = u_url
        # qrcode_img=qrcode.make(data.user_url)
        # randnumber = random.randint(0,9999)
        # canvas=Image.new("RGB", (300,300),"white")
        # draw=ImageDraw.Draw(canvas)
        # canvas.paste(qrcode_img)
        # buffer=BytesIO()
        # canvas.save(buffer,"PNG")
        # data.user_qrcode = f'image{randnumber}.png'
        # data.user_qrcode.save(f'image{randnumber}.png',File(buffer),save=False)
        # data.save()
        # canvas.close()
        return redirect('user_scan')
    return render(request,'user/user-url.html')

def user_scan(request):
    user_id = request.session['user_id']
    wo = WordNetLemmatizer()

    def wordopt(text):
        text = text.lower()
        text = re.sub('\[.*?\]', '', text)
        text = re.sub("\\W"," ",text) 
        text = re.sub('https?://\S+|www\.\S+', '', text)
        text = re.sub('<.*?>+', '', text)
        text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
        text = re.sub('\n', '', text)
        text = re.sub('\w*\d\w*', '', text)    
        return text

    # Load vectorizer and model
    vectorizer = pickle.load(open('vectorizer.pkl','rb'))
    mnb = pickle.load(open('rfc_credit.pkl','rb'))
    strr = request.session.get('u_url')
    print(strr , "urlllllll")

    a = wordopt(strr)
    example_counts = vectorizer.transform([a])
    prediction = mnb.predict(example_counts)
    print(prediction[0],"howwwww")
    result_message = ''
    if prediction[0] == 'good':
        result_message = 'Good'
    elif prediction[0] == 'bad':
        result_message = 'Bad'

    return render(request,'user/user-scan.html', {'prediction': result_message,'strr':strr})

   
