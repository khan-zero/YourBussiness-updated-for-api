from . import views
from django.urls import path

urlpatterns = [
    path('hero/list', views.hero_list),
    path('hero/detail/<int:id>/', views.hero_detail),
    path('hero/create/', views.hero_create),

    path('client/list', views.client_list),
    path('client/detail/<int:id>/', views.client_detail),
    path('client/create/', views.client_create),

    path('about/list', views.about_list),
    path('about/detail/<int:id>/', views.about_detail),
    path('about/create/', views.about_create),

    path('aboutOPP/list', views.about_us_opp_list),
    path('aboutOPP/detail/<int:id>/', views.about_us_opp_detail),
    path('aboutOPP/create/', views.about_us_opp_create),

    path('whyUS/list', views.why_list),
    path('whyUS/detail/<int:id>/', views.why_detail),
    path('whyUS/create/', views.why_create),

    path('whyQA/list', views.why_qa_list),
    path('whyQA/detail/<int:id>/', views.why_qa_detail),
    path('whyQA/create/', views.why_qa_create),

    path('skills/list', views.skills_list),
    path('skills/detail/<int:id>/', views.skills_detail),
    path('skills/create/', views.skills_create),

    path('skillsUsage/list', views.skill_usage_list),
    path('skillsUsage/detail/<int:id>/', views.skills_usage_detail),
    path('skillsUsage/create/', views.skills_usage_create),

    path('service/list', views.servie_list),
    path('service/detail/<int:id>/', views.servie_detail),
    path('service/create/', views.servie_create),

    #call to action
    path('cta/list', views.servie_list),
    path('cta/detail/<int:id>/', views.servie_detail),
    path('cta/create/', views.servie_create),

    path('portfolio/list', views.portfolio_list),
    path('portfolio/detail/<int:id>/', views.portfolio_detail),
    path('portfolio/create/', views.portfolio_create),

    path('member/list', views.member_list),
    path('member/detail/<int:id>/', views.member_detail),
    path('member/create/', views.member_create),

    path('faq/list', views.faq_list),
    path('faq/detail/<int:id>/', views.faq_detail),
    path('faq/create/', views.faq_create),

    path('contact/list', views.contact_list),
    path('contact/detail/<int:id>/', views.contact_detail),
    path('contact/create/', views.contact_create),

    path('contact/list', views.contact_list),
    path('contact/detail/<int:id>/', views.contact_detail),
    path('contact/create/', views.contact_create),

    path('fooder/list', views.fooder_list),
    path('fooder/detail/<int:id>/', views.fooder_detail),
    path('fooder/create/', views.fooder_create),


    #dashboard
    path('activity/list', views.activity_list),
    path('activity/detail/<int:id>/', views.activity_detail),
    path('activity/create/', views.activity_create),
]
