from tastypie.resources import ModelResource
from marketplace.models import Category, Computer, Monitor
from .authentication import CustomAuthentication
from tastypie.authorization import Authorization


class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'categories'
        allowed_methods = ['get']


class ComputerResource(ModelResource):
    class Meta:
        queryset = Computer.objects.all()
        resource_name = 'computers'
        allowed_methods = ['get', 'post', 'delete']
        authentication = CustomAuthentication()
        authorization = Authorization()


class MonitorResource(ModelResource):
    class Meta:
        queryset = Monitor.objects.all()
        resource_name = 'monitors'
        allowed_methods = ['get', 'post', 'delete']
        authentication = CustomAuthentication()
        authorization = Authorization()
