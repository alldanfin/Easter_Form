from django.shortcuts import render
from eggform.forms import EggForm

def index(request):
    form = EggForm()

    if request.method == "POST":
        form = EggForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return thankyou(request)
        else:
            print('ERROR FORM INVALID')

    return render(request,'eggform/index.html',{'form':form})


def thankyou(request):
    return render(request,'eggform/thankyou.html')
