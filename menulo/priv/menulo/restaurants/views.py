from django.shortcuts import render, redirect
from main.models import categories, topic, Restaurant, sub_categories, dish, review, size, price, Slider, GuestRegister
from django.views.generic import DetailView
from django.urls import resolve
import numpy
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth, logout as de_auth
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User


# Create your views here.


def resturent(request, slug):
    url_slug = slug
    if url_slug == 'weko':
        return redirect('weko/')
    else:
        rest = Restaurant.objects.filter(slug__exact=slug).first()

        if rest:
            current_user = User.objects.filter(id=rest.user.id).first()
            user_email = current_user.email

            if request.method == 'POST':

                if request.POST.get('guest', 'false') == 'true':
                    guest_register = GuestRegister(vorname=request.POST.get('vorname', ''),
                                                   nachname=request.POST.get('nachname', ''),
                                                   Adresse=request.POST.get('adresse', ''),
                                                   tel=request.POST.get('tel', ''),
                                                   email=request.POST.get('email', ''),
                                                   restaurants=rest)

                    guest_register.save()
                else:
                    c_name = request.POST["author"]
                    c_review = request.POST["comment"]
                    loc = review(restaurants=rest, name=c_name, user_review=c_review)
                    loc.save()
                    print(c_name, c_review)

                    if user_email:
                        subject = 'Feedback'
                        message = c_review
                        email_from = settings.EMAIL_HOST_USER
                        recipient_list = [user_email, ]
                        send_mail(subject, message, email_from, recipient_list)

            rest_name = rest.id
            topi = topic.objects.filter(restaurants_id=rest_name).select_related()
            top = topic.objects.filter(restaurants_id=rest_name).select_related().first()
            slider_list = Slider.objects.filter(restaurants_id=rest_name).all()
            slider_first = Slider.objects.filter(restaurants_id=rest_name).first()

            main_cat = categories.objects.select_related()

            sub_cat = sub_categories.objects.select_related()

            dishes = dish.objects.select_related()
            sizes = size.objects.select_related()
            prices = price.objects.select_related()
            context = {
                "resturent": rest,
                "sl_f": slider_first,
                "sl_all": slider_list,
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
