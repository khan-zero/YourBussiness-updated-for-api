from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard_index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.log_out, name='logout'),

    path('portfolio/', views.portfolio_list, name='portfolio_list'),
    path('portfolio/create/', views.portfolio_create, name='portfolio_create'),
    path('portfolio/update/<int:pk>/', views.portfolio_update, name='portfolio_update'),
    path('portfolio/delete/<int:pk>/', views.portfolio_delete, name='portfolio_delete'),

    path('member/', views.member_list, name='member_list'),
    path('member/create/', views.member_create, name='member_create'),
    path('member/update/<int:pk>/', views.member_update, name='member_update'),
    path('member/delete/<int:pk>/', views.member_delete, name='member_delete'),

    path('faqs/', views.faq_list, name='faq_list'),
    path('faqs/create/', views.faq_create, name='faq_create'),
    path('faqs/<int:pk>/update/', views.faq_update, name='faq_update'),
    path('faqs/<int:pk>/delete/', views.faq_delete, name='faq_delete'),
]
