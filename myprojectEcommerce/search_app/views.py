from django.shortcuts import render
from myapp.models import Product, Category
from django.db.models import Q


# Create your views here.

def searchResult(request):
    products = None
    query = None  # Get the query or set to an empty string by default

    if 'q' in request.GET:  # Only perform the search if the query is not empty
        query = request.GET.get('q')
        products = Product.objects.filter(
            Q(names__icontains=query) | Q(decs__icontains=query))  # Case insensitive search
        # Debugging information
    print(f"Search query: {query}")
    print(f"Products found: {products}")
    return render(request, 'search.html', {'query': query, 'products': products})
