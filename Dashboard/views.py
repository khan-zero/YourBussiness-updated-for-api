from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from BusnesApp.models import Portfolio, Member, DashActivities, FAQ
from BusnesApp.forms import PortfolioForm, MemberForm, FAQForm

@login_required(login_url='login')
def index(request):
    activity = DashActivities.objects.first()
    context = {"activities" : activity}


    return render(request, 'dash/index.html', context)

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')

        # Maydonlar bo'shlikka tekshirish
        if not username or not email or not password or not confirm_password:
            text = "All fields are required."
            return render(request, 'dash/404.html', {'message': text})

        # Foydalanuvchi nomi allaqachon olinganligini tekshirish
        if User.objects.filter(username=username).exists():
            text = "Bu username allaqachon mavjud."
            return render(request, 'dash/404.html', {'message': text})

        # email adresni uniquelikka tekshirish
        if User.objects.filter(email=email).exists():
            text = "Bu email allaqachon mavjud."
            return render(request, 'dash/404.html', {'message': text})

        # parolni mosligiga tekshirish
        if password != confirm_password:
            text = "Parolingiz birbiriga mos kelmadi."
            return render(request, 'dash/404.html', {'message': text})

        # parol uzunligigga limit ornatish (hozircha kk emas)
        """
        if len(password) < 8:
            text = "Parolingiz 8 ta "
            return render(request, 'dash/error.html', {'message': text})
        """

        try:
            hashed_password = make_password(password)

            user = User.objects.create_user(
                username=username,
                email=email,
                password=hashed_password
            )
            login(request, user)
            return redirect('index')
        except ValidationError as e:

            text = "There was a problem creating your account. Please try again."
            return render(request, 'dash/404.html', {'message': text})


    return render(request, 'dash/register.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            text = "Siz allaqachon registratsiyadan o'tgansiz yoki Ummuman o'tmagansiz"
            return render(request, "dash/404.html", {"message": text})
    return render(request, 'dash/login.html')

def log_out(request):
    logout(request)
    return redirect('index')


# Portfolio Views
def portfolio_list(request):
    portfolios = Portfolio.objects.all()
    return render(request, 'dash/portfolio_list.html', {'portfolios': portfolios})

def portfolio_create(request):
    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('portfolio_list')
    else:
        form = PortfolioForm()
    return render(request, 'dash/portfolio_form.html', {'form': form})

def portfolio_update(request, pk):
    portfolio = get_object_or_404(Portfolio, pk=pk)
    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES, instance=portfolio)
        if form.is_valid():
            form.save()
            return redirect('portfolio_list')
    else:
        form = PortfolioForm(instance=portfolio)
    return render(request, 'dash/portfolio_form.html', {'form': form})

def portfolio_delete(request, pk):
    portfolio = get_object_or_404(Portfolio, pk=pk)
    if request.method == 'POST':
        portfolio.delete()
        return redirect('portfolio_list')
    return render(request, 'dash/portfolio_confirm_delete.html', {'portfolio': portfolio})

# Member Views
def member_list(request):
    members = Member.objects.all()
    return render(request, 'dash/member_list.html', {'members': members})

def member_create(request):
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberForm()
    return render(request, 'dash/member_form.html', {'form': form})

def member_update(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberForm(instance=member)
    return render(request, 'dash/member_form.html', {'form': form})

def member_delete(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        member.delete()
        return redirect('member_list')
    return render(request, 'dash/member_confirm_delete.html', {'member': member})
    
    
def faq_list(request):
    faqs = FAQ.objects.all()
    return render(request, 'dash/faq_list.html', {'faqs': faqs})


def faq_create(request):
    if request.method == 'POST':
        form = FAQForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('faq_list')
    else:
        form = FAQForm()
    return render(request, 'dash/faq_form.html', {'form': form, 'title': 'Create FAQ'})


def faq_update(request, pk):
    faq = get_object_or_404(FAQ, pk=pk)
    if request.method == 'POST':
        form = FAQForm(request.POST, instance=faq)
        if form.is_valid():
            form.save()
            return redirect('faq_list')
    else:
        form = FAQForm(instance=faq)
    return render(request, 'dash/faq_form.html', {'form': form, 'title': 'Update FAQ'})


def faq_delete(request, pk):
    faq = get_object_or_404(FAQ, pk=pk)
    if request.method == 'POST':
        faq.delete()
        return redirect('faq_list')
    return render(request, 'dash/faq_confirm_delete.html', {'faq': faq})
