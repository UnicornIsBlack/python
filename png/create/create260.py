import array
class PngFile:

    def __init__(self):
        self.start = '89 50 4E 47 0D 0A 1A 0A 00 00 00 0D 49 48 44 52 ' \
           '00 00 00 20 00 00 00 20 02 03 00 00 00 0E 14 92 ' \
           '67 00 00 00 04 67 41 4D 41 00 00 B1 8F 0B FC 61 ' \
           '05 00 00 00 0C 50 4C 54 45 FF FF FF 00 00 00 FF ' \
           '00 00 FF FF 00 31 F4 60 1E 00 00 00 01 62 4B 47 ' \
           '44 00 88 05 1D 48 00 00 00 09 70 48 59 73 00 00 ' \
           '0B 11 00 00 0B 11 01 7F 64 5F 91 00 00 00 91 49 ' \
           '44 41 54 28 CF 55 D0 BB 0D 02 31 0C 80 E1 DF 92 ' \
           '43 9D E2 42 71 D3 E4 24 44 9D 22 A1 60 03 98 82 ' \
           '11 32 C4 71 42 9E 82 D1 28 CE 91 0E 57 9F FC 92 ' \
           '65 38 C6 94 1C 8F 0C 10 6A 33 32 A0 C8 BB 39 B6 ' \
           'AD FF 83 E5 E6 60 2E 8E 10 1D 8C 8D 44 60 02 4A ' \
           '04 2E C1 33 8A BC 88 7B DF 57 6A 20 19 B4 02 52 ' \
           'F6 01 48 AD 2D 00 2C FD D4 15 90 EB 3A F7 02 E8 ' \
           'D9 6C CD 00 B3 D9 0A A0 03 E1 6E '
        self.end = ' 3B 92 42 6D 1F 3E F9 D5 83 F1 00 00 00 00 49 45 4E 44 AE 42 60 82'
        self.fuzz = 'F6 C1 4B'

    def get_hex(self,fuzz):
        png = bytearray.fromhex(self.start)
        png.extend(fuzz)
        png.extend(bytearray.fromhex(self.end))
        return png



    def get_png(self,filename,png):
        pngFile = open(filename, 'wb')
        try:
            pngFile.write(png)
        except IOError as e:
            print(e)
        finally:
            if 'pngFile' in locals():
                pngFile.close()

    def int_to_byte(self,num):
        array_num = []
        array_num.append(num >> 16 & 0xFF)
        array_num.append(num >> 8 & 0xFF)
        array_num.append(num & 0xFF)
        return bytearray(array_num)

    def get_num_of_1(self,num):
        count = 0
        while num:
            num = num & (num - 1)
            count += 1
        return count

    def get_num_fuzz(self,binary_num):
        fuzz_num = 0xF6C14B
        binary_array = array.array('B', [0] * 24)
        i = 23
        while i >= 0:
            binary_array[i] = fuzz_num & 1
            binary_array[i] = binary_array[i] ^ binary_num[i]
            i -= 1
            fuzz_num = fuzz_num >> 1
        int_num = 0
        for bit in binary_array:
            int_num = (int_num << 1) | bit
        return int_num

    def get_num_of_extend(self,num):
        binary_num = array.array('B',[0]*24)
        binary_num[0] = (num >> 12) & 1
        binary_num[2] = (num >> 11) & 1
        binary_num[5] = (num >> 10) & 1
        binary_num[8] = (num >> 9) & 1
        binary_num[9] = (num >> 8) & 1
        binary_num[10] = (num >> 7) & 1
        binary_num[11] = (num >> 6) & 1
        binary_num[12] = (num >> 5) & 1
        binary_num[18] = (num >> 4) & 1
        binary_num[19] = (num >> 3) & 1
        binary_num[21] = (num >> 2) & 1
        binary_num[22] = (num >> 1) & 1
        binary_num[23] = num & 1
        return binary_num

    def get_num_of_extend_11(self,num):
        binary_num = array.array('B',[0]*24)
        binary_num[1] = (num >> 10) & 1
        binary_num[3] = (num >> 9) & 1
        binary_num[4] = (num >> 8) & 1
        binary_num[6] = (num >> 7) & 1
        binary_num[7] = (num >> 6) & 1
        binary_num[13] = (num >> 5) & 1
        binary_num[14] = (num >> 4) & 1
        binary_num[15] = (num >> 3) & 1
        binary_num[16] = (num >> 2) & 1
        binary_num[17] = (num >> 1) & 1
        binary_num[20] = num & 1
        return binary_num

    def get_filename(self,binary_num):
        num = 0
        for bit in binary_num:
            num = (num << 1) | bit
        num_of_1 = self.get_num_of_1(num)
        #filename = '../img11/' + str(num_of_1) + '/' + '{0:024b}'.format(num)
        filename = '../img11/image1/' + '{0:024b}'.format(num)
        return filename

    def run(self):
        i = 0x000
        while i <=0x7FF :
            binary_num = self.get_num_of_extend_11(i)
            num = self.get_num_fuzz(binary_num)
            fuzz = self.int_to_byte(num)
            png = self.get_hex(fuzz)
            filename = self.get_filename(binary_num) + '.png'
            self.get_png(filename, png)
            print(filename)
            i += 1
        print('end')


png = PngFile()
png.run()
