from django.db import models
from mainapp.models import *



class URLMOdel(models.Model):
    url_id = models.AutoField(primary_key=True)
    user_url = models.ForeignKey(UserModel, on_delete=models.CASCADE,related_name='user_url')
    url=models.TextField()

    class Meta:
        db_table = 'URL_QR_Details'


class TestModel(models.Model):
    id=models.AutoField(primary_key=True)
    testurl=models.TextField()
    test_qrcode=models.ImageField(blank=True,upload_to='media/',null=True)


    class Meta:
        db_table = 'Testing_Details'
