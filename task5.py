from collections import OrderedDict


class HistoryDict:

    def __init__(self, init_dict):
        self.dict = OrderedDict(init_dict)
        self.history = []

    def set_value(self, key, value):
        self.history.append(key)
        if len(self.history) > 10:
            self.history.pop(0)

        self.dict[key] = value

    def get_history(self):
        return self.history


d = HistoryDict({"foo": 43})
d.set_value("baz", 44)
d.set_value("arr", 42)

print(d.get_history())
