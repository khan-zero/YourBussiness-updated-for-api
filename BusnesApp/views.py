from django.shortcuts import render
from .models import (
    HeroSection, Client, AboutUs, AboutUsOpp,
    WhyUS, WhyUsQA, Skills, SkillsUsage, Service,
    CallToAction, Portfolio, Member, Subscribe,
    FAQ, Contact)
# Create your views here.
def index(request):
    hero = HeroSection.objects.all()
    client = Client.objects.all()
    about_us = AboutUs.objects.all()
    about_us_opp = AboutUsOpp.objects.all()
    why_us = WhyUS.objects.all()
    why_us_qa = WhyUsQA.objects.all()
    skills = Skills.objects.all()
    skills_usage = SkillsUsage.objects.all()
    service = Service.objects.all()
    call_to_action = CallToAction.objects.all()
    portfolio = Portfolio.objects.all()
    member = Member.objects.all()
    sub = Subscribe.objects.all()
    faq = FAQ.objects.all()
    contact = Contact.objects.first()

    context = {}
    context['hero'] = hero
    context['clients'] = client
    context['about_us'] = about_us
    context['about_us_opp'] = about_us_opp
    context['why_us'] = why_us
    context['why_us_qa'] = why_us_qa
    context['skills'] = skills
    context['skills_usage'] = skills_usage
    context['services'] = service
    context['call_to_action'] = call_to_action
    context['portfolio'] = portfolio
    context['members'] = member
    context['subs'] = sub
    context['faq'] = faq
    context['contact'] = contact

    return render(request, 'front/index.html', context)