#scripts/getplot
# Author: NajlaBH
# version 0.1.0
#

from newspaper import Article
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from wordcloud import STOPWORDS

import argparse
import sys


#Fir ---or test
#URL_NAME= 'https://towardsdatascience.com/create-word-cloud-into-any-shape-you-want-using-python-d0b88834bc32'
#PATH_OUTPUT="./tests/wordcloud/article.png"


def get_article_plot(URL_NAME,PATH_OUTPUT):
    """ create the worldcloud simple png """
    article = Article(URL_NAME)
    article.download()
    article.parse()
    article_text=article.text
    #print(article_text)
    #wc = WordCloud()
    wc= WordCloud(background_color="white",
            max_words=2000,
            stopwords=STOPWORDS,
            max_font_size=256,
            random_state=42,
            width=500,
            height=500)
    wc.generate(article_text)
    plt.imshow(wc, interpolation="bilinear")
    plt.axis('off')
    #plt.show()
    plt.savefig(PATH_OUTPUT)


#FUNC CALL
def launch_getplot():
    """ Launch with arguments """
    parser = argparse.ArgumentParser()
    parser.add_argument("urlname",type=str, help="Url to scrap.")
    parser.add_argument("pathout", type=str, help="Path of the png output file.")
    parser.parse_args()
    if (len(sys.argv) < 3):
        print("You have ommitted an argument")
        print("Please put the right arguments and try again")
    elif(len(sys.argv) == 3):
        url_name = sys.argv[1]
        #print(url_name)
        path_png = sys.argv[2]
        get_article_plot(url_name, path_png)


#FUNC CALL
launch_getplot()
