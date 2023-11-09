from django.urls import path
from apiapp import views
urlpatterns = [
    path('blogapi/', views.BlogList.as_view(), name = 'blogapi'),
    path('createblog/', views.BlogCreate.as_view(), name = 'createblog'),
    path('retrieveblog/<int:pk>', views.BlogRetrieve.as_view(), name='retriveblog'),
    path('updateblog/<int:pk>', views.BlogUpdate.as_view(), name = 'updateblog'),
    path('deleteblog/<int:pk>', views.BlogDelete.as_view(), name = 'deleteblog')
]
