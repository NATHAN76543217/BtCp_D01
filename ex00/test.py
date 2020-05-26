from book import Book
from recipe import Recipe

if __name__ == "__main__":
    ingredients_gateau = ["Tomate", "farine", "orange", "cawote"]
    ingredients_profiterole = ["farine", "eau", "sucre", "guacamole"]

    description = "Un jolie gateau a base d'ingredients"
    my_book = Book("livre de recette")
    ma_recette = Recipe(
        "mon beau gateau", 3, 30,
        ingredients_gateau, description, "dessert")
    mes_profiteroles = Recipe(
        "Profiteroles", 5, 40,
        ingredients_profiterole, "un tres bon dessert", "dessert")
    print(my_book)
    my_book.add_recipe(mes_profiteroles)
    my_book.add_recipe(ma_recette)
    print(my_book.get_recipe_by_name("mon beau gateau"))
    print("")
    print(my_book.get_recipes_by_types("dessert"))
    print(my_book)
