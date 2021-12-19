from django.contrib.auth import get_user_model
from django import forms
from django.core.validators import MinValueValidator
from django.forms import CheckboxInput
from home.models import Boardrooms


class BoardroomForm(forms.ModelForm):
    class Meta:
        model = Boardrooms
        fields = '__all__'

        # name = forms.CharField(label="Your name", max_length=255)
        # capacity = forms.IntegerField(validators=[MinValueValidator(1)])
        # projector = forms.BooleanField(label='projector', label_suffix=":",
        #                                widget=forms.widgets.CheckboxInput(
        #                                    attrs={'class': 'checkbox-inline'}))

    # def save(self, commit=True, *args, **kwargs):
    #     m = super().save(commit=False)
    #     m.name = self.cleaned_data.get('name').lower
    #     m.capacity = self.cleaned_data.get('capacity')
    #     m.projector = self.cleaned_data.get('')
    #
    #     if commit:
    #         m.save
    #
    #     return m

