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
           #post.fecha_publica=timezone.now()
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

def post_draft_list(request):
    publi= Publicar.objects.filter(fecha_publica__isnull=True).order_by('fecha_creacion')
    return render(request, 'blog/post_draft_list.html', {'posts': publi})

def post_publish(request, pk):
    post = get_object_or_404(Publicar, pk=pk)
    post.publicacion()
    return redirect('post_detail', pk=pk)

def publish(self):
    self.fecha_publica= timezone.now()
    self.save()


def post_remove(request, pk):
    post = get_object_or_404(Publicar, pk=pk)
    post.delete()
    publi= Publicar.objects.filter(fecha_publica__lte=timezone.now()).order_by('fecha_publica')
    return render(request,'blog/listar_publicacion.html',{'publi':publi})
