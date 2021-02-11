#scripts/getarticle
# Author: NajlaBH
# version 0.1.0
#

from newspaper import Article
import argparse
import sys

#FOR LOCAL TEST
#URL_NAME= 'https://towardsdatascience.com/create-word-cloud-into-any-shape-you-want-using-python-d0b88834bc32'
#PATH_OUTPUT="./tests/wordcloud/article.txt"


def get_article_text(URL_NAME,PATH_OUTPUT):
    """ Redirect url text to file """
    article = Article(URL_NAME)
    article.download()
    article.parse()
    article_text=article.text
    #print(article_text)
    with open(PATH_OUTPUT, 'w') as a_writer:
            a_writer.write(article_text)


def launch_getarticle():
    """ launch with arguments """
    parser = argparse.ArgumentParser()
    parser.add_argument("urlname",type=str, help="Url to scrap.")
    parser.add_argument("pathout", type=str, help="Path of the text output file.")
    parser.parse_args()
    if (len(sys.argv) < 3):
        print("You have ommitted an argument")
        print("Please put the right arguments and try again")
    elif(len(sys.argv) == 3):
        url_name = sys.argv[1]
        #print(url_name)
        path_txt = sys.argv[2]
        get_article_text(url_name, path_txt)


#FUNC CALL
launch_getarticle()
