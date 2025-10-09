from django.contrib import admin 
from django.urls import path 
from myapp import views 
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('calculate_bmi/',views.calculate_bmi,name="calculate_bmi"),
    path('',views.calculate_bmi,name="calculate_bmi")
]