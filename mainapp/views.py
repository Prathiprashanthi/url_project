from django.shortcuts import render,redirect
from django.contrib import messages
from adminapp.models import *
import urllib.request
import urllib.parse
from mainapp.models import *
import random 
import ssl
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def sendSMS(user, otp, mobile):
    data = urllib.parse.urlencode({
        'username': 'Codebook',
        'apikey': '56dbbdc9cea86b276f6c',
        'mobile': mobile,
        'message': f'Hello {user}, your OTP for account activation is {otp}. This message is generated from https://www.codebook.in server. Thank you',
        'senderid': 'CODEBK'
    })
    data = data.encode('utf-8')
    # Disable SSL certificate verification
    context = ssl._create_unverified_context()
    request = urllib.request.Request("https://smslogin.co/v3/api.php?")
    f = urllib.request.urlopen(request, data,context=context)
    return f.read()

def main_index(request):

    return render(request,'main/main-index.html')

def main_about(request):
    return render(request,'main/main-about.html')

def main_admin_login(request):
    if request.method=='POST':
        
        username=request.POST.get('name')
        userpassword=request.POST.get('password')
        print(username,userpassword)

        if username =="admin" and userpassword == "admin":
            print('suceeeee')
            messages.success(request,"successfully login")
            return redirect('admin_index')
        else:
            messages.error(request,"invalid credentials")
            return redirect('main_admin_login')
  

        messages.success(request,"invalid credentials")
    return render(request,'main/main-admin-login.html')

def main_user_login(request):
    if request.method == 'POST':
        user_email = request.POST.get('email')
        user_password = request.POST.get('password')
        print( user_email,user_password)
        
        # try:
        user_data = UserModel.objects.get(user_email = user_email)
        print(user_data)
        if user_data.user_password == user_password:
            if user_data.Otp_Status == 'verified' and user_data.User_Status=='accepted':
                request.session['user_id'] = user_data.user_id
                messages.success(request, 'You are logged in..')
                user_data.No_Of_Times_Login += 1
                user_data.save()
                return redirect('user_index')
            elif user_data.Otp_Status == 'verified' and user_data.User_Status=='pending':
                messages.info(request, 'Your Status is in pending')
                return redirect('main_user_login')
            else:
                messages.warning(request, 'verifyOTP...!')
                request.session['user_email'] = user_data.user_email
                return redirect('main_otp')
        else:
            messages.error(request, 'incorrect credentials...!')
            return redirect('main_user_login')
        
    return render(request,'main/main-user-login.html')


def main_user_registration(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        age = request.POST.get('age')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        contact = request.POST.get('contact')
        Image = request.FILES['image']
        number= random.randint(1000,9999)
        print(number,'yuiougfghjkhgfdfghjkhgf')
        try:
            data = UserModel.objects.get(user_email =  email)
            messages.warning(request, 'Email was already registered, choose another email..!')
            return redirect('main_user_registration')
        except:
            sendSMS(name,number,contact)
            UserModel.objects.create( user_image=Image,user_name=name,user_password=password,user_age=age,user_email=email,user_address=address,user_contact=contact,Otp_Num = number)
            mail_message = f'Registration Successfully\n Your 4 digit Pin is below\n {number}'
            print(mail_message)
            send_mail("User Password", mail_message , settings.EMAIL_HOST_USER, [email])
            request.session['user_email']= email
            messages.success(request, 'Your account was created..')
            return redirect('main_otp')
    # This block is executed for GET requests.
    return render(request, 'main/main-user-registration.html')



def main_otp(request):
    user_email = request.session['user_email']
    user_o = UserModel.objects.get(user_email = user_email)
    print(user_o.Otp_Num,'data otp')
    if request.method == 'POST':
        user_otp = request.POST.get('otp')
        u_otp = int(user_otp)
        if u_otp == user_o.Otp_Num:
            user_o.Otp_Status = 'verified'
            user_o.save()
            messages.success(request, 'OTP verification was Success. Now you can continue to login..!')
            return redirect('main_user_login')
        else:
            messages.error(request, 'OTP verification was Faild. You entered invalid OTP..!')
            return redirect('main_otp')
    return render(request,'main/main-otp.html')

def main_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        contact = request.POST.get('PhoneNumber')
        age = request.POST.get('age')
        message = request.POST.get('Message')
        print(name,contact,age,message, 'uuuuuuuuuuuuuuuuuuuuuuuuuuuuu')
        UserModel.objects.create(user_name=name,user_contact=contact,user_age=age,Message=message)
        messages.success(request, 'Your message has been submitted successfully.')
        return redirect('main_contact') 
    return render(request,'main/main-contact.html')


