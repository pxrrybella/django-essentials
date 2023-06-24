from django.db import models

# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
## python manage.py makemigrations
## python manage.py migrate
## python manage.py shell <- to access db information using models