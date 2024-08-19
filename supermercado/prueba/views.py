from django.shortcuts import render, redirect, get_object_or_404
from .models import Lista, Producto
from .forms import ListaForm, ProductoForm

def lista_supermercado(request):
    if request.method == 'POST':
        if 'add_list' in request.POST:
            form = ListaForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('lista_supermercado')
        elif 'add_product' in request.POST:
            form = ProductoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('lista_supermercado')
    else:
        lista_form = ListaForm()
        producto_form = ProductoForm()


    if request.method == 'POST' and 'toggle' in request.POST:
        producto_id = request.POST.get('toggle')
        producto = get_object_or_404(Producto, id=producto_id)
        producto.marcado = not producto.marcado
        producto.save()
        return redirect('lista_supermercado')

    listas = Lista.objects.all()
    productos = Producto.objects.all()
    total = sum(producto.precio for producto in productos if producto.marcado)

    context = {
        'listas': listas,
        'productos': productos,
        'total': total,
        'lista_form': lista_form,
        'producto_form': producto_form,
    }
    return render(request, 'lista_supermercado.html', context)