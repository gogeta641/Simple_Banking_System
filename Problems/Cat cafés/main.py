cafe = ""
cafe_name = []
cafe_cats = []

while True:
    cafe = input()
    if cafe == "MEOW":
        break
    cafe_list = cafe.split()
    cafe_name.append(cafe_list[0])
    cafe_cats.append(int(cafe_list[1]))

biggest = cafe_cats.index(max(cafe_cats))
print(cafe_name[biggest])