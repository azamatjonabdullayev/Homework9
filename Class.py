import time as t

"""     sleep() funksiyasidan foydalanilgan!        """


class Vertolyot:
    def __init__(self, model: str, tezlig = 0, max_tezlig = 2400):
        self.model = model
        self.speed = tezlig
        self.max_speed = max_tezlig



    def info(self):
        print(f"Vertolyot modeli: {self.model}\n"
              f"Hozirgi tezligi: {self.speed}\n"
              f"Maksimal tezlig: {self.max_speed}")


    def speed_info(self):
        print(f"Hozirgi tezlig: {self.speed}")


    def start(self):
        if self.speed > 0:
            print("Vertolyot allaqachon havoda!")
        elif self.speed == 0:
            print("Vertolyotga start berildi!")
            tezlik = int(input("Qaysi tezlikka chiqsin?\n>>>>>>>>>> "))
            self.speed += tezlik


    def add_speed(self):
        if self.speed < self.max_speed:

            add_tezlik = int(input("Tezlik qo'shing: "))
            t.sleep(5)
            self.speed += add_tezlik


            if self.speed >= self.max_speed:
                self.speed = self.max_speed
            print(f"Tezlik {self.speed}ga oshirildi!")



    def sub_speed(self):
        if self.speed == 0:
            print("Vertolyot allaqachon to'xtagan!")
            return
        else:
            sub_tezlik = int(input("Tezlikni kamaytiring: "))
            t.sleep(5)
            if self.speed - sub_tezlik <= 0:
                self.speed = 0
                print("Vertolyot to'xtadi.")
                return
            else:
                self.speed -= sub_tezlik
                print(f"Tezlik {sub_tezlik} ga kamaytirildi.")



    def stop(self):
        if self.speed <= 0:
            print("Vertolyot allaqachon to'xtagan!")
            return
        else:
            t.sleep(5)
            self.speed = 0
            print("Vertolyot to'xtadi!")
            return