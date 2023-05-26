from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from django.conf.urls.static import static
from django3dlab import settings
from user.views import *
from order.views import *

urlpatterns = [
    path('api/v1/user/', UserAPIList.as_view()),
    path('api/v1/order/create/', FileUploadView.as_view()),
    path('api/v1/order/list/', FileUploadViewList.as_view()),
    path('api/v1/order/<int:pk>/', FileUploadViewDetailCheck.as_view()),
    path('api/v1/order/<int:pk>/done/', status, ),
    path('api/v1/order/<int:pk>/reject/', reject, ),
    path('api/v1/auth/', include('djoser.urls')),  # new
    path('api/v1/auth/register/', RegisterApi.as_view()),  # new
    path('api/v1/auth/login/', UserLoginApi.as_view()),  # new
    path('api/v1/auth/logout/', UserLogoutApi.as_view()),  # new
    re_path(r'^auth/', include('djoser.urls.authtoken')),  # new
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
