from django import forms
from django.contrib.auth.forms import AuthenticationForm
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import FieldWithButtons
from crispy_forms.layout import Layout, Submit
from crispy_bootstrap5 import bootstrap5


class SearchForm(forms.Form):
    q = forms.CharField(label="Search", required=False)

    class Media:
        js = [
            "js/search.js",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["q"].label = ""

        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_method = "GET"
        self.helper.include_media = False
        self.helper.layout = Layout(
            FieldWithButtons(
                bootstrap5.Field("q", type="search"),
                Submit("search", "Search"),
            )
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
            bootstrap5.FloatingField("username", autocomplete="username"),
            bootstrap5.FloatingField("password", autocomplete="current-password"),
        )
