import copy


class Portfolio:
    #####
    # Dunder methods
    #####
    def __init__(self, initial_cash, positions):
        """ Used to instantiate the class, in this case, the positions 
        need to be specified as a dictionary that contains as the keys 
        the names of the companies and as the value another dictionary 
        containing the share price and the number of shares.
        
        Example:
        initial_cash = 100000
        positions = {"Apple":   {"Share price": 150.0, "Number": 1000},
                       "Verizon": {"Share price": 52.4, "Number": 3000}}
        """
        # Attributes
        self.__initial_cash = initial_cash
        self.positions = positions
        self.cash = initial_cash
    
    
    def __str__(self):
        return "A portfolio consisting of {number} positions and " \
            + "a total value of {value:,} USD.".format(
                number=len(self.positions), 
                value=round(self.get_total_value(), 2)
                )
    
    
    #def __len__(self):
    #    return len(self.positions)
    
    
    #def __add__(self, portfolio_2):
    #    initial_cash = self.cash + portfolio_2.cash
    #    for company, position in portfolio_2.positions.items():
    #        if company in self.positions:
    #            self.make_transaction(company, position['Number'])
    #        else:
    #            self.make_transaction(company, position['Number'], 
    #               position['Share price'])
    #    positions = self.positions
    #    return Portfolio(initial_cash, positions)
    
    
    #def __ge__(self, portfolio_2):
    #    return self.get_total_value() >= portfolio_2.get_total_value()
    
    
    #def __iter__(self):
    #    self.n = 0
    #    self.companies = list(self.positions)
    #    return self
    
    
    #def __next__(self):
    #    if self.n <= len(self.companies) - 1:
    #        company = self.companies[self.n]
    #        result = self.positions[company]
    #        self.n += 1
    #        return company, result
    #    else:
    #        raise StopIteration
    
    #####
    # Attributes
    #####
    #@property
    #def value(self):
    #    return sum([position['Share price']*position['Number'] 
    #                          for _, position 
    #                          in self.positions.items()]) \
    #            + self.cash
    
    #@property
    #def positions(self):
        """
        The difference between shallow and deep copying is only relevant
        for compound objects 
        (objects that contain other objects, like lists or 
        class instances):
                - A shallow copy constructs a new compound object and
                then (to the extent possible) inserts references into it
                to the objects found in the original.
                - A deep copy constructs a new compound object and then,
                recursively, inserts copies into it of the objects found
                in the original.
        """
    #    return copy.deepcopy(self.positions)

    
    #####
    # Class methods
    #####
    #@classmethod
    #def from_dataframe(self, initial_value, portfolio):
    #    dictionary = {}
    #    for _, row in portfolio.iterrows():
    #        dictionary[row['company']] = {
    #           "Share price": row['share_price'], 
    #           "Number": row['number']
    #           }
    #    return Portfolio(initial_value, dictionary)
    
    #####
    # Static method
    #####
    #@staticmethod
    #def get_present_value(fv, r, time):
    #    return fv*(1/(1+r)**time)
    
    #####
    # Methods
    #####
    def get_total_value(self):
        return sum([position['Share price']*position['Number'] 
                              for _, position
                              in self.positions.items()]) \
                 + self.cash
    
    
    #def update_price(self, company, new_price):
    #    self.positions[company]['Share price'] = new_price
    #    return 'SUCCESS'
    
    
    #def update_positions(self, positions):
    #    self.positions = positions
    #    self.cash = self.__initial_cash
    #    for _, position in positions.items():
    #        self.cash -= position['Share price']*position['Number']
    
    
    def make_transaction(self, company, number, price=None):
        if company not in self.positions:
            assert price is not None, \
                'Company not yet known, please provide share price.'
            assert self.cash - price*number >= 0, "Not enough cash, please increase cash position"
            self.positions[company] = {'Share price': price, 
                                         "Number": number}
            self.cash = self.cash - price*number
        else:
            assert price is None, \
                "When making a transaction on a company in the portfolio, you should update " + \
                "the price using the update_price method first instead of specifying the price here."
            self.positions[company]['Number'] += number
            self.cash -= number*self.positions[company]["Share price"]