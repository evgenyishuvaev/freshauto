from django.urls import path

from .views import LoginUser, logout_page


urlpatterns = [

    path('login_page/', LoginUser.as_view(), name='login_page'),
    path('logout/', logout_page, name='logout_handler')
]
