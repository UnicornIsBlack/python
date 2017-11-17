
class Complete:
    complete = []

    def __init__(self):
        self.complete_init()

    def complete_init(self):
        file_complete = open('complete.txt')
        try:
            for each_line in file_complete:
                self.complete.append(each_line.split('\n')[0])
        except IOError as e:
            print(e)
        finally:
            if 'file_complete' in locals():
                file_complete.close()
        return


