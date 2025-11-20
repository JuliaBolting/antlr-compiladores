class IRCode:
    def __init__(self):
        self.code = []
        self.temp_count = 0
        self.label_count = 0

    def new_temp(self):
        t = f"t{self.temp_count}"
        self.temp_count += 1
        return t

    def new_label(self):
        L = f"L{self.label_count}"
        self.label_count += 1
        return L

    def emit(self, op, arg1=None, arg2=None, result=None):
        self.code.append((op, arg1, arg2, result))

    def emit_label(self, label):
        self.code.append(("LABEL", label, None, None))
