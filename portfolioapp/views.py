from django.shortcuts import redirect, render

from portfolioapp.models import Projects, Query, Skills, Testimonial

# Create your views here.
def home(request):
    skills = Skills.objects.all()
    testimonial = Testimonial.objects.all()
    projects = Projects.objects.all()
    return render(request,'index.html',{'skills':skills,'projects':projects,'testimonial':testimonial})

def add(request):
    if request.method=="POST":
        name = request.POST['name']
        desc = request.POST['desc']
        info = request.POST['info']
        img = request.FILES['image']
        d = Testimonial(name=name,pic=img,desc=desc,info=info)
        d.save()
    return redirect("/")

def query(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        d = Query(name=name,email=email,message=message)
        d.save()
    return redirect("/")