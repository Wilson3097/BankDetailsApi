from django.urls import path
from .views import *

urlpatterns = [path("getDetailsFromIFSC/", GetDetailsFromIFSC.as_view()),
               path("getDetailsFromNameCity/",
                    GetDetailsFromNameAndCity.as_view()),
               path("getAllBanks/", GetAllBanks.as_view())]
