from os import path
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage

# create your Views here
def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,'about.html')

def project(request):
    project_show=[

        {"title":"Crudapp",
        "path":"images/crudapp.png"},

         {"title":"Digitam Bank Management System",
         "path":"images/digitalbank_project.png"},

         {"title":"Blinkit Colon",
         "path":"images/Blinkit colon.png"},

         {"title":"FoodOrdering_Console Based Project",
         "path":"images/foodordering.png"},

         {"title":"Portfolio Project",
         "path":"images/portfolio.png"},
         {"title":"ImageUploder Project",
          "path":"images/imageuploder.png"},

    ]
    return render(request,"project.html",{"project_show":project_show})

def experience(request) -> HttpResponse:
    experience = [
        {
            "company": "Growingseed Technologies (Online Training)",
            "Position": "Python + Django Trainee",
            "duration": "3 Months Training",
            "description": "Learned Python basics to Advanced, Django framework, and built sample projects."
        },
        {
            "company": "Digicoder Private Limited Technologies",
            "Position": "6 Months Summer Training",
            "duration": "6 Months Training",
            "description": "Studied web development using HTML,CSS,BOOTSTRAP,JAVASCRIPT, JAVA, and MySQL. Created mini projects."
        }
    ]
    return render(request, "experience.html", {"experience": experience})


def certificate(request):
    certificate_show=[

        {"title":"Growingseed Technologes",
        "path":"images/growingseed.jpg"},

         {"title":"Digicoder Private Limited Technologes",
        "path":"images/digicoder.jpg"},

         {"title":"Wscube Tech",
        "path":"images/wscubetech.jpg"},
    ]
    return render(request,"certificate.html",{"certificate":certificate_show})

def contact(request):
    return render(request,"contact.html")

# Resume function
from django.http import HttpResponse, FileResponse
from django.contrib.staticfiles.storage import staticfiles_storage

def resume(request):
    resume_path = "myapp/resume.pdf"  # ✅ correct path format
    
    if staticfiles_storage.exists(resume_path):
        file_path = staticfiles_storage.path(resume_path)
        with open(file_path, "rb") as resume_file:
            response = HttpResponse(resume_file.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'attachment; filename="resume.pdf"'  # ✅ fixed header
            return response
    else:
        return HttpResponse("Resume not found", status=404)
