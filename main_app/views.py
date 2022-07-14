from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cat, Toy
from .forms import FeedingForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

# faux cat data:

# class Cat:
#   def __init__(self, name, breed, description, age):
#     self.name = name
#     self.breed = breed
#     self.description = description
#     self.age = age

# cats = [
#   Cat('Mark', 'Cat', 'Scratchy', 3),
#   Cat('Jose', 'Cat', 'Bitey', 15),
#   Cat('Janet', 'Cat', 'Ran away', 4)
# ]


# # Create your views here.


def home(req):
  return render(req, 'home.html')


#If you want to send back raw text or an html string use HttpResponse


def about(req):
  return render(req, 'about.html')

def base(req):
  return render(req, 'base.html')

def cats_index(req):
  cats = Cat.objects.all()
  return render(req, 'cats/index.html', {'cats': cats})

def cats_detail(req, cat_id):
  #get individual cat
  cat = Cat.objects.get(id=cat_id)
  #instantiate feddingform to be rendered in the template
  feeding_form = FeedingForm()
  #render the template
  return render(req, 'cats/detail.html', {'cat': cat, 'feeding_form': feeding_form})

def add_feeding(req, cat_id):
  # create the ModelForm using the data in request.POST
  form = FeedingForm(req.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.cat_id = cat_id
    new_feeding.save()
  return redirect('detail', cat_id=cat_id)

class CatCreate(CreateView):
  model = Cat
  fields = '__all__'
  success_url = '/cats/'

class CatUpdate(UpdateView):
  model = Cat
  fields = ['breed', 'description', 'age']

class CatDelete(DeleteView):
  model = Cat
  success_url = '/cats/'

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'