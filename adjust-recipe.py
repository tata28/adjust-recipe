from tokenize import String

new_ingridients=True
ingridients=[]
weight=[]
satuan=[]
ratio=0

print("==== RESEP ASLI =====")
while new_ingridients:
    print(" ")
    user_input = input("Masukkan nama bahan (atau x jika selesai) : ")
    if user_input=='x':
        new_ingridients=False
    else:
        ingridients.append(user_input)
        user_input=float(input("Masukkan berat bahan : "))
        weight.append(user_input)
        user_input=input("Masukkan satuan bahan : ")
        satuan.append(user_input)

print("")
print("==== ADJUST RECIPE ==== ")
user_input = float(input("Masukkan berat bahan pertama : "))
ratio=user_input/weight[0]

print("")
print("==== YOUR RECIPE =====")
for x in range(0,len(ingridients)):
    print(ingridients[x],", ",weight[x]*ratio,", ", satuan[x])
