from tyre.tyre import Tyre



class CariganTyre(Tyre):
    def __init__(self, tyre_array):
        self.tyre_array = tyre_array

    def needs_service(self):
        c=0
        for i in self.tyre_array:
            if i>=0.9:
                c+=1
        if c>=1:
            return True
        else:
            return False