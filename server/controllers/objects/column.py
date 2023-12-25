class Column:
    def __init__(self, name, type, primary_key=False, nullable=True, reference=None):
        self.name = name
        self.type = type
        self.primary_key = primary_key
        self.nullable = nullable
        self.reference = reference
    def __repr__(self):
        return f"<Column {self.name}>"
    
    def change_nullability(self):
        if self.primary_key:
            self.nullable = False