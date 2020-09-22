class Manipulation:
    
    def __init__(self, x):
        self.x = x
        
    def month(self):
        return self.x.split('/')[0]
    
    def seasonCalc(self):
        if self.x in ['12', '1', '2', '3']:
            return 'Winter'
        elif self.x in ['4', '5', '6']:
            return 'Spring'
        elif self.x in ['7', '8', '9']:
            return 'Summer'
        else: 
            return 'Fall'