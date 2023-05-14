from django import forms
from app.models import *
class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields=['topic_name']
class WebPageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields=['name','url']

class AccessForm(forms.ModelForm):
    class Meta:
        model=AccessRecord
        fields=['auother','date']

