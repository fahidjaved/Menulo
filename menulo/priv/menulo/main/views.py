from django.shortcuts import render, redirect
from .models import categories, topic, Restaurant, sub_categories, dish, review, size, price, Slider
from django.views.generic import DetailView
from django.urls import resolve
import numpy
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth, logout as de_auth
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from dynamic.models import *
from django.shortcuts import get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth import logout as auth_logout


# Create your views here.

def home(request):
    # hom=Home.objects.get()
    hom = Home.objects.all()
    if hom:
        context = {
            "welcome": hom.welcome,
            "home": hom
        }
    else:
        context = {
            "welcome": '',
            "home": hom
        }
    return render(request, 'index.html', context)


def funktioniert(request):
    home = Home.objects.get()
    context = {
        "welcome": home.welcome,
        "home": home
    }
    return render(request, 'funktioniert.html', context)


def resturent(request, slug):
    rest = Restaurant.objects.filter(slug__exact=slug).first()

    if request.method == 'POST':
        c_name = request.POST["author"]
        c_review = request.POST["comment"]
        loc = review(restaurants=rest, name=c_name, user_review=c_review)
        loc.save()
        print(c_name, c_review)
    if rest:
        rest_name = rest.id
        topi = topic.objects.filter(restaurants_id=rest_name).select_related()
        top = topic.objects.filter(restaurants_id=rest_name).select_related().first()

        main_cat = categories.objects.select_related()

        sub_cat = sub_categories.objects.select_related()

        dishes = dish.objects.select_related()
        sizes = size.objects.select_related()
        prices = price.objects.select_related()
        context = {
            "resturent": rest,
            "top": top,
            "topi": topi,
            "main_cat": main_cat,
            "sub_cat": sub_cat,
            "dish": dishes,
            "sizes": sizes,
            "prices": prices,
        }

        return render(request, 'resturent.html', context)
    else:
        return render(request, 'resturent.html')


def Kontakt(request):
    kontakt = contact.objects.get()
    if kontakt:
        context = {
            "kontakt": kontakt
        }
        return render(request, 'kontakt.html', context)
    return render(request, 'kontakt.html')


def impressum(request):
    data = imprint.objects.get()
    context = {
        "imprint": data
    }
    return render(request, 'impressum.html', context)


def agb(request):
    ag = AGB.objects.get()
    context = {
        "agb": ag
    }
    return render(request, 'agb.html', context)


def privacy(request):
    privacy = data_protection.objects.get()
    context = {
        "privacy": privacy
    }
    return render(request, 'datenschutz.html', context)


@csrf_exempt
def login(request):
    if request.user.is_authenticated:
        return redirect('main:dashboard')
    if request.method == 'POST':
        username = request.POST.get('user_login')
        password = request.POST.get('user_pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth(request, user)
            return redirect('main:dashboard')
        else:
            return render(request, 'login.html')

    return render(request, 'login.html')


def log_out(request):
    auth_logout(request)
    return redirect('main:login')


def bestellen(request):
    return render(request, 'bestellen.html')


def speisekarte(request):
    return render(request, 'speisekarte.html')


def qr_code(request):
    return render(request, 'qr_code.html')


def allgemein(request):
    return render(request, 'allgemein.html')


def zusammenstellen(request):
    return render(request, 'zusammenstellen.html')


def itemdetail1(request, slug):
    dishes = dish.objects.filter(slug__exact=slug).first()
    sub_cat = sub_categories.objects.filter(id=dishes.sub_category.id).select_related().first()
    main_cat = categories.objects.filter(id=sub_cat.category.id).first()
    top = topic.objects.filter(id=main_cat.menu.id).select_related().first()
    rest = Restaurant.objects.filter(id=top.restaurants.id).first()
    sizes = size.objects.filter(dish_id=dishes.id).select_related().all()
    topi = topic.objects.filter(Q(restaurants=rest.id) & Q(name='shisha') & Q(id=main_cat.menu.id)).first()
    # print(topi)
    if rest:
        return render(request, 'product.html', {"rest": rest, "dish": dishes, "sizes": sizes, "top": topi})
    return render(request, 'product.html')


def itemdetail2(request, slug, id):
    dishes = dish.objects.filter(slug__exact=slug).first()
    sub_cat = sub_categories.objects.filter(id=dishes.sub_category.id).select_related().first()
    main_cat = categories.objects.filter(id=sub_cat.category.id).first()
    top = topic.objects.filter(id=main_cat.menu.id).first()
    rest = Restaurant.objects.filter(id=top.restaurants.id).first()
    sizes = size.objects.filter(dish_id=dishes.id).select_related().all()
    prices = price.objects.filter(id=id).first()
    sizes = size.objects.filter(id=prices.size_id.id).first()
    # print(rest)
    if rest:
        if top == "shisha":
            law = rest.shisha_law
            return render(request, 'product.html', {"rest": rest, "dish": dishes, "sizes": sizes, "law": law})
    return render(request, 'product.html')


@login_required(login_url='/login')
def dashboard(request):
    id = request.user

    if id:

        rest = Restaurant.objects.filter(user=id).first()
        if not rest:
            return render(request, 'dashboard/price.html')
        tp = topic.objects.filter(Q(restaurants=rest.id) & ~Q(name='shisha')).all()
        top = topic.objects.filter(Q(restaurants=rest.id) & ~Q(name='shisha')).first()
        ss = topic.objects.filter(Q(restaurants=rest.id) & Q(name='shisha')).first()
        ns = topic.objects.filter(Q(restaurants=rest.id) & ~Q(name='shisha')).first()

        # print(tp)
        dishes = dish.objects.filter(restaurant=rest.id).all()

        sizes = size.objects.all()

        if request.POST.get('q'):
            query = request.GET.get('q')
            if query:
                dishi = dish.objects.filter(Q(restaurants=rest.id) & Q(title__icontains=query))
                return render(request, 'dashboard/price.html', {"dishes": tp, "search": dishi, "top": ns})
            else:
                return None

        if request.POST.get('id'):
            dishid = request.POST.get('id')
            edited_dish = dishes.get(id=dishid)
            edited_dish.price = request.POST.get('price')
            edited_dish.save()
            # return render(request, 'dashboard/price.html',{"dishes":tp,"topic":top,"rest":rest,"shisha":ss,"top":ns})

        if request.POST.get('spid'):
            pid = request.POST.get('spid')
            print(pid)
            edited_price = sizes.get(id=pid)
            edited_price.price = request.POST.get('sprice')
            edited_price.save()
            # return render(request, 'dashboard/price.html',{"dishes":tp,"topic":top,"rest":rest,"shisha":ss,"top":ns})

        return render(request, 'dashboard/price.html',
                      {"dishes": tp, "topic": top, "rest": rest, "shisha": ss, "top": ns})

    return render(request, 'dashboard/price.html')


@login_required(login_url='/login')
def shisha(request):
    user = request.user
    rest = Restaurant.objects.filter(user=user.id).first()
    if rest:
        tp = topic.objects.filter(restaurants=rest.id, name="shisha").all()
        dishes = dish.objects.filter(restaurant=rest.id).all()
        top = topic.objects.filter(Q(restaurants=rest.id) & Q(name='shisha')).first()
        ss = topic.objects.filter(Q(restaurants=rest.id) & Q(name='shisha')).first()
        ns = topic.objects.filter(Q(restaurants=rest.id) & ~Q(name='shisha')).first()

        if request.POST.get('id'):
            if request.POST.get('price') and request.POST.get('title'):
                dishid = request.POST.get('id')
                edited_dish = dishes.get(id=dishid)
                edited_dish.price = request.POST.get('price')
                edited_dish.title = request.POST.get('title')
                edited_dish.save()
                tp = topic.objects.filter(restaurants=rest.id, name="shisha").all()
                # return render(request, 'dashboard/shisha.html',{"dishes":tp,"topi":top,"rest":rest})

            if request.POST.get('price'):
                dishid = request.POST.get('id')
                edited_dish = dishes.get(id=dishid)
                edited_dish.price = request.POST.get('price')
                edited_dish.save()
                tp = topic.objects.filter(restaurants=rest.id, name="shisha").all()
                # return render(request, 'dashboard/shisha.html',{"dishes":tp,"topi":top,"rest":rest})

            if request.POST.get('title'):
                dishid = request.POST.get('id')
                edited_dish = dishes.get(id=dishid)
                edited_dish.title = request.POST.get('title')
                edited_dish.save()
                tp = topic.objects.filter(restaurants=rest.id, name="shisha").all()
                # return render(request, 'dashboard/shisha.html',{"dishes":tp,"topi":top,"rest":rest})
        return render(request, 'dashboard/shisha.html', {"dishes": tp, "rest": rest, "shisha": ss, "top": ns})

    return render(request, 'dashboard/shisha.html')


@login_required(login_url='/login')
def feedback(request):
    user = request.user
    rest = Restaurant.objects.filter(user=user.id).first()
    if rest:
        feedback = review.objects.filter(restaurants=rest.id).all()
        tp = topic.objects.filter(Q(restaurants=rest.id) & ~Q(name='shisha')).all()
        top = topic.objects.filter(Q(restaurants=rest.id) & ~Q(name='shisha')).first()
        ss = topic.objects.filter(Q(restaurants=rest.id) & Q(name='shisha')).first()
        ns = topic.objects.filter(Q(restaurants=rest.id) & ~Q(name='shisha')).first()

        if request.POST.get('id'):
            feedback_id = request.POST.get('id')
            review.objects.filter(id=feedback_id).delete()

        return render(request, 'dashboard/feedback.html', {"feedback": feedback, "rest": rest, "shisha": ss, "top": ns})

    return render(request, 'dashboard/feedback.html')


@login_required(login_url='/login')
def guests(request):
    user = request.user
    rest = Restaurant.objects.filter(user=user.id).first()
    if request.method == 'POST':
        GuestRegister.objects.filter(Q(created_at__date__gte=request.POST['to_date']) & Q(created_at__date__lte=request.POST['from_date'])).delete()
    if rest:
        guest_users = GuestRegister.objects.filter(restaurants=rest.id).all()
        tp = topic.objects.filter(Q(restaurants=rest.id) & ~Q(name='shisha')).all()
        top = topic.objects.filter(Q(restaurants=rest.id) & ~Q(name='shisha')).first()
        ss = topic.objects.filter(Q(restaurants=rest.id) & Q(name='shisha')).first()
        ns = topic.objects.filter(Q(restaurants=rest.id) & ~Q(name='shisha')).first()

        if request.POST.get('id'):
            guest_id = request.POST.get('id')
            GuestRegister.objects.get(id=guest_id).delete()

        return render(request, 'dashboard/guests.html',
                      {"guest_users": guest_users, "rest": rest, "shisha": ss, "top": ns})

    return render(request, 'dashboard/guests.html')
