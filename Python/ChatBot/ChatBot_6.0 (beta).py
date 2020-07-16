# ChatBot 6.0 BETA

"""
TODO list:
	* Add the !functions
	* Add what to do for !wrong
"""

from Chatbot_lib_6 import *
from difflib import SequenceMatcher
from random import choice

import nltk as nltk
from nltk.book import (FreqDist, text1, text2, text3, text4, text5, text6,
                       text7, text8, text9)
from nltk.corpus import wordnet as wn

freq_dist1 = FreqDist(text1)
freq_dist2 = FreqDist(text2)
freq_dist3 = FreqDist(text3)
freq_dist4 = FreqDist(text4)
freq_dist5 = FreqDist(text5)
freq_dist6 = FreqDist(text6)
freq_dist7 = FreqDist(text7)
freq_dist8 = FreqDist(text8)
freq_dist9 = FreqDist(text9)


def freq_range(j): return freq_dist1[j] + freq_dist2[j] + freq_dist3[j] + freq_dist4[j] + \
    freq_dist5[j] + freq_dist6[j] + \
    freq_dist7[j] + freq_dist8[j] + freq_dist9[j]


print("WELCOME TO CHATBOT!" + "\n")

print("I AM YOUR PERSONAL CHATBOT")
print("I AM HERE TO TALK WITH YOU")
print("UNFORTUNATELY, MY DATABASE ISN'T VERY BIG YET SO PLEASE EXCUSE THE FACT THAT MY CONVERSATIONS ARE LIMITED")
print("THANK YOU" + "\n")

print("START OF CONVERSATION" + "\n")


class ChatBot(object):
    """Run the whole ChatBot."""

    def __init__(self, chatbot_name, yesno_values):
        self.chatbot_name = chatbot_name + ": "
        self.yesno_values = yesno_values

        self.commands = ["!endchat", "!wrong"]
        self.highest_matching = 0.0
        self.query_locator = ""
        self.closest_match = ""
        self.input = ""
        self.response = ""
        self.tokens = []
        self.tagged_tokens = []
        self.synsets = []
        self.freq_dict = {}
        self.syn_val_count = 0
        self.history = ""

    def querent(self):
        """Do the querying."""

        self.input = usr_input.lower()
        self.highest_matching = 0.0
        self.query_locator = ""
        if self.input not in self.commands:
            outercursor = conn.cursor()
            for i in outercursor.execute("""SELECT * FROM triggers_sql"""):
                innercursor = conn.cursor()
                for l in innercursor.execute("""SELECT * FROM "{}" """.format(i)):
                    if SequenceMatcher(None, self.input, l).ratio() > self.highest_matching:
                        self.highest_matching = SequenceMatcher(
                            None, self.input, l).ratio()
                        self.query_locator = i
                        self.closest_match = l
        else:
            if self.input == self.commands[0]:
                self.highest_matching = -1.0
                self.query_locator = "farewells"
            elif self.input == self.commands[1]:
                if user.return_user_status != "admin":
                    self.highest_matching = -2.0

    def comparer(self):
        """Check if 'usr_input' is close enough to examples in libraries and returns answer."""

        self.querent()
        if self.highest_matching >= 0.75 or self.highest_matching == -1.0 or self.highest_matching == -2.0:
            if self.highest_matching != -2.0:
                if self.query_locator not in c.execute("""SELECT query FROM special_categories"""):
                    if self.highest_matching <= 0.8:
                        c.execute("""INSERT OR IGNORE INTO "{}" VALUES ("{}")""".format(
                            self.query_locator, self.input))
                        conn.commit()
                    return self.reply()
                else:
                    if self.history in c.execute("""SELECT history_query FROM special_categories"""):
                        return self.reply()
                    else:
                        self.query_locator = "misunderstand"
                        return self.reply()
            else:
                return self.chatbot_name + "You are not an administrator and therefore do not have permission to modify my database." + "\n"
        else:
            self.query_locator = "misunderstand"
            return self.reply()

    def reply(self):
        """Return the reply."""

        self.history_update()
        c.execute(
            """SELECT * FROM "{}" """.format(self.query_locator + "_response"))
        self.response = choice(c.fetchall())
        self.tokens = nltk.word_tokenize(self.response)
        self.tagged_tokens = nltk.pos_tag(self.tokens)
        # word to search for synonyms
        for i in self.tagged_tokens:
            self.freq_dict.clear()
            self.synsets = wn.synsets(i[0])
            self.syn_val_count = 0
            # synonym set
            for l in self.synsets:
                print(
                    "**********************************************************************************")
                # the synonym
                for j in l.lemma_names():
                    if j not in self.freq_dict:
                        self.syn_val_count += freq_range(j) + 1
                    self.freq_dict[j] = range(
                        self.syn_val_count, freq_range(j) + 1)

    def history_update(self):
        """Update the 'history' variable."""

        self.history = self.query_locator

    def enter_valid_value(self, index):
        """Ask the user to enter a valid value"""


chatbot = ChatBot(ChatBot_name, YesNo_values)

while True:
    usr_input = input(user.return_name() + ": ")
    print(chatbot.comparer())
    if usr_input == "!endchat":
        break
