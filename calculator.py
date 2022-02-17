class Calculator:
    def __init__(self):
        pass

    def calculate(self, company, product) -> float:
        """ Returns cost to transport product.
        Arguments:
        company -- the company that defines the prices
        product -- product to be shipped"""
        if company.min_weight is not None:
            if product.weight <= company.min_weight:
                return
        if company.max_weight is not None:
            if product.weight > company.max_weight:
                return
        return (company.fixed_value + (product.weight * product.distance * company.value))/100
    

