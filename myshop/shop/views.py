from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Category, Product
from django.views.generic import DetailView, ListView
from .forms import ContactForm
import random
from django.core.paginator import Paginator

class ProductListView(ListView):
    """Начальная страница"""
    model = Product
    template_name = 'shop/product/list.html'
    context_object_name = 'products'
    paginate_by = 4  
    

    def get_context_data(self, **kwargs):
        """
        вытягивает всекатегории товара
        """
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
    
    
    def get_pagination_context(self, **kwargs):
        """
        пагинация карточки товара 
        """
        context = super().get_context_data(**kwargs)
        context["paginator"] = context['paginator']
        context["page_obj"] = context['page_obj']
        return context
    
    
    # def get_queryset(self):
    #     """
    #     Получает случайные 4 продуктов карточки 
    #     """
    #     all_products = list(Product.objects.all())
    #     random_products = random.sample(all_products, min(4,len(all_products)))
    #     return random_products
        
     
class AllCategoryView(ListView):
    """все категории товара"""
    model = Category
    template_name = 'shop/product/all_categories.html'
    context_object_name = 'all_categories'
            
        

class ProductDetail(DetailView):
    """класс детальной информации """
    model = Product
    template_name = 'shop/product/detail.html'
    context_object_name = 'product_detail'



class ProductByCategory(ListView):
    """класс категории товара """
    model = Product
    template_name = 'shop/product/list_by_category.html'
    context_object_name = 'category_product'

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        category = Category.objects.get(slug=category_slug)
        return Product.objects.filter(category=category)


class ProductSearchListView(ListView):
    """класс поиска товара """
    model = Product
    template_name = 'shop/product/product_search_results.html'
    context_object_name = 'product_search'
    paginate_by = 10  #количество результатов на странице

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Product.objects.filter(name__icontains=query)
        else:
            return Product.objects.all()


# def contact_view(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form = ContactForm()
#     return render(request, 'contact/tags/form.html', {'form': form})



