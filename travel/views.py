from django.shortcuts import render
# from django.http import HttpResponse


countries = [
        {
        'United States': 'Maine, Oregon, Seattle',
        'Candada': 'Vancouver, Whistler',
        'Indonesia': 'Jarata, Misool',
        'Iceland': 'All over the place',
        'Hungary': 'Budapest'
    }
    ]

def home(request):
    context = {
        'countries': countries
        }
    return render(request, 'travel/home.html', context)

def about(request):
    return render(request, 'travel/about.html')

