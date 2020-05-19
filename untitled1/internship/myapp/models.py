from django.db import models


# Create your models here.
class me(models.Model):
    name = models.CharField(max_length=100)
    classes = models.CharField(max_length=20)


'''
def compostsignup(request):
    name = request.POST.get('name')
    desc = request.POST.get('des')
    passwo = request.POST.get('pass')
    user = authe.create_user_with_email_and_password(email,passwo)
    uid = user['localId']
    data = {'name': name, 'description': desc, 'passwo': passwo}
    database.child("company").child(uid).child("details").set(data)
    return render(request,'signin.html')
'''
