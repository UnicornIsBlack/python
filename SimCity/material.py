class Material:
    material_name = []
    material_time = []
    material_count = []

    def __init__(self):
        self.init_material()

    def init_material(self):
        file_material = open('material.txt')
        try:
            for each_line in file_material:
                (name, time, count) = each_line.split(' ')
                self.material_name.append(name)
                self.material_time.append(time)
                self.material_count.append(int(count))
        except IOError as e:
            print(e)
        finally:
            if 'file_material' in locals():
                file_material.close()

    def print_material(self):
        i = 0
        print('**********Material**********')
        while i < len(self.material_count):
            print(self.material_name[i] + ':' + str(self.material_count[i]))
            i += 1
        print('****************************')
        return

    def is_material(self, name):
        try:
            return self.material_name.index(name)
        except:
            return -1

    def material_index(self, name):
        try:
            return self.material_name.index(name)
        except:
            print('Please input correct material name!!!')
            return -1

