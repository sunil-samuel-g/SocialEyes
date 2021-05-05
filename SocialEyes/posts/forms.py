from django import forms
from .models import Post, Comment

class PostModelForm(forms.ModelForm):
	content=forms.CharField(widget=forms.Textarea(attrs={'rows':2,'Placeholder':'Say something...'}))
	class Meta:
		model=Post
		fields=('content','image')

class CommentModelForm(forms.ModelForm):
	body=forms.CharField(label='', 
						widget=forms.TextInput(attrs={'Placeholder':'Add a comment...'}))
	class Meta:
		model=Comment
		fields=('body',)