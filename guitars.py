from Prac_06.guitar import Guitar

print("My guitars!")
guitars = [Guitar("Gibson L-5 CES", 1922, 16035.40), Guitar("Line 6 JTV-59", 2010, 1512.9)]

for i, guitar in enumerate(guitars):
    if guitar.is_vintage():
        print(f"Guitar {i + 1}: {guitar.name} ({guitar.year}), worth $ {guitar.cost:,.2f} (vintage)")
    else:
        print(f"Guitar {i + 1}: {guitar.name} ({guitar.year}), worth $ {guitar.cost:,.2f}")
