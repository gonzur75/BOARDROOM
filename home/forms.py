from django.contrib.auth import get_user_model
from django import forms
from django.core.validators import MinValueValidator
from django.forms import CheckboxInput, TextInput
from home.models import Boardrooms


class BoardroomForm(forms.ModelForm):
    class Meta:
        model = Boardrooms
        fields = '__all__'


class BrModify(forms.ModelForm):
    name = forms.CharField(max_length=255)

    class Meta:
        model = Boardrooms
        fields = {'capacity', 'projector'}

