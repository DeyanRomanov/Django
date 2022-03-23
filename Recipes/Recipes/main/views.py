from django.shortcuts import render, redirect

from Recipes.main.forms import CreateRecipe, EditRecipe, DeleteRecipe
from Recipes.main.models import Recipe


def get_recipe():
    recipe = Recipe.objects.all()
    if recipe:
        return recipe


def home_view(request):
    recipes = get_recipe()
    context = {
        'recipes': recipes,
    }
    return render(request, 'index.html', context)


def create_view(request):
    if request.method == 'POST':
        form = CreateRecipe(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = CreateRecipe()
    context = {
        'form': form,
    }
    return render(request, 'create.html', context)


def edit_view(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditRecipe(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = EditRecipe(instance=recipe)
    context = {
        'form': form,
        'recipe': recipe,
    }
    return render(request, 'edit.html', context)


def delete_view(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteRecipe(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = DeleteRecipe(instance=recipe)
    context = {
        'form': form,
        'recipe': recipe,
    }
    return render(request, 'delete.html', context)


def details_view(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ingredients = recipe.ingredients.split(', ')
    context = {
        'recipe': recipe,
        'ingredients': ingredients,
    }
    return render(request, 'details.html', context)
