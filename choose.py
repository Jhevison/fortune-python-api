import random
import json
import ast


elements = ["quotes/food", "quotes/art", "quotes/tao", "quotes/goedel", "quotes/medicine", "quotes/law", "quotes/work", "quotes/brasil", "quotes/zippy", "quotes/translate-me", "quotes/love", "quotes/drugs", "quotes/science", "quotes/linux", "quotes/kids", "quotes/sports", "quotes/magic", "quotes/people", "quotes/debian", "quotes/definitions", "quotes/songs-poems", "quotes/computers", "quotes/paradoxum", "quotes/politics", "quotes/men-women"]


def returnQuote():
    element = random.choice(elements)

    file = open(element, "r")
    quote = file.read()
    file.close()
    quote = quote.split("%")
 
    
    quote = random.choice(quote).replace("\n", " ").replace("\t", " ").replace("~", " ")
    """
    dict = {
     "quote": quote
     }   
    """
    return quote
returnQuote()
