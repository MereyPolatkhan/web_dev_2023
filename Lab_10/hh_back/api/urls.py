from django.urls import path, include
from api import views

urlpatterns = [
    path('companies/', views.get_companies),
    path('companies/<int:company_id>', views.get_company),
    path('companies/<int:company_id>/vacancies', views.get_company_vacancies),

    path('vacancies/', views.get_vacancies),
    path('vacancies/<int:vacancy_id>', views.get_vacancy),
    path('vacancies/top_ten', views.get_top_ten_vacancies),
]