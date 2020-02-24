from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from classes import views
from API import views as apiviews
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('classrooms/', views.classroom_list, name='classroom-list'),
    path('classrooms/<int:classroom_id>/', views.classroom_detail, name='classroom-detail'),

    path('classrooms/create', views.classroom_create, name='classroom-create'),
    path('classrooms/<int:classroom_id>/update/', views.classroom_update, name='classroom-update'),
    path('classrooms/<int:classroom_id>/delete/', views.classroom_delete, name='classroom-delete'),

    path('api/classrooms/', apiviews.ListView.as_view(), name='api-classroom-list'),
    path('api/classrooms/<int:classroom_id>/', apiviews.DetailView.as_view(), name='api-classroom-detail'),

    path('api/create/', apiviews.CreateView.as_view(), name='api-classroom-create'),
    path('api/classrooms/<int:classroom_id>/update/', apiviews.UpdateView.as_view(), name='api-classroom-update'),
    path('api/classrooms/<int:classroom_id>/delete/', apiviews.DeleteView.as_view(), name='api-classroom-delete'),

    path('api/token /', TokenObtainPairView.as_view(), name="api-login"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name="token-refresh"),
]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
