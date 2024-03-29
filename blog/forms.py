from django import forms

from blog.models import Comment


class EmailPostForms(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["body", "name", "email"]


class SearchForm(forms.Form):
    query = forms.CharField()
