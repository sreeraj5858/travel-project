# from django.http import HttpResponse
# from django.shortcuts import render
#
# # Create your views here.
# def demo(request):
#     return HttpResponse("hello world")


from django.http import HttpResponse
from django.shortcuts import render
from .models import place
from .models import team

# Create your views here.
def demo(request):
    obj=place.objects.all()
    obj2=team.objects.all()
    return render(request,"index.html",{'result':obj,'result2':obj2})


#
# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res1 =x-y
#
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res2=x*y
#
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res3=x/y
#
#     return render(request,"result.html",{'result':res,'result1':res1,'result2':res2,'result3':res3})
#
#
#
#
