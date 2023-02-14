from . import validators


class PostCodeForm(forms.Form):
    post_code = forms.CharField(max_length=10, validators=[validators.PostCodeValidator])
