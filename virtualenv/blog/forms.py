from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm): #PostForm is the form's name, forms.ModelForm tells Django this form is a ModelForm
    class Meta:
        model = Post #tell Django which model should be used to create this form
        fields = ('title', 'text',) #which field(s) should end up in our form
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)