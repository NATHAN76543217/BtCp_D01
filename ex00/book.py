from datetime import datetime
from recipe import Recipe


class Book():
    """Book of Recipes"""
    def __init__(self, name):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(
                "{} attribute must be set to an instance of {}"
                .format(name, str))
        self.creation_date = datetime.now()
        self.last_update = datetime.now()
        self.recipe_list = dict()
        self.recipe_list["starter"] = []
        self.recipe_list["lunch"] = []
        self.recipe_list["dessert"] = []

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        recipe = None
        for categorie in self.recipe_list.values():
            for recipe in categorie:
                if recipe.name == name:
                    return recipe

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        recipe_names = []
        for recipe in self.recipe_list[recipe_type]:
            recipe_names.append(recipe.name)
        return recipe_names

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if not isinstance(recipe, Recipe):
            raise TypeError(
                "The 'recipe' param must be an instance of Recipe class")
        self.recipe_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.now()

    def __str__(self):
        txt = ""
        txt += "Book: " + self.name + '\n'
        txt += " Created:\t" + str(self.creation_date) + "\n"
        txt += " Last Update:\t" + str(self.last_update)
        return txt
