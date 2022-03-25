"""Classes for melon orders."""




class AbstractMelonOrder:
    """An abstract base class that other Melon Orders inherit from."""
    
    def __init__(self, species, qty, order_type, tax):
        self.species = species
        self.qty = int(qty)
        self.shipped = False
        self.order_type = order_type
        self.tax = float(tax)

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5

        if self.species == "Christmas melon":
            base_price = base_price * 1.5
        
        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == 'international' and self.qty < 10:
            total += 3
        
        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True
    

class GovernmentMelonOrder(AbstractMelonOrder):
    
    def __init__(self, species, qty):
        super().__init__(species, qty, "government", 0.0)
        self.passed_inspection = False
    
    
    def mark_inspection(self, passed):
        self.passed_inspection = passed


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    
    def __init__(self, species, qty):
        super().__init__(species, qty, "domestic", 0.08)
        # """Initialize melon order attributes."""
         

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    
    
    def __init__(self, species, qty, country_code):
        super().__init__(species, qty, "international", 0.17 )
        self.country_code = country_code

  

def get_country_code(self):
        """Return the country code."""
        
        return self.country_code

        """Initialize melon order attributes."""
    


order0 = GovernmentMelonOrder("watermelon", 6)

