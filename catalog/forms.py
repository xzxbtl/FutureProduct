from django import forms
from django.core.validators import RegexValidator
from .models import NotesUser


# Валидация:
def usernameAndFirstName(value):
    username = str(value)
    if username.lower() == 'none':
        raise forms.ValidationError("Укажите корректное значение")
    elif username.lower() == 'не указано':
        raise forms.ValidationError("Вы не указали значение")
    elif len(username) < 3:
        raise forms.ValidationError("Слишком коротко")


class UserFormOrder(forms.ModelForm):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+79...'. Up to 15 digits "
                                         "allowed.")

    class Meta:
        model = NotesUser
        fields = ("username", "first_name", "phone", "image", "wish")

    username = forms.CharField(
        validators=[usernameAndFirstName],
        required=True,
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите ваше имя пользователя",
            }
        )
    )
    first_name = forms.CharField(
        validators=[usernameAndFirstName],
        required=False,
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите ваше имя",
            }
        )
    )
    phone = forms.CharField(
        validators=[phone_regex],
        required=True,
        max_length=17,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите ваш Телефон",
            }
        )
    )

    image = forms.ImageField(
        widget=forms.FileInput(attrs={"class": "form-control"}),
        required=False
    )

    wish = forms.CharField(
        required=False,
        max_length=200,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите ваше пожелание",
            }
        )
    )
