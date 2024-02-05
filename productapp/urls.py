
from django.urls import path
from productapp import views


rng_path1 = 'sdlkfjsldfjweuiriouvnxncmvn121jlkjsdlfj7897sdfnlkqwejrilqweuorflkdngvldjfjgl;eowurp'
rng_path2 = 'aaiokijjkwiuejdnvkdlowqp'

urlpatterns = [
    path('',views.index),
    path(f'details/<id>/',views.details),
   
 
    
]
