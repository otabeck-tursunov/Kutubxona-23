from django.contrib import admin
from django.urls import path

from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', test_view),
    path('', home_view),
    path('talabalar/', talabalar_view, name='talabalar'),
    path('talabalar/<int:talaba_id>/', talaba_details_view),
    path('kitoblar/', kitoblar_view, name='kitoblar'),
    path("kitob-qo'shish/", kitob_qoshish_view, name='kitob-qoshish'),
    path('mualliflar/', mualliflar_view, name='mualliflar'),
]
