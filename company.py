class Company:
    def __init__(self, name, fixed_value, value, max_weight = None, min_weight = 0):
        self.name = name
        self.fixed_value = fixed_value
        self.value = value
        self.max_weight = max_weight
        self.min_weight = min_weight