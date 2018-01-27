from django import forms

from .models import Post, Questions

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',) 
        
class QuestionForm(forms.ModelForm):
    
    class Meta:
        model = Questions
        fields = ('author' , 'title', 'text' )
