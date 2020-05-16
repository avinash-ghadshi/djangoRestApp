from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, mixins, generics
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Article
from .serializers import ArticleSerializer


#----- generic api view with mixins -----
class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):

    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    
    lookup_field = 'id'
    allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')
    
    def get(self, request, id=None):
        
        if id:
            return self.retrieve(request, id)
        else:
            return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
    def put(self, request, id):
        return self.update(request, id)
    
    def delete(self, request, id):
        return self.destroy(request, id)
        

#----- class based api view -----
class ArticleAPIView(APIView):
    
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        article = Article.objects.all()
        serialize = ArticleSerializer(article, many=True)
        return Response(serialize.data)
    
    def post(self, request):
        serialize = ArticleSerializer(data=request.data)
        
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)


#----- api_view function for api -----    
@api_view(['GET','POST'])
def article_list(request):
    
    if request.method == 'GET':
        article = Article.objects.all()
        serialize = ArticleSerializer(article, many=True)
        return Response(serialize.data)
    
    elif request.method == 'POST':
        #data = JSONParser().parse(request)  --- Not needed in api_view functions
        serialize = ArticleSerializer(data=request.data)
        
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)
 
#----- Simple function for api -----
@csrf_exempt
def article_details(request, id):
    
    try:
        article = Article.objects.get(pk=id)
    except Article.DoesNotExist:
        return HttpResponse(status=404)
    
    
    if request.method == 'GET':
        serialize = ArticleSerializer(article)
        return JsonResponse(serialize.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serialize = ArticleSerializer(article, data=data)
        
        if serialize.is_valid():
            serialize.save()
            return JsonResponse(serialize.data, status=200)
        
        return JsonResponse(serialize.errors, status=400)
    
    elif request.method == 'DELETE':
        article.delete()
        return HttpResponse(status=204)