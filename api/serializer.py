from rest_framework.serializers import ModelSerializer, Serializer
from BusnesApp.models import (
    HeroSection, DashActivities, Client, AboutUs, AboutUsOpp,
    WhyUS, WhyUsQA, Skills, SkillsUsage, Service, CallToAction,
    Portfolio, Member, Subscribe, FAQ, Contact, FooterLiks
    )
from rest_framework import serializers

class HeroSectionSerializer(ModelSerializer):
    class Meta:
        model = HeroSection
        fields = '__all__'

class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class AboutUsSerializer(ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'


class AboutUsOppSerializer(ModelSerializer):
    class Meta:
        model = AboutUsOpp
        fields = '__all__'
        

class WhyUSSerializer(ModelSerializer):
    class Meta:
        model = WhyUS
        fields = '__all__'


class WhyUsQASerializer(ModelSerializer):
    class Meta:
        model = WhyUsQA
        fields = '__all__'
        
class SkillsSerializer(ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'


class SkillsUsageSerializer(ModelSerializer):
    class Meta:
        model = SkillsUsage
        fields = '__all__'
        
class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class CallToActionSerializer(ModelSerializer):
    class Meta:
        model = CallToAction
        fields = '__all__'

class CallToActionSerializer(ModelSerializer):
    class Meta:
        model = CallToAction
        fields = '__all__'

class PortfolioSerializer(ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'

class MemberSerializer(ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

class SubscribeSerializer(ModelSerializer):
    class Meta:
        model = Subscribe
        fields = '__all__'

class FAQSerializer(ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class FooterLiksSerializer(ModelSerializer):
    class Meta:
        model = FooterLiks
        fields = '__all__'


class DashActivitiesSerializer(Serializer):
    message = serializers.IntegerField()
    notification = serializers.IntegerField()
    
