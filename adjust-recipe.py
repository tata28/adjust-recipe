from tokenize import String

new_ingredients=True
ingredients=[]
weight=[]
units=[]
ratio=0

print("==== RESEP ASLI =====")
while new_ingredients:
    print(" ")
    user_input = input("Masukkan nama bahan (atau x jika selesai) : ")
    if user_input=='x':
        break
    else:
        ingredients.append(user_input)
        user_input=float(input("Masukkan berat bahan : "))
        weight.append(user_input)
        user_input=input("Masukkan units bahan : ")
        units.append(user_input)

print("")
print("==== ADJUST RECIPE ==== ")
user_input = float(input("Masukkan berat bahan pertama : "))
ratio=user_input/weight[0]

print("")
print("==== YOUR RECIPE =====")
for x in range(0,len(ingredients)):
    print(ingredients[x]," : ",weight[x]*ratio," ", units[x])