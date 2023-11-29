from django.urls import path
from .views import index


urlpatterns =[
    #path('user/<str:name><int:age>', index , name='home')#http://127.0.0.1:8000/app/user/TOM
    path('user/<str:name>', index , name='home'),
    path('user', index , name='home')

]