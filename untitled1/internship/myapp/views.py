from django.shortcuts import render
from django.contrib import auth
# Create your views here.
import pyrebase

config = {
    'apiKey': "AIzaSyCjq6k6g2U1M9kutf9Ok810pu7HcP4CX1o",
    'authDomain': "dbmsproject-bf65c.firebaseapp.com",
    'databaseURL': "https://dbmsproject-bf65c.firebaseio.com",
    'projectId': "dbmsproject-bf65c",
    'storageBucket': "dbmsproject-bf65c.appspot.com",
    'messagingSenderId': "334632020356",
    'appId': "1:334632020356:web:91e0c2e3b0ee94053895d1",
    'measurementId': "G-H7TF0PYKJ3"
}
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()


def signin(request):
    return render(request, 'signin.html')


def postsign(request):
    email = request.POST.get('email')
    passw = request.POST.get('pass')
    try:
        user = authe.sign_in_with_email_and_password(email, passw)
    except:
        message = "qwerty"
        return render(request, 'signin.html', {'msg': 'message'})
    #print(user['idToken'])
    session_id = user['idToken']
    request.session['uid'] = str(session_id)
    idtoken = request.session['uid']
    a = authe.get_account_info(idtoken)
    a=a['users']
    a=a[0]
    a=a['localId']
    print(str(a))
    name = database.child("student").child(a).child("detail").child("name").get().val()
    data= database.child('company').shallow().get().val()

    return render(request, 'welcome.html',{'n': name})


def logout(request):
    auth.logout(request)
    return render(request, 'signin.html')


def signup(request):
    return render(request, 'signup.html ')


def postsignup(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    passwo = request.POST.get('pass')
    user = authe.create_user_with_email_and_password(email, passwo)
    uid = user['localId']
    data = {'name': name, 'email': email, 'passwo': passwo}
    database.child("student").child(uid).child("detail").set(data)
    return render(request, "welcome.html", {'n': name})


def comsignup(request):
    return render(request, "comsignup.html")


def postcomsignup(request):
    name = request.POST.get('name')
    des = request.POST.get('des')
    link = request.POST.get('link')
    data = {'des': des, 'link': link}
    database.child("company").child(name).set(data)
    return render(request, "postcom.html")

def intern(request):
    idtoken = request.session['uid']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    name = database.child("student").child(a).child("detail").child("name").get().val()
    data = database.child('company').shallow().get().val()
    company=[]
    description=[]
    link=[]
    for x in data:
        company.append(x)
    print(company)
    for y in company:
        des=database.child("company").child(y).child("des").get().val()
        description.append(str(des))
    for z in company:
        l=database.child("company").child(y).child("link").get().val()
        link.append(str(l))
    print(link)
    print(description)
    combined=zip(company,description,link)
    return render(request,'getintern.html',{'combine':combined,'n':name})