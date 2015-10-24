import numpy as np

if __name__ == '__main__':
    green = [(25,125), (44,105), (29,97), (35,63), (55,63), (42,57), (23,40), (64,37), (33,22), (55,20)]
    gold  = [(28,145), (65,140), (50,130), (38,115), (55,118), (50,90), (43,83), (50,60), (50,30)]

    print("---- Question 1 ------")
    green_centroid = [0.,0.]
    gold_centroid  = [0.,0.]
    green_centroid[0] += sum([x[0] for x in green])/float(len(green))
    green_centroid[1] += sum([x[1] for x in green])/float(len(green))
    gold_centroid[0]  += sum([x[0] for x in gold])/float(len(gold))
    gold_centroid[1]  += sum([x[1] for x in gold])/float(len(gold))
     
    print("Green centroid: {0}".format(green_centroid))
    print("Gold centroid: {0}".format(gold_centroid))
    
    print("---- Question 2 -----")
    c1 = (5, 10)
    c2 = (20, 5)
    