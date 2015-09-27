
class apriori():
    def __init__(self, file, support):
        # File - each line is set separated by comma or ','
        self.tranlates  = dict()
        self.init_dict  = dict()
        self.counts     = []
        self.temp_count = 0
        self.support    = support

    def __first_round():
        with open("file.txt", "r") as fi:
            for line in fi:
                s = line.split(',')
                for key in s:
                    self.init_dict[key] = self.init_dict(key, 0) + 1

        for key in self.init_dict.keys():

    


    def run():
        pass

    def __second_round():
        pass



if __name__ == '__main__':
    pass