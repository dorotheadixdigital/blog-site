from django import forms
from core.models import Question, Answer, Favorite

class QuestionCreateForm(forms.Form):
    title = forms.CharField(max_length=250)
    content = forms.CharField(max_length=2000)
    referenceURL = forms.URLField(max_length=2000)


class AnswerCreateForm(forms.Form):
    content = forms.CharField(max_length=2000)
    referenceURL = forms.URLField(max_length=2000)

