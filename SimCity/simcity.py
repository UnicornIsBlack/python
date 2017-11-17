from material import Material
from product import Product
from complete import Complete
from simplecomplete import SimpleCompleter
import readline

class SimCity:
    material = Material()
    product = Product()
    complete = Complete()

    def __init__(self):
        pass

    def complete_input(self):
        readline.set_completer(SimpleCompleter(self.complete.complete).complete)
        readline.parse_and_bind('tab:complete')
        self.input_demand()
        return

    def input_demand(self):
        print('Input quit to exit!')
        while True:
            demand_input = input('You need:')
            if demand_input == 'quit':
                return
            else:
                (name,count) = demand_input.split(' ')
            if self.material.is_material(name) != -1:
                self.material_add(name, int(count))
            elif self.product.is_product(name) != -1:
                self.product_add(name, int(count))
            else:
                print('Please input correct name!!!')

    def material_add(self, name, count):
        index = self.material.material_index(name)
        if index == -1:
            print('error')
        else:
            self.material.material_count[index] += count
        return

    def product_add(self, name, count):
        index = self.product.product_index(name)
        if index == -1:
            print('error')
        else:
            self.product.product_count[index] += count
            self.product_analysis(index, count)
        return

    def product_analysis(self, index, count):
        pro_or_mat = self.product.get_formula_by_index(index).split('+')
        for element in pro_or_mat:
            (e, e_count) = element.split('*')
            if self.material.is_material(e) != -1:
                self.material_add(e, int(e_count)*count)
            elif self.product.is_product(e) != -1:
                self.product_add(e, int(e_count)*count)
        return

    def print_demand(self):
        self.material.print_material()
        self.product.print_product_count()
        return
