from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):                     #the class Post is Django model
    auther = models.ForeignKey('auth.User')    # a link to another model
    title = models.CharField(max_length=200)   #define text with a limited number of characters
    text = models.TextField()                  #long text without a limit
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.published_data = timezone.now()
        self.save()
        
    def __str__(self):
        return self.title