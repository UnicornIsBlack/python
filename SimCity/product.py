class Product:

    product_name = []
    product_formula = []
    product_count = []

    def __init__(self):
        self.init_product()

    def init_product(self):
        file_product = open('product.txt')
        try:
            for each_line in file_product:
                (name, formula, count) = each_line.split(' ')
                self.product_name.append(name)
                self.product_formula.append(formula)
                self.product_count.append(int(count))
        except IOError as e:
            print(e)
        finally:
            if 'file_product' in locals():
                file_product.close()

    def print_product_count(self):
        i = 0
        print('**********Product Count**********')
        while i < len(self.product_count):
            print(self.product_name[i] + ':' + str(self.product_count[i]))
            i += 1
        print('*********************************')
        return

    def is_product(self, name):
        try:
            return self.product_name.index(name)
        except:
            return -1

    def product_index(self, name):
        try:
            return self.product_name.index(name)
        except:
            print('Please input correct product name!!!')
            return -1

    def get_formula_by_index(self, index):
        return self.product_formula[index]