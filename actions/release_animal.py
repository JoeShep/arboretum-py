from animals import RiverDolphin

def release_animal(arboretum):
    print("1. River Dolphin")
    print("2. Dragonfly")

    choice = input("Choose animal to release > ")

    if choice == "1":
        dolphin = RiverDolphin()
        count = 1
        for river in arboretum.rivers:
            print(f"{str(count)}. {river}")
            count += 1
        for coastline in arboretum.coastlines:
            print(f"{str(count)}. {coastline}")
        dolphin_choice = input("Choose where to release your river dolphin > ")

    if choice == "2":
        pass
