#scripts/getshape
# Author: NajlaBH
# version 0.1.0
#
from newspaper import Article
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from wordcloud import STOPWORDS
from PIL import Image
import numpy as np


import sys
import argparse

#FOR LOCAL TEST
#URL_NAME= 'https://towardsdatascience.com/create-word-cloud-into-any-shape-you-want-using-python-d0b88834bc32'
#PATH_ORIGINAL_SHAPE="./tests/wordcloud/shaps/mask_shape.png"
#PATH_FINAL_SHAPE="./tests/wordcloud/shape.png"


def get_article_shape(URL_NAME,PATH_ORIGINAL_SHAPE,PATH_FINAL_SHAPE):
    """ Create worldcloud based shape """"
    article = Article(URL_NAME)
    article.download()
    article.parse()
    article_text=article.text
    #print(article_text)
    #wc = WordCloud()
    mask = np.array(Image.open(PATH_ORIGINAL_SHAPE))
    wc= WordCloud(stopwords=STOPWORDS,
            mask=mask,
            background_color="white",
            max_words=2000,
            max_font_size=256,
            random_state=42,
            width=mask.shape[1],
            height=mask.shape[0])
    wc.generate(article_text)
    plt.imshow(wc, interpolation="bilinear")
    plt.axis('off')
    #plt.show()
    plt.savefig(PATH_FINAL_SHAPE)


#FUNC CALL
def launch_getshape():
    """ Launch with arguments """
    parser = argparse.ArgumentParser()
    parser.add_argument("urlname",type=str, help="Url to scrap.")
    parser.add_argument("pathin", type=str, help="Path of the original png file.")
    parser.add_argument("pathout", type=str, help="Path of the new png output file.")
    parser.parse_args()
    if (len(sys.argv) < 4):
        print("You have ommitted an argument")
        print("Please put the right arguments and try again")
    elif(len(sys.argv) == 4):
        url_name = sys.argv[1]
        #print(url_name)
        path_png = sys.argv[2]
        path_shape = sys.argv[3]
        get_article_shape(url_name, path_png,path_shape)

#FUNC CALL
launch_getshape()

