from django.urls import path
from .views import article_list, article_details, ArticleAPIView, GenericAPIView

urlpatterns = [
    path('articles', article_list),
    path('articlesapi', ArticleAPIView.as_view()),
    path('articlesgen/<int:id>', GenericAPIView.as_view()),
    path('article/<int:id>', article_details),
]
