from django.forms import ModelForm, NumberInput
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget

from ddt.models import Registration, Wall


class RegistrationForm(ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaWidget())

    class Meta:
        model = Registration
        fields = '__all__'
        widgets = {
            'amount': NumberInput(attrs={'min': 1, 'max': 10})
        }


class WallForm(ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaWidget())

    class Meta:
        model = Wall
        fields = '__all__'
