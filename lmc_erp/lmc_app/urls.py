from django.urls import path
from lmc_app.views import accueil, grade, employe, employe_detail,fonction

urlpatterns = [
    path('', accueil, name="accueil"),
    path('grade', grade, name="grade"),
    path('fonction', fonction, name="fonction"),
    path('employe', employe, name="employe"),
    path('employe/<int:id>', employe_detail,name="employe_detail"),
]
