"""
Views
"""
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Recipe
from .forms import CommentForm, RecipeForm


def about(request):
    """
    Renders the about page
    """
    return render(request, "about.html")


def add_recipe(request):
    """
    Renders add a recipe page 
    """
    recipe_form = RecipeForm(request.POST or None, request.FILES or None)
    context = {
        'recipe_form': recipe_form,
    }

    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST, request.FILES)
        if recipe_form.is_valid():
            recipe_form = recipe_form.save(commit=False)
            recipe_form.author = request.user
            recipe_form.status = 1
            recipe_form.save()
            return redirect('home')
    else:
        recipe_form = RecipeForm()
    return render(request,'add_recipe.html', context)


class RecipeList(generic.ListView):
    """
    This class creates the recipe list
    """
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class RecipeDetail(View):
    """
    This class creates the recipe view
    """
    def get(self, request, slug, *args, **kwargs):
        """
        This class creates the recipe list
        """
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.order_by('created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
                "recipe_form": RecipeForm(),
            },
        )

    def recipe(self, request, slug, *args, **kwargs):
        """
        Submits form content to the database
        """
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.order_by('created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


def update_recipe(request, slug):
    """
    Recipe update view
    """
    recipe = get_object_or_404(Recipe, slug=slug)
    recipe_form = RecipeForm(request.POST or None, instance=recipe)
    context = {
        'recipe_form': recipe_form,
        'recipe': recipe,
    }
    if request.method == "POST":
        recipe_form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if recipe_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('home')
    else:
        recipe_form = RecipeForm(instance=recipe)
    return render(request, "update_recipe.html", context)


def delete_recipe(request, slug):
    """
    Recipe delete view
    """
    recipe = get_object_or_404(Recipe, slug=slug)
    recipe.delete()
    return redirect('home')


class RecipeLike(View):
    """
    Likes on a recipe
    """
    def post(self, request, slug):
        """
        Submits to view
        """
        recipe = get_object_or_404(Recipe, slug=slug)
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)

        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))

