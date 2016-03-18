from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):                     #the class Post is Django model
    author = models.ForeignKey('auth.User')    # a link to another model
    title = models.CharField(max_length=200)   #define text with a limited number of characters
    text = models.TextField()                  #long text without a limit
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def __str__(self):
        return self.title
        
    def approved_comments(self):
        return self.comments.filter(approved_comment=True) #used as post.approved_comments.count in html
        
class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments') 
    #allow us to have access to comments from post model,in html file will access it by post.comments
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    
    def approve(self):
        self.approved_comment = True
        self.save()
        
    def __str__(self):
        return self.text