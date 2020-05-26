class Recipe():
    """
        Recipe class
    """
    def __init__(
        self, name, cooking_lvl, cooking_time,
            ingredients, description, recipe_type):

        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(
                "{} attribute must be set to an instance of {}"
                .format(name, str))
        if isinstance(cooking_lvl, int):
            if cooking_lvl >= 0 and cooking_lvl <= 5:
                self.cooking_lvl = cooking_lvl
            else:
                raise ValueError(
                    "{} attribute must be a number beetween 1 and 5"
                    .format("cooking_lvl"))
        else:
            raise TypeError(
                "{} attribute must be set to an instance of {}"
                .format("cooking_lvl", int))
        if isinstance(cooking_time, int):
            if cooking_time >= 0:
                self.cooking_time = cooking_time
            else:
                raise ValueError(
                    "{} attribute must be a positive number"
                    .format("cooking_time"))
        else:
            raise TypeError(
                "{} attribute must be set to an instance of {}"
                .format("cooking_time", int))
        if isinstance(ingredients, list):
            for ingredient in ingredients:
                if not isinstance(ingredient, str):
                    raise TypeError(
                        "All ingredients attributes must be represent by str")
            self.ingredients = ingredients
        else:
            raise TypeError(
                "{} attribute must be set to an instance of {}"
                .format("ingredients", list))
        if isinstance(description, str):
            self.description = description
        else:
            raise TypeError(
                "{} attribute must be set to an instance of {}"
                .format(description, str))
        if isinstance(recipe_type, str):
            if recipe_type in ("starter", "lunch", "dessert"):
                self.recipe_type = recipe_type
            else:
                raise ValueError(
                    "{} attribute must one of" +
                    "\"starter\", \"lunch\", \"dessert\""
                    .format(recipe_type))
        else:
            raise TypeError(
                "{} attribute must be set to an instance of {}"
                .format(recipe_type, str))

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = ""
        txt += "----" + self.name + "----\n"
        txt += "Difficulty: " + str(self.cooking_lvl) + '\n'
        txt += "Time: " + str(self.cooking_time) + "min\n"
        txt += "Ingredients:\n"
        for ingredient in self.ingredients:
            txt += "-- " + ingredient+'\n'
        txt += "Description: " + self.description + '\n'
        txt += "Recommanded: " + self.recipe_type
        return txt
