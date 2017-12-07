import os

class Compare:

    def __init__(self):
        self.array = [0]*24
        pass

    def get_num_by_str(self,filename):
        num = int(filename,2)
        return num

    def get_num_array(self,file_array):
        num_array = []
        for file in file_array:
            (filename,suffix) = file.split('.')
            num = self.get_num_by_str(filename)
            num_array.append(num)
        return num_array

    def print_array(self):
        i = 0
        for num in self.array:
            print(str(i) + ':' + str(num))
            i += 1

    def get_num_of_1(self,num):
        count = 0
        while num:
            num = num & (num - 1)
            count += 1
        return count

    def start(self,img_dir,no_img_dir):
        print('start')
        self.array = [0]*24
        img_file = os.listdir(img_dir)
        no_img_file = os.listdir(no_img_dir)

        img_array = self.get_num_array(img_file)
        no_img_array = self.get_num_array(no_img_file)

        for img_num in img_array:
            num_min = 24
            for no_img_num in no_img_array:
                num = img_num ^ no_img_num
                num_of_1 = self.get_num_of_1(num)
                if num_of_1 < num_min:
                    num_min = num_of_1
            self.array[num_min] += 1
        self.print_array()
        print('end')

compare = Compare()
print('13')
compare.start('../image/','../noimage/')
print('11')
compare.start('../img11/image/','../img11/noimage/')
print('11 and 13')
compare.start('../img11_13/image/','../img11_13/noimage/')
print('11 img and 13 noimg')
compare.start('../img11/image/','../noimage/')



