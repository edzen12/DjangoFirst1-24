from django.shortcuts import render
from apps.contact.models import Contact
from apps.news.models import Category


def contact_page(request):
    contacts = Contact.objects.latest('-id')
    categories = Category.objects.filter(news__isnull=False).distinct()
    context = {
        'contacts':contacts,
        'categories':categories,
    }
    return render(request, 'pages/contact.html', context)