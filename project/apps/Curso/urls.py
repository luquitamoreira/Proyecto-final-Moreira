from django.urls import path
from . import views
from django.views.generic import TemplateView   
app_name="Curso"
urlpatterns=  [ path("",views.index,name="home")] 

urlpatterns += [
    path('', TemplateView.as_view(template_name="Curso/index.html"),name='home'),
    path('cursocategoria/list/',views.CursoCategoriaList.as_view(),name='cursocategoria_list'),
    path('cursocategoria/create/', views.CursoCategoriaCreate.as_view(),name='cursocategoria_create'),
    path("cursocategoria/detail/<int:pk>", views.CursoCategoriaDetail.as_view(),name="cursocategoria_detail"),
    path("cursocategoria/update/<int:pk>", views.CursoCategoriaUpdate.as_view(),name="cursocategoria_update"),
    path("cursocategoria/delete/<int:pk>", views.CursoCategoriaDelete.as_view(),name="cursocategoria_delete"),
]

urlpatterns+= [
   
    path('curso/list/', views.CursoList.as_view(),
         name='curso_list'),
    path('curso/create/', views.CursoCreate.as_view(),
         name='curso_create'),
    path("curso/detail/<int:pk>", views.CursoDetail.as_view(),
         name="curso_detail"),
    path("curso/update/<int:pk>", views.CursoUpdate.as_view(),
         name="curso_update"),
    path("curso/delete/<int:pk>", views.CursoDelete.as_view(),
         name="curso_delete"),
]