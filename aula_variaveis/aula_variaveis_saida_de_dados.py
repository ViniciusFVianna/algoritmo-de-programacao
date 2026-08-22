baseIngredient = "Pão"
creamIngredient = "Requeijão"
slashedIngredient = "Queijo"

sanduch = f"""
    1. Paegue a fatia de {baseIngredient}.
    2. Pegue a faca.
    3. Com a faca pague o {creamIngredient}.
    4. Passe o {creamIngredient} na fatia de {baseIngredient}
    5. Acrescente uma fatia de {slashedIngredient}..
"""

print("============= Ingredientes do sanduíche: =============")
print("Ingrediente base:",baseIngredient)
print("Ingrediente cremoso:",creamIngredient)
print("Ingrediente fatiado:",slashedIngredient,)
print("Receita de sanduíche:")
print(sanduch)