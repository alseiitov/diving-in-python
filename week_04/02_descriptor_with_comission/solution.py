class Value:
    def __set__(self, obj, value):
        self.amount = value * (1 - obj.commission)

    def __get__(self, obj, obj_type):
        return self.amount


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission
