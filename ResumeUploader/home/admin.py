from django.contrib import admin
from .models import Resume

# Register your models here.
@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "dob",
        "email",
        "mobile",
        "gender",
        "address",
        "city",
        "pincode",
        "state",
        "country",
        "job_city",
        "profile_image",
        "my_file",
    ]
