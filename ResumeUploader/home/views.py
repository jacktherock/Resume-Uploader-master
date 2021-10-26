from django.shortcuts import redirect, render
from .models import Resume
from .forms import ResumeForm
from django.contrib import messages


def home(request):
    candidates = Resume.objects.all()
    if request.method == "POST":
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Resume Uploaded Successfully !")
        else:
            messages.success(request, "Please Fill Valid Resume !")
    else:
        form = ResumeForm()
    return render(request, "home.html", {"form": form, "candidates": candidates})


def CandidateDetail(request, pk):
    candidate = Resume.objects.get(pk=pk)
    return render(request, "candidate.html", {"candidate": candidate})

def delete(request, id):
    if request.method=='POST':
        pi = Resume.objects.get(pk=id)
        pi.delete()
        return redirect('/')
