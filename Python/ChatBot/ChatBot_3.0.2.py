# ChatBot 3.0.2

from Chatbot_lib import *
from difflib import *
from random import *

print("")
print("HELLO, USER!")
print("WELCOME TO CHATBOT!")
print("")
print("I AM YOUR CHATBOT")
print("I AM HERE TO TALK WITH YOU")
print("UNFORTUNATELY, MY DATABASE ISN'T VERY BIG YET SO PLEASE EXCUSE THE FACT THAT MY CONVERSATIONS ARE VERY LIMITED")
print("THANK YOU")
print("")


def query(trigger):
    highest_matching = 0.0
    query_locater = ""
    if usr_input != "!endchat":
        for i in trigger:
            for l in trigger[i]:
                if SequenceMatcher(None, usr_input, l).ratio() > highest_matching:
                    highest_matching = SequenceMatcher(
                        None, usr_input, l).ratio()
                    query_locater = i
    else:
        highest_matching = -1
        query_locater = "farewells"

    if highest_matching >= 0.75 or highest_matching == -1.0:
        return trigger_response[query_locater][randrange(len(trigger_response[query_locater]))]
    else:
        return trigger_response["misunderstand"][randrange(len(trigger_response["misunderstand"]))]


while True:
    usr_input = input()
    print(query(triggers))
    if usr_input == "!endchat":
        break
