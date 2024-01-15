import fil


lista=fil.beolvas()

fil.sorok(lista)

lr_index=fil.l_rovidebb(lista)
print(f"A legrovidebb film cime: {lista[lr_index].cim}")

szamlalo=fil.x_perces(lista)
print(f"{szamlalo} db, legalabb 110 perces film van.")

eredmeny=fil.beker(lista)
print(eredmeny)

fil.kiir(eredmeny)
print(f"A szinesz a kovetkezo filmben szerepel: {eredmeny}")