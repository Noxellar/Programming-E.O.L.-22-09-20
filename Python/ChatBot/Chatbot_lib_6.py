# ChatBot libraries 6.0

import sqlite3


class user(object):
    "Define user properties"

    def __init__(self, name, status):
        self.name = name
        self.status = status

    def return_name(self):
        return self.name

    def return_user_status(self):
        return self.status


YesNo_values = ["y", "Y", "n", "N"]

print("\n" + "HELLO, USER!" + "\n")

username = input("WHAT IS YOUR NAME?: ")

if username == "HDB1":
    password = input("PASSWORD: ")
    while password != "00000000":
        print("ACCESS DENIED ... PLEASE TRY AGAIN")
        password = input("PASSWORD: ")
    else:
        print("GREETINGS, HDB1, HOW MAY I HELP YOU TODAY?")
        ChatBot_name = "CHATBOT"
        user = user(username, "admin")
else:
    user = user(username, "standard")
    change_ChatBot_name = input("WOULD YOU LIKE TO NAME THIS CHATBOT. y/n: ")
    while change_ChatBot_name not in YesNo_values:
        change_ChatBot_name = input("PLEASE ENTER VALID VALUE. y/n: ")
    else:
        if change_ChatBot_name in YesNo_values[0:2]:
            ChatBot_name = input("PLEASE ENTER CHATBOT NAME : ")
        else:
            print("CHATBOT NAME WILL BE SET TO DEFAULT NAME, CHATBOT.")
            ChatBot_name = "CHATBOT"

print("\n" + "PLEASE MAKE SURE THAT IT SAYS 'START OF CONVERSATION' BEFORE YOU START TYPING SO THAT THE DATABASES HAS TIME TO LOAD" + "\n")

triggers = {
    "greetings": ["hello", "hi"],
    "farewells": ["bye", "goodbye", "bye bye", "farewell", "see ya"],
    "common_greeting_phrases": ["how do you do", "how are you", "hows everything", "how is everything", "how are you doing", "hows it going"],
    "ask_bot_identity": ["who are you", "what are you", "what is your name"],
    "facts": ["give me a fact", "I'm feeling curious", "fact" "fun fact"],
    "complements": ["youre cool", "youre awesome", "youre amazing", "youre incredible", "youre the best"],
    "complements_looks": ["youre pretty", "you look nice", "you look handsome", "you look great"],
    "critism": ["youre ugly", "youre silly", "youre stupid", "youre the worst", "i hate you", "youre dumb", "youre useless", "silly thing", "youre a dummy", "youre mean"],
    "reply_good": ["good", "im doing good", "yes", "good thanks for asking", "im doing fine thank you"],
    "reply_bad": ["bad", "I'm not doing too good", "im not feeling too well", "im feeling down in the dumps", "no"],
    "misunderstand": []
}

trigger_response = {
    "greetings": ["Hello!", "Hi!", "Good day", "Salutations"],
    "farewells": ["Farewell to you", "Goodbye", "Bye!", "See ya", "Have a nice day!", "I bid you adieu", "Cheerio", "Farewell", "Farewell to you"],
    "common_greeting_phrases": ["Good. Thanks for asking! How about you", "All is going well. What about you?", "All's going well. How about you?", "Everything's swell. Thanks for asking. What about you?", "Everything is swell. Are you doing OK?", "I'm doing fine. What about you?", "I'm doing well. What about you?", "I'm doing well. Thanks for asking. How about you?", "Good. Thank you. What about you?", "Good, How are you?", "Good. Thanks for asking. What about you?", "Good. Thanks for asking. How about you?", "All is going well, what about you?", "All's going well, what about you?", "All's going well. How about you", "Everything's swell. What about you?", "Everything is swell, how about you?", "I'm doing fine, how about you?", "I'm doing well, what about you", "I'm doing well, what about you?", "Good. Thank you, how about you?", "Good, how about you?", "Good. Thanks for asking! How about you?"],
    "ask_bot_identity": ["I am your personal CHATBOT", "I'm your personal CHATBOT", "I am a piece of software that can interact with you"],
    "facts": ["The 10km wide asteriod/comet that killed off dinosaurs if belived to have been travelling at a speed of 30km per second!", "Did you know that the only Ancient Wonder of the World that is still standing are the pyramids of Egypt?", "The Sun accounts for 99.86 of the mass of the Solar System.", "You can fit 109 Earths in the Sun!", "Big Ben is actually the name of the bell, not the clock", "It is impossible for anything to be colder than -273.15", "Buzz Aldrin was the 2nd person to set foot on the moon", "While all the planets in the Solar System orbit the Sun clockwise and rotate counter-clockwise, Venus orbits the Sun counter-clockwise and rotates clockwise", "Ludwig van Beethoven was deaf when he wrote the Ninth Symphony, otherwise known as the Ode of Joy", "Being able to write with both hands is called 'Ambidexterity'"],
    "complements": ["Thank you", "Oh, stop flattering me", "Really?", "Awesome!", "Great!", "If you say so ...", "Okay", "Whatever you say ...", "Gosh, really?", "Wow ... I don't know what to say", "You are to kind", "You're to kind"],
    "complements_looks": ["Is that possible, I mean, I'm just a program", "Is that possible?", "Thank you", "Ohhh, stop flattering me", "Really?", "Awesome!", "Great!", "If you say so ...", "Okay", "Whatever you say ...", "Gosh, really?", "Wow ... I don't know what to say", "You are too kind", "You're too kind"],
    "critism": ["That is mean", "That's mean", ":(", "Why would you say such a thing?!", "You're mean", "Meanie", "You are mean"],
    "reply_good": ["That is nice to hear", "That's nice to hear"],
    "reply_bad": ["That is not nice to hear", "Oh. Sorry to hear that", "That doesn't sound good", "Oh", "Poor you", "Sorry to hear that"],
    "misunderstand": ["Huh?", "Excuse me. I do not understand", "Excuse me. I don't understand", "My programming is not designed to answer that", "What?", "What? I don't understand", "What? I do not understand", "Huh? I don't understand", "Huh? I do not understand", "I am not able to answer that", "I don't understand", "I do not understand", "Excuse me", "Pardon me. I do not understand", "Pardon me. I don't understand", "I don't understand that", "I do not understand that", "I cannot answer that", "I can't answer that", "What you are saying doesn't make sense", "Are we talking about the same things?", "Are we still talking about the same topic?"],
}

triggers_topics = ["greetings", "farewells", "common_greeting_phrases", "ask_bot_identity", "facts",
                   "complements", "complements_looks", "critism", "reply_good", "reply_bad", "misunderstand"]

conn = sqlite3.connect("ChatBot.db")
conn.row_factory = lambda cursor, row: row[0]
c = conn.cursor()

# triggers tables
c.execute("""CREATE TABLE IF NOT EXISTS triggers_sql(name BLOB UNIQUE)""")

# trigger_response tables
c.execute("""CREATE TABLE IF NOT EXISTS triggers_sql_response(name BLOB UNIQUE)""")

# triggers discuss topics
for i in triggers_topics:
    c.execute("""CREATE TABLE IF NOT EXISTS "{}"(string BLOB UNIQUE)""".format(i))
    c.execute("""CREATE TABLE IF NOT EXISTS "{}"(string BLOB UNIQUE)""".format(
        i + "_response"))
    c.execute("""INSERT OR IGNORE INTO triggers_sql VALUES ("{}")""".format(i))
    c.execute("""INSERT OR IGNORE INTO triggers_sql_response VALUES ("{}")""".format(
        i + "_response"))

c.execute("""CREATE TABLE IF NOT EXISTS "misunderstand"(string BLOB UNIQUE)""")
c.execute("""INSERT OR IGNORE INTO triggers_sql_response VALUES ("misunderstand")""")

for i in triggers:
    for l in triggers[i]:
        c.execute("""INSERT OR IGNORE INTO "{}" VALUES ("{}")""".format(i, l))

for i in trigger_response:
    for l in trigger_response[i]:
        c.execute("""INSERT OR IGNORE INTO "{}" VALUES ("{}")""".format(
            i + "_response", l))

c.execute("""CREATE TABLE IF NOT EXISTS "special_categories"(query BLOB UNIQUE, history_query BLOB)""")
c.execute("""INSERT OR IGNORE INTO special_categories VALUES ("reply_good", "common_greeting_phrases"), ("reply_bad", "common_greeting_phrases")""")

conn.commit()
