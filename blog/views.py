from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Publicar
from .forms import PostearForm
from django.shortcuts import redirect


def listar_publicacion(request):
    publi= Publicar.objects.filter(fecha_publica__lte=timezone.now()).order_by('fecha_publica')
    return render(request,'blog/listar_publicacion.html',{'publi':publi})

def detalle_p(request,pk):
        p=get_object_or_404(Publicar,pk=pk)
        return render(request,'blog/post_detail.html', {'p':p})

def post_new(request):
    if request.method=="POST":
       form = (PostearForm(request.POST))
       if form.is_valid():
           post= form.save(commit=False)
           post.autor=request.user
           post.fecha_publica=timezone.now()
           post.save()
           return redirect('post_detail', pk=post.pk)
    else:
        form = PostearForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_detail(request,pk):
    p=get_object_or_404(Publicar,pk=pk)
    return render(request,'blog/post_detail.html', {'p':p})

def post_edit(request, pk):
        post = get_object_or_404(Publicar, pk=pk)
        if request.method == "POST":
            form = PostearForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect('postear', pk=post.pk)
        else:
            form = PostearForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})
