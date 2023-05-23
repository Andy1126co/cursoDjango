# EJERCICIO 1
#
# El area metropolitana de bucaramanga esta constituido
# por los municipio de Bucaramanga, Floridablanca, Girón,
# y Piedecueta

# ¿Cuantas personas en
# total hay en el AMB?
#
# Bucaramanga  581 mil
# Flroridablanca 267 mil
# Girón            260 mil
# Piedecuesta       163 mil


bucaramanga = 581000
floridablanca = 267000
giron = 260000
piedecuesta = 163000

total = bucaramanga + floridablanca + giron + piedecuesta
print("En el area metropolitana hay un total de " + str(total) + " Habitantes")

# ///////////////////////////////////////////////////////////////////////////////////////////////////////

# Jose tiene 3 hijos, si cada hijo tiene 2 mascotas,
# ¿cuántas mascotas tiene Jose en su hogar?

hijosJose = 3
mascotas = 2
print("Jose tiene " + str(hijosJose * mascotas) + " mascotas en su hogar")
print("¿cuántas mascotas habrían en el AMB?")
print("Hay " + str(int((total / 10) * 3)) + " mascotas en el AMB")
