from builder import Builder

class Director:
    def __init__(self)->None:
        self._builder = None
        
    @property
    def builder(self)->Builder:
        return self._builder
    
    @builder.setter
    def builder(self,builder:Builder)->None:
        self._builder = builder
        
    def built_minimal_product(self)->None:
        self.builder.produce_part_a()
        
    def built_full_product(self)->None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()
