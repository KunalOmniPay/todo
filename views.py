from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect
from .models import List
from .forms import Form
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
def todoapp(request):
    form = Form(request.POST or None)
    if request.method=='POST':

     if form.is_valid:
         new_post=form.save(commit=False)
         new_post.save()
         messages.success(request, ('Event is added to the list'))
    form=Form()
    items=List.objects.all()
    return render(request,'home.html',{'items':items,'form':form})

def delete(request,list_id):
    item=List.objects.get(pk=list_id)
    item.delete()
    messages.success(request,('Item has been deleted'))
    return redirect('/home')
def edit(request,list_id):
    instance=get_object_or_404(List,id=list_id)
    form=Form(request.POST or None ,instance=instance)
    if form.is_valid():
        update_post=form.save(commit=False)
        update_post.save()
        return redirect('/home/')
    return render(request,'edit.html',{"form":form})

