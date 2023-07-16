from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from core.erp.models import Category, Product
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


def category_list(request):
    data = {
        'title': 'Listado de categorias',
        'categorias': Category.objects.all()
    }
    return render(request, 'category/list.html', data)

class CategoryListView(ListView):
    model = Category 
    template_name = 'category/list.html'


    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
          data= Category.objects.get(pk=request.POST['id']).toJSON
        except Exception as e:
            data['error'] = str(e)
        
        return JsonResponse(data)

    def get_queryset(self):
        return Category.objects.filter(name__startswith='b')


    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context ['title'] = 'Listado de categorias'
        #context ['objects_list'] = Product.objects.all()
        return context