from django import forms
from new.models import Feedback2,DataModel

#model feedback
class FeedbackForm(forms.ModelForm):
   

    class Meta:
        model=Feedback2
        fields="__all__"


#model data
class DataForm2(forms.ModelForm):
   

    class Meta:
        model=DataModel
        fields="__all__"

