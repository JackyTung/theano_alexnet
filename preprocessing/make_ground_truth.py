import random
import argparse
import os

parser = argparse.ArgumentParser(description='generate random ground truth on imagenet')
parser.add_argument('--random-num', type=int, default=100, 
                    help='random range from 1 to random')
parser.add_argument('--num-imgs', type=int, default=5000,
                    help='number of images')
parser.add_argument('--output-dir', type=str, default='/dl-mount/random_ground_truth.txt',
                    help='output file absoluetly path')
args = parser.parse_args()

def generate_ground_truth(rand, num_img, outputfile):
    
    f = open(outputfile, 'w')
    for x in xrange(num_img):
        num = random.randint(1, rand)
        f.write("%s\n" %(num))
    f.close()    

if __name__ == '__main__':
    generate_ground_truth(args.random_num, args.num_imgs, args.output_dir)
