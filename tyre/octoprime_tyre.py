from tyre.tyre import Tyre



class OctoprimeTyre(Tyre):
    def __init__(self, tyre_array):
        self.tyre_array = tyre_array

    def needs_service(self):
        sum=0
        for i in self.tyre_array:
            sum+=i
        if sum>=3:
            return True
        else:
            return False