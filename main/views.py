from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import *


def test_view(request):
    talabalar = Talaba.objects.all()
    temp = ""
    for i, talaba in enumerate(talabalar):
        temp += f"<p>{i + 1}. {talaba.ism} [{talaba.kurs}-kurs]</p>\n"
    return HttpResponse(
        f'''
        <h3>Talabalar ro'yxati</h3>
        {temp}
        '''
    )


def home_view(request):
    return render(request, 'home.html')


def talabalar_view(request):
    talabalar = Talaba.objects.all()
    context = {
        'talabalar': talabalar
    }
    return render(request, 'talabalar.html', context)


def talaba_details_view(request, talaba_id):
    talaba = Talaba.objects.get(id=talaba_id)
    context = {
        'talaba': talaba
    }
    return render(request, 'talaba_details.html', context)



def kitoblar_view(request):
    kitoblar = Kitob.objects.all()
    context = {
        'kitoblar': kitoblar
    }
    return render(request, 'kitoblar.html', context)