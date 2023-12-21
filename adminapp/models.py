from django.db import models

# Create your models here.
class Dataset(models.Model):
    data_id = models.AutoField(primary_key=True)
    data_set = models.FileField(upload_to='files/')
    Accuracy = models.FloatField(null=True)
    Precision = models.FloatField(null=True)
    Recall = models.FloatField(null=True)
    F1_Score = models.FloatField(null=True)
    algo = models.CharField(max_length=50,null=True)
    class Meta:
        db_table = 'dataset'
