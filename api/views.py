from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import (
    HeroSectionSerializer, DashActivitiesSerializer, ClientSerializer,
    AboutUsSerializer, AboutUsOppSerializer, WhyUSSerializer, WhyUsQASerializer,
    SkillsSerializer, SkillsUsageSerializer, ServiceSerializer, CallToActionSerializer,
    PortfolioSerializer, MemberSerializer, SubscribeSerializer, FAQSerializer,
    ContactSerializer, FooterLiksSerializer
    )


from BusnesApp.models import (
    HeroSection, DashActivities, Client, AboutUs, AboutUsOpp, WhyUS, WhyUsQA, Skills,
    SkillsUsage, Service, CallToAction, Portfolio, Member, Subscribe, FAQ, Contact,
    FooterLiks
    )

@api_view(['GET'])
def hero_list(request):
    hero_section = HeroSection.objects.all()
    serializer_data = HeroSectionSerializer(hero_section, many = True)
    
    return Response(serializer_data.data)

@api_view(['GET'])
def hero_detail(request, id):
    hero = HeroSection.objects.get(id=id)
    ser_data = HeroSectionSerializer(hero)

    return Response(ser_data.data)

@api_view(['POST'])
def hero_create(request):
    ser_data = HeroSectionSerializer(data=request.data)
    if ser_data.is_valid():
        ser_data.save()

    return Response({'satus':201})




@api_view(['GET'])
def client_list(request):
    client_section = Client.objects.all()
    serializer_data = ClientSerializer(client_section, many=True)

    return Response(serializer_data.data)

@api_view(['GET'])
def client_detail(request, id):
    client = Client.objects.get(id=id)
    ser_data = ClientSerializer(client)

    return Response(ser_data.data)


@api_view(['POST'])
def client_create(request):
    ser_data = ClientSerializer(data=request.data)
    if ser_data.is_valid():
        ser_data.save()

    return Response({'satus': 201})




@api_view(['GET'])
def about_list(request):
    about_section = AboutUs.objects.all()
    serializer_data = AboutUsSerializer(about_section, many=True)

    return Response(serializer_data.data)


@api_view(['GET'])
def about_detail(request, id):
    about = AboutUs.objects.get(id=id)
    ser_data = AboutUsSerializer(about)

    return Response(ser_data.data)


@api_view(['POST'])
def about_create(request):
    ser_data = AboutUsSerializer(data=request.data)
    if ser_data.is_valid():
        ser_data.save()

    return Response({'satus': 201})





@api_view(['GET'])
def about_us_opp_list(request):
    about_us_opp_section = AboutUsOpp.objects.all()
    serializer_data = AboutUsOppSerializer(about_us_opp_section, many=True)

    return Response(serializer_data.data)


@api_view(['GET'])
def about_us_opp_detail(request, id):
    about = AboutUsOpp.objects.get(id=id)
    ser_data = AboutUsOppSerializer(about)

    return Response(ser_data.data)


@api_view(['POST'])
def about_us_opp_create(request):
    ser_data = AboutUsSerializer(data=request.data)
    if ser_data.is_valid():
        ser_data.save()

    return Response({'satus': 201})




@api_view(['GET'])
def why_list(request):
    why_section = WhyUS.objects.all()
    serializer_data = WhyUSSerializer(why_section, many=True)

    return Response(serializer_data.data)


@api_view(['GET'])
def why_detail(request, id):
    why = WhyUS.objects.get(id=id)
    ser_data = WhyUSSerializer(why)

    return Response(ser_data.data)


@api_view(['POST'])
def why_create(request):
    ser_data = WhyUSSerializer(data=request.data)
    if ser_data.is_valid():
        ser_data.save()

    return Response({'satus': 201})




@api_view(['GET'])
def why_qa_list(request):
    why_section = WhyUsQA.objects.all()
    serializer_data = WhyUsQASerializer(why_section, many=True)

    return Response(serializer_data.data)


@api_view(['GET'])
def why_qa_detail(request, id):
    why_qa = WhyUsQA.objects.get(id=id)
    ser_data = WhyUSSerializer(why_qa)

    return Response(ser_data.data)


@api_view(['POST'])
def why_qa_create(request):
    ser_data = WhyUSSerializer(data=request.data)
    if ser_data.is_valid():
        ser_data.save()

    return Response({'satus': 201})




@api_view(['GET'])
def skills_list(request):
    skills_section = Skills.objects.all()
    serializer_data = SkillsSerializer(skills_section, many=True)

    return Response(serializer_data.data)


@api_view(['GET'])
def skills_detail(request, id):
    skills = Skills.objects.get(id=id)
    ser_data = SkillsSerializer(skills)

    return Response(ser_data.data)


@api_view(['POST'])
def skills_create(request):
    ser_data = SkillsSerializer(data=request.data)
    if ser_data.is_valid():
        ser_data.save()

    return Response({'satus': 201})




@api_view(['GET'])
def skill_usage_list(request):
    skill_usage_section = SkillsUsage.objects.all()
    serializer_data = SkillsUsageSerializer(skill_usage_section, many=True)

    return Response(serializer_data.data)


@api_view(['GET'])
def skills_usage_detail(request, id):
    skill_usage = SkillsUsage.objects.get(id=id)
    ser_data = SkillsUsageSerializer(skill_usage)

    return Response(ser_data.data)


@api_view(['POST'])
def skills_usage_create(request):
    ser_data = SkillsUsageSerializer(data=request.data)
    if ser_data.is_valid():
        ser_data.save()

    return Response({'satus': 201})



@api_view(['GET'])
def servie_list(request):
    service_section = Service.objects.all()
    serializer_data = ServiceSerializer(service_section, many=True)

    return Response(serializer_data.data)


@api_view(['GET'])
def servie_detail(request, id):
    servie_usage = Service.objects.get(id=id)
    ser_data = ServiceSerializer(servie_usage)

    return Response(ser_data.data)


@api_view(['POST'])
def servie_create(request):
    ser_data = ServiceSerializer(data=request.data)
    if ser_data.is_valid():
        ser_data.save()

    return Response({'satus': 201})


@api_view(['GET'])
def cta_list(request):
    cta_section = CallToAction.objects.all()
    serializer_data = CallToActionSerializer(cta_section, many=True)

    return Response(serializer_data.data)


@api_view(['GET'])
def cta_detail(request, id):
    servie_usage = CallToAction.objects.get(id=id)
    ser_data = CallToActionSerializer(servie_usage)

    return Response(ser_data.data)


@api_view(['POST'])
def cta_create(request):
    ser_data = CallToActionSerializer(data=request.data)
    if ser_data.is_valid():
        ser_data.save()

    return Response({'satus': 201})


@api_view(['GET'])
def portfolio_list(request):
    portfolio_section = Portfolio.objects.all()
    serializer_data = PortfolioSerializer(portfolio_section, many=True)

    return Response(serializer_data.data)


@api_view(['GET'])
def portfolio_detail(request, id):
    servie_usage = Portfolio.objects.get(id=id)
    ser_data = PortfolioSerializer(servie_usage)

    return Response(ser_data.data)


@api_view(['POST'])
def portfolio_create(request):
    ser_data = PortfolioSerializer(data=request.data)
    if ser_data.is_valid():
        ser_data.save()

    return Response({'satus': 201})



@api_view(['GET'])
def member_list(request):
    member_section = Member.objects.all()
    serializer_data = MemberSerializer(member_section, many=True)

    return Response(serializer_data.data)


@api_view(['GET'])
def member_detail(request, id):
    servie_usage = Member.objects.get(id=id)
    ser_data = MemberSerializer(servie_usage)

    return Response(ser_data.data)


@api_view(['POST'])
def member_create(request):
    ser_data = MemberSerializer(data=request.data)
    if ser_data.is_valid():
        ser_data.save()

    return Response({'satus': 201})


@api_view(['GET'])
def subscribe_list(request):
    subscribe_section = Subscribe.objects.all()
    serializer_data = SubscribeSerializer(subscribe_section, many=True)

    return Response(serializer_data.data)


@api_view(['GET'])
def subscribe_detail(request, id):
    servie_usage = Subscribe.objects.get(id=id)
    ser_data = SubscribeSerializer(servie_usage)

    return Response(ser_data.data)


@api_view(['POST'])
def subscribe_create(request):
    ser_data = SubscribeSerializer(data=request.data)
    if ser_data.is_valid():
        ser_data.save()

    return Response({'satus': 201})


@api_view(['GET'])
def faq_list(request):
    faq_section = FAQ.objects.all()
    serializer_data = FAQSerializer(faq_section, many=True)

    return Response(serializer_data.data)


@api_view(['GET'])
def faq_detail(request, id):
    servie_usage = FAQ.objects.get(id=id)
    ser_data = FAQSerializer(servie_usage)

    return Response(ser_data.data)


@api_view(['POST'])
def faq_create(request):
    ser_data = FAQSerializer(data=request.data)
    if ser_data.is_valid():
        ser_data.save()

    return Response({'satus': 201})



@api_view(['GET'])
def contact_list(request):
    contact_section = Contact.objects.all()
    serializer_data = ContactSerializer(contact_section, many=True)

    return Response(serializer_data.data)


@api_view(['GET'])
def contact_detail(request, id):
    servie_usage = Contact.objects.get(id=id)
    ser_data = ContactSerializer(servie_usage)

    return Response(ser_data.data)


@api_view(['POST'])
def contact_create(request):
    ser_data = ContactSerializer(data=request.data)
    if ser_data.is_valid():
        ser_data.save()

    return Response({'satus': 201})



@api_view(['GET'])
def fooder_list(request):
    fooder_section = FooterLiks.objects.all()
    serializer_data = FooterLiksSerializer(fooder_section, many=True)

    return Response(serializer_data.data)


@api_view(['GET'])
def fooder_detail(request, id):
    servie_usage = FooterLiks.objects.get(id=id)
    ser_data = FooterLiksSerializer(servie_usage)

    return Response(ser_data.data)


@api_view(['POST'])
def fooder_create(request):
    ser_data = FooterLiksSerializer(data=request.data)
    if ser_data.is_valid():
        ser_data.save()

    return Response({'satus': 201})



#buni qayerdadur hato borga ohshayapti topalmadim | this one isn't working so, you can cange on serializer
@api_view(['GET'])
def activity_list(request):
    activity_section = DashActivities.objects.all()
    serializer_data = DashActivitiesSerializer(activity_section, many=True)

    return Response(serializer_data.data)

@api_view(['GET'])
def activity_detail(request, id):
    activity_section = DashActivities.objects.get(id=id)
    ser_data = DashActivitiesSerializer(activity_section)

    return Response(ser_data.data)


@api_view(['POST'])
def activity_create(request):
    ser_data = DashActivitiesSerializer(data=request.data)
    if ser_data.is_valid():
        ser_data.save()

    return Response({'satus': 201})