from django.urls import path
from .views import *

urlpatterns = [path("crudBank/", CRUDBank.as_view()),
               path("crudBank/<int:bankId>/", CRUDBank.as_view()),
               path("getDetailsFromIFSC/", GetDetailsFromIFSC.as_view()),
               path("getDetailsFromNameCity/",
                    GetDetailsFromNameAndCity.as_view()),
               # path("getAllBanks/", GetAllBanks.as_view())]
               ]
