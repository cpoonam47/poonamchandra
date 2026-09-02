from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact,GalleryImage
from django.http import HttpResponse
from django.shortcuts import render
from .models import Visitor


def index(request):
    return render(request, "myprofile/index.html")


def contact(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        Contact.objects.create(
            name=name,
            email=email,
            mobile=mobile,
            subject=subject,
            message=message
        )
     
        #messages.success(request,"Thanks for contacting me! Your message has been received.")
        return HttpResponse("""
		<!DOCTYPE html>
		<html>
		<head>
		    <style>
		        .notification {
		            background-color: #28a740;
		            color: white;
		            padding: 18px;
		            margin:-15px;
		            font-size: 16px;
		            font-weight: bold;
		            text-align: center;
		        }
		    </style>
		</head>

		<body>

		<div class="notification">
		    Thanks for contacting me! Your message has been received.
		    We will contact you soon!
		</div>

		</body>
		</html>
		""")
    return HttpResponse("Invalid request")




def gallery(request):

    images = GalleryImage.objects.filter(
        is_active=True
    ).order_by(
        'order',
        '-created_at'
    )

    context = {
        'images': images,
        'total_images': images.count(),
    }

    return render(
        request,
        'myprofile/gallery.html',
        context
    )




def get_client_ip(request):
    """
    Get visitor IP address.
    """
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")

    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0].strip()
    else:
        ip = request.META.get("REMOTE_ADDR")

    return ip


def home(request):

    # Get visitor IP
    ip_address = get_client_ip(request)

    # Record this visit
    Visitor.objects.create(
        ip_address=ip_address
    )

    # Total visitors
    total_visitors = Visitor.objects.count()

    # Today's visitors
    from django.utils import timezone

    today = timezone.localdate()

    today_visitors = Visitor.objects.filter(
        visit_date=today
    ).count()

    context = {
        "total_visitors": total_visitors,
        "today_visitors": today_visitors,
    }

    return render(request, "index.html", context)

