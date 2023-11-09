#Generic API View and Model Mixin
from django.shortcuts import render
from .models import Blog
from .serializers import BlogSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

# Create your views here.

class BlogList(GenericAPIView, ListModelMixin):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
class BlogCreate(GenericAPIView, CreateModelMixin):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class BlogRetrieve(GenericAPIView, RetrieveModelMixin):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    
class BlogUpdate(GenericAPIView, UpdateModelMixin):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    
class BlogDelete(GenericAPIView, DestroyModelMixin):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    