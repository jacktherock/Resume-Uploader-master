from django import forms
from .models import Resume

GENDER = [
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other"),
]

JOB_CITY = [
    ("Delhi", "Delhi"),
    ("Pune", "Pune"),
    ("Mumbai", "Mumbai"),
    ("Nagpur", "Nagpur"),
    ("Aurangabad", "Aurangabad"),
    ("Nashik", "Nashik"),
]


class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER, widget=forms.RadioSelect)
    job_city = forms.MultipleChoiceField(
        label="Preferred Job Location",
        choices=JOB_CITY,
        widget=forms.CheckboxSelectMultiple(),
    )

    class Meta:
        model = Resume
        fields = "__all__"
        labels = {
            "dob": "Date of Birth",
            "email": "Email ID",
            "mobile": "Mobile Number",
            "pincode": "Pin Code",
            "profile_image": "Profile Image",
            "my_file": "My File",
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "dob": forms.DateInput(attrs={"class": "form-control ", "id":"datepicker"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "mobile": forms.NumberInput(attrs={"class": "form-control"}),
            "address": forms.TextInput(attrs={"class": "form-control"}),
            "city": forms.TextInput(attrs={"class": "form-control"}),
            "pincode": forms.NumberInput(attrs={"class": "form-control"}),
            "state": forms.Select(attrs={"class": "form-control"}),
            "country": forms.Select(attrs={"class": "form-control"}),
            "profile_image": forms.FileInput(attrs={"class": "form-control"}),
            "my_file": forms.FileInput(attrs={"class": "form-control"}),
        }
