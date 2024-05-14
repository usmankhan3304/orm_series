from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class MyForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    email = forms.EmailField(label="Email")
    age = forms.IntegerField(label="Age")
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')], widget=forms.RadioSelect(), label="Gender")
    comments = forms.CharField(label="Comments", widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(MyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6 mb-0'),
                Column('email', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('age', css_class='form-group col-md-6 mb-0'),
                Column('gender', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'comments',
            Submit('submit', 'Submit', css_class='btn btn-primary')
        )