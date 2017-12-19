from django.conf.urls import url
from pincodes import views as pincode_views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include
from django.contrib.auth import views as auth_views
#from rest_framework.swagger.views import get_swagger_view
# API endpoints
#schema_view = get_swagger_view(title='Pincode API')
urlpatterns = format_suffix_patterns([
    #url(r'^$', schema_view),
    #url(r'^pincodes/$', pincode_views.pincode_list, name='pincode_list'),
    #url(r'^$', views.api_root),
    url(r'^pincodes/$',pincode_views.PincodeList.as_view(),name='pincode-list'),
    url(r'^pincodes/(?P<pincode>[0-9]+)/$',pincode_views.PincodeDetail.as_view(),name='pincode-detail'),
    #url(r'^users/$',views.UserList.as_view(),name='user-list'),
    #url(r'^users/(?P<pk>[0-9]+)/$',views.UserDetail.as_view(),name='user-detail'),
    #url(r'^pincodes/(?P<pincode>[0-9]+)/$', pincode_views.pincode_detail, name='pincode_detail'), 
])

# Login and logout views for the browsable API
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]




