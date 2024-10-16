from django.shortcuts import render
from django.http import HttpResponse

DATA = {
        'omlet': {
            'яйца, шт': 2,
            'молоко, л': 0.1,
            'соль, ч.л.': 0.5,
        },
        'pasta': {
            'макароны, г': 0.3,
            'сыр, г': 0.05,
        },
        'buter': {
            'хлеб, ломтик': 1,
            'колбаса, ломтик': 1,
            'сыр, ломтик': 1,
            'помидор, ломтик': 1,
        },
    }

def recipes(request, recipe_name):
    all_recipes = DATA

    recipe = DATA.get(recipe_name, None)

    return render(request, 'index.html', {'recipe': recipe})


def get_servings(request, recipe_name):

    recipe = DATA.get(recipe_name)

    serving = int(request.GET.get('servings', 1))

    if recipe:
        new_recipe = {name: amount * serving for name, amount in recipe.items()}
    else:
        new_recipe = None

    return render(request, 'index.html', {'recipe': new_recipe})

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
