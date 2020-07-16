# ChatBot 5.1

"""
TODO list:
    * Everything done so far!
"""

from __future__ import print_function

from Chatbot_lib import *
from difflib import SequenceMatcher
from random import randrange

print("HELLO, USER!")
print("WELCOME TO CHATBOT!" + "\n")

print("I AM YOUR PERSONAL CHATBOT")
print("I AM HERE TO TALK WITH YOU")
print("UNFORTUNATELY, MY DATABASE ISN'T VERY BIG YET SO PLEASE EXCUSE THE FACT THAT MY CONVERSATIONS ARE LIMITED")
print("THANK YOU" + "\n")


print("\n" + "START OF CONVERSATION" + "\n")


class query(object):

    def __init__(self, highest_matching, query_locator, history):
        self.highest_matching = highest_matching
        self.query_locator = query_locator
        self.history = history

    def querent(self, trigger):
        self.highest_matching = 0.0
        self.query_locator = ""
        if usr_input != "!endchat":
            for i in trigger:
                for l in trigger[i]:
                    if SequenceMatcher(None, usr_input, l).ratio() > self.highest_matching:
                        self.highest_matching = SequenceMatcher(
                            None, usr_input, l).ratio()
                        self.query_locator = i
        else:
            self.highest_matching = -1.0
            self.query_locator = "farewells"

    def comparer(self):
        self.special_categories = {
            "reply_good": "common_greeting_phrases", "reply_bad": "common_greeting_phrases"}
        self.querent(triggers)
        if self.highest_matching >= 0.75 or self.highest_matching == -1.0:
            if self.query_locator not in self.special_categories:
                return self.reply()
            else:
                if self.history == self.special_categories[self.query_locator]:
                    return self.reply()
                else:
                    return self.misunderstand()
        else:
            return self.misunderstand()

    def reply(self):
        self.history_update()
        return chatbot_name + ": " + trigger_response[self.query_locator][randrange(len(trigger_response[self.query_locator]))] + "\n"

    def misunderstand(self):
        return chatbot_name + ": " + trigger_response["misunderstand"][randrange(len(trigger_response["misunderstand"]))] + "\n"

    def history_update(self):
        self.history = self.query_locator


chatbot = query(0.0, "", "")

while True:
    usr_input = input(Username + ": ")
    print(chatbot.comparer())
    if usr_input == "!endchat":
        break
