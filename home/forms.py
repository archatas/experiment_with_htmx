from django import forms
from django.contrib.auth.forms import AuthenticationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_bootstrap5 import bootstrap5

class SearchForm(forms.Form):
    q = forms.CharField(label="Search", required=False)

    class Media:
        js = [
            "js/search.js",
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_method = "GET"
        self.helper.include_media = False
        self.helper.layout = Layout(
            bootstrap5.Field("q", type="search"),
        )


class LoginForm(AuthenticationForm):

    class Media:
        js = [
            "js/login.js",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.include_media = False
        self.helper.layout = Layout(
            bootstrap5.Field("username", autocomplete="username"),
            bootstrap5.Field("password", autocomplete="current-password"),
        )