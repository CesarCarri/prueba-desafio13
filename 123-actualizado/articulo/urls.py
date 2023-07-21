from django.urls import path
from .views import  listar_articulos_por_categoria, listar_articulos_por_categorias, listar_categorias, ArtListView, ArtCreateView, AllArticlesView, AllCategoriaView, CategoryCreateView, ArtDetailView, ArtUpdateView, ArtDeleteView

app_name="articulos"

urlpatterns = [
    path('', ArtListView.as_view(), name="home"),
    path('create/', ArtCreateView.as_view(), name="create"),
    path('all-articles/', AllArticlesView.as_view(), name="all_articles"),
    path('all-category/', AllCategoriaView.as_view(), name="all_category"),
    path('create-category/', CategoryCreateView.as_view(), name="create_category"),
    path('Article/<int:post_id>/', ArtDetailView.as_view(), name="detail"),
    path('<int:pk>/update/', ArtUpdateView.as_view(), name="update"),
    path('<int:pk>/delete/', ArtDeleteView.as_view(), name="delete"),

    path('categorias/', listar_categorias.as_view(), name='listar_categorias'),
    path('categoria/<int:categoria_id>/', listar_articulos_por_categorias.as_view(), name='listar_articulos_por_categorias'),
]