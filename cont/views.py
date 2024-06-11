from django.shortcuts import render

def contact(request):
    # if request.method=="POST":
    #     print("Hello")
    return render(request,'cont/contact.html')