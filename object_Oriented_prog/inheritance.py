class Smart_Speaker:
    volume = 15
    def increase_volume(self):
        self.volume = self.volume + 1
        print("Smart Speaker Volume :", self.volume)


class Smart_TV(Smart_Speaker):
    volume = 20
    def increase_volume(self):
        super().increase_volume()
        print("Smart TV Volume :", self.volume)


my_smart_tv = Smart_TV()
my_smart_tv.increase_volume()