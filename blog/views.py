from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Publicar



def listar_publicacion(request):
    publi= Publicar.objects.filter(fecha_publica__lte=timezone.now()).order_by('fecha_publica')
    return render(request,'blog/listar_publicacion.html',{'publi':publi})

def detalle_p(request,pk):
        p=get_object_or_404(Publicar,pk=pk)
        return render(request,'blog/post_detail.html', {'p':p})
