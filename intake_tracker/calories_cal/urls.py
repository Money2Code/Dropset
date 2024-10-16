from django.urls import path
from . import views

urlpatterns = [
    path('log/', views.log_calorie_intake, name='log_calorie_intake'),
    path('progress/', views.calories_progress, name='calories_progress'),
    path('index/', views.index , name='index'),
    path('signup/', views.signup, name='signup'),
    path('handlelogin/', views.handlelogin, name='handlelogin'),  # Add this line to include the login URL
    path('handlelogout/', views.handlelogout, name='handlelogout'), 
    path('diet',views.diet_plan_view,name="calculate_diet_plan") # Add this line to include the logout URL
]
