from Class import *

start = input("Boshlashga tayyormisiz(h/y)?\n>>>>>>>>>> ")

if start != 'h' and start != 'H':
    print("Dastur to'xtatildi!")

else:
    mod = input("Vertolyot modelini bering: ")
    v = Vertolyot(mod)

    while True:
        print("__________________\nTanlovni kiriting: ")
        tanlov = int(input(
            "1. Informatsiya chiqarish\n"
            "2. Start berish\n"
            "3. Tezlik qo'shish\n"
            "4. Tezlik kamaytirish\n"
            "5. Vertolyotni to'xtatish\n"
            "6. Dasturni to'xtatish\n"
            ">>>>>>>>>>>> "
        ))

        match tanlov:
            case 1:
                print("**************************\n")
                v.info()
                print("\n**************************\n")
            case 2:
                print("\n**************************\n")
                v.start()
                v.speed_info()
                print("\n**************************\n")
            case 3:
                print("\n**************************\n")
                v.add_speed()
                v.speed_info()
                print("\n**************************\n")
            case 4:
                print("\n**************************\n")
                v.sub_speed()
                v.speed_info()
                print("\n**************************\n")
            case 5:
                print("\n**************************\n")
                v.stop()
                v.speed_info()
                print("\n**************************\n")
            case 6:
                print("\n**************************\n")
                print("Dastur to'xtatildi!")
                break
            case _:
                print("\n**************************\n")
                print("Bunday funksiya mavjud emas!")