from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Recipe
from .forms import CommentForm, RecipeForm


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginated_by = 6


class RecipeDetail(View):
    def get(self, request, slug, *args, **kwargs):
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
                "comment_form": CommentForm()
            },
        )

    def recipe(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.order_by('created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.recipe)

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


class RecipeLike(View):

    def recipe(self, request, slug):
        recipe = get_object_or_404(Recipe, slug=slug)
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)

        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


def add_recipe(request):
    recipe_form = RecipeForm(request.recipe or None, request.FILES or None)
    context = {
        'recipe_form': recipe_form,
    }

    if request.method == 'recipe':
        recipe_form = RecipeForm(request.recipe, request.FILES)
        if recipe_form.is_valid():
            recipe_form = recipe_form.save(commit=False)
            recipe_form.author = request.user
            recipe_form.status = 1
            recipe_form.save()
            return redirect('home')
    else:
        recipe_form = RecipeForm()
    return render(request,'add_recipe.html', context)


def update_recipe(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    recipe_form = RecipeForm(request.recipe or None, instance=recipe)
    context = {
        'recipe_form': recipe_form,
        'recipe': recipe,
    }
    if request.method == "recipe":
        recipe_form = RecipeForm(request.recipe, request.FILES, instance=recipe)
        if recipe_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('home')
    else:
        recipe_form = RecipeForm(instance=recipe)
    return render(request, "update_recipe.html", context)


def delete_recipe(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    recipe.delete()
    return redirect('home')


def about(request):
    return render(request, "about.html")
