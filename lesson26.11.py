# h = int(input("Введіть висоту h: "))
# w = int(input("Введіть ширину w: "))

# # Перший рядок
# print("*" * w)

# # Середні рядки
# for _ in range(h - 2):
#     print("*" + " " * (w - 2) + "*")

# # Останній рядок
# print("*" * w)




h = int(input("напишите высоту: "))
w = int(input("напишите ширину: "))

print("*" * w)

for _ in range(h - 2):
    print("*" + " " * (w - 2) + "*")

print("*" * w)
