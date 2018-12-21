#Pete, the baker
#Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths.
#Can you help him to find out, how many cakes he could bake considering his recipes?

#Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object) and returns the maximum number of cakes Pete can bake (integer).
#For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). Ingredients that are not present in the objects, can be considered as 0.

#recipe {'flour': 500, 'eggs': 1, 'sugar': 200} and available ingredients {'flour': 1200, 'eggs': 5, 'milk': 200, 'sugar': 1200}: should equal 2
#recipe {'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100, 'cream': 200} and available ingredients {'flour': 20000, 'oil': 30000, 'cream': 5000, 'milk': 20000, 'sugar': 1700}: 0 should equal 11
#recipe {'cocoa': 17, 'eggs': 28, 'pears': 1} and available ingredients {'butter': 9297, 'crumbles': 3676, 'flour': 9354, 'eggs': 4279, 'nuts': 1793, 'pears': 409, 'chocolate': 775, 'cocoa': 6805, 'oil': 6912, 'apples': 2530, 'sugar': 3835, 'milk': 1849, 'cream': 4806}: 0 should equal 152

recipe =  {'oil': 1, 'flour': 3, 'eggs': 1, 'sugar': 1, 'milk': 1, 'cream': 1}
available = {'oil': 1, 'flour': 3, 'eggs': 1, 'sugar': 1, 'milk': 1, 'cream': 1}

def cakes(recipe, available):

    new = 0

    list = []

    recipeKeys = set(recipe.keys())
    recipeAvailable = set(available.keys())
    intersection = recipeKeys.intersection(recipeAvailable)
    print(sorted(intersection))
    print(sorted(recipeKeys))
    
    return sorted(intersection) == sorted(recipeKeys)

    if sorted(intersection) != sorted(recipeKeys):
        return 0 #Why does this return 0 for the above dictionaries?
    elif sorted(intersection) == sorted(recipeKeys):
        for key in recipe.keys():
            if available[key] // recipe[key] > 1:
                new += 1
            
    if new == len(recipe):
        for key in recipe.keys():
            list.append(available[key] // recipe[key])
        return sorted(list)[0]
    elif new != len(recipe):
        return 0            


print(cakes(recipe,available))
    
