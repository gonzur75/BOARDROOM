import datetime

from django.contrib.auth import get_user_model
from django import forms
from django.core.validators import MinValueValidator
from django.forms import CheckboxInput, TextInput, SelectDateWidget, HiddenInput
from django.utils import timezone

from home.models import Boardrooms, Reservations


class BoardroomForm(forms.ModelForm):
    class Meta:
        model = Boardrooms
        fields = '__all__'


class BrModify(forms.ModelForm):
    # name = forms.CharField(max_length=255)

    class Meta:
        model = Boardrooms
        fields = '__all__'     # {'capacity', 'projector'}


class BrReserveForm(forms.ModelForm):
    class Meta:
        model = Reservations
        fields = "__all__"
        labels = {'rese_date': 'Please choose booking date'}
        defaults = {'rese_date': timezone.now()}
        widgets = {
            'boardrooms': HiddenInput(),
            'rese_date': SelectDateWidget(),
            'comment': TextInput(attrs={
                'placeholder': 'Please enter additional info'
            })
        }
        # constraints = [
        #      models.CheckConstraint(check=models.Q(age__gte=18), name='age_gte_18'),
        # ]


class BrSearchForm(forms.ModelForm):
    class Meta:
        model = Boardrooms
        fields = '__all__'


