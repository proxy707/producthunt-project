
from django.contrib import admin
from django.urls import path,include
from products import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('create',views.create,name='create'),
    path('<int:product_id>', views.detail, name ='detail'),
    path('<int:product_id>/upvote', views.upvote, name ='upvote'),  
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)