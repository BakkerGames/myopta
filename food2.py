class Food:
    def __init__(self, name, carbs, protein, fat):
        self.name = name
        self.carbs = carbs
        self.protein = protein
        self.fat = fat

    def calories(self):
        result = (4 * self.carbs) + \
                (4 * self.protein) + \
                (9 * self.fat)
        return result

class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def __str__(self):
        return self.name

    def calories(self):
        result = 0
        for ingredient in self.ingredients:
            result += ingredient.calories()
        return result

recipe1 = Recipe('cake',
    [
        Food('flour',5,0,1),
        Food('milk',0,10,3),
        Food('sugar',6,0,0)
    ])
recipe2 = Recipe('cookies',
    [
        Food('flour',5,0,1),
        Food('milk',0,10,3),
        Food('sugar',6,0,0),
        Food('chocolate chips',10,0,10)
    ])
print(recipe1, recipe1.calories())
print(recipe2, recipe2.calories())
