from django.shortcuts import render, redirect, get_object_or_404
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
    if request.method == "POST":
        Talaba.objects.create(
            ism=request.POST.get('ism'),
            kurs=request.POST.get('kurs'),
            guruh=request.POST.get('guruh'),
            telefon_raqam=request.POST.get('telefon_raqam'),
            yosh=request.POST.get('yosh'),
            kitob_soni=request.POST.get('kitob_soni'),
        )
        return redirect('talabalar')
    talabalar = Talaba.objects.all()

    search = request.GET.get('search')
    if search is not None:
        talabalar = talabalar.filter(ism__contains=search)

    context = {
        'talabalar': talabalar,
        'search': search
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


def kitob_qoshish_view(request):
    if request.method == "POST":
        kitob = Kitob.objects.create(
            nom=request.POST.get('nom'),
            janr=request.POST.get('janr'),
            sahifa=request.POST.get('sahifa'),
            muqova=request.POST.get('muqova')
        )
        muallif = get_object_or_404(Muallif, id=request.POST.get('muallif_id'))
        kitob.muallif.add(muallif)
        kitob.save()
        return redirect('kitoblar')
    context = {
        'mualliflar': Muallif.objects.all()
    }
    return render(request, 'kitob_qoshish.html', context)


def mualliflar_view(request):
    if request.method == "POST":
        if request.POST.get('tirik') == "on":
            tirik = True
        else:
            tirik = False
        Muallif.objects.create(
            ism=request.POST.get('ism'),
            millat=request.POST.get('millat'),
            jins=request.POST.get('jins'),
            kitob_soni=request.POST.get('kitob_soni'),
            t_yil=request.POST.get('t_yil'),
            tirik=tirik
        )
        return redirect('mualliflar')
    mualliflar = Muallif.objects.all()
    context = {
        'mualliflar': mualliflar
    }
    return render(request, 'mualliflar.html', context)
