# youtube_analysis/forms.py
from django import forms

class CommentAnalysisForm(forms.Form):
    comments = forms.CharField(widget=forms.Textarea, label="Enter Comments")
