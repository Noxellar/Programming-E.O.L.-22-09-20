# ChatBot libraries

Username = input("WHAT IS YOUR NAME?: ")

change_chatbot_name_values = ["y", "Y", "n", "N"]

if Username == "HDB1":
    password = input("PASSWORD: ")
    while password != "Harrydebest1":
        print("ACCESS DENIED ... PLEASE TRY AGAIN")
        password = input("PASSWORD: ")
    else:
        Username = "HDB1"
        print("GREETING, HDB1, HOW MAY I HELP YOU TODAY?")
        chatbot_name = "CHATBOT"
else:
    change_chatbot_name = input("WOULD YOU LIKE TO NAME THIS CHATBOT. y/n: ")
    while change_chatbot_name not in change_chatbot_name_values:
        change_chatbot_name = input("PLEASE ENTER VALID VALUE. y/n: ")
    else:
        if change_chatbot_name in change_chatbot_name_values[0:2]:
            chatbot_name = input("PLEASE ENTER CHATBOT NAME : ")
        else:
            print("CHATBOT NAME WILL BE SET TO DEFAULT NAME, CHATBOT.")
            chatbot_name = "CHATBOT"

triggers = {
    "greetings": ["hello", "hi", "good day", "salutations"],
    "farewells": ["bye", "goodbye", "bye bye", "farewell", "see ya", "have a nice day", "have a good day", "I bid you adieu", "adios amigos", "hasta la vista", "ta-ta", "cheerio", "farewell to you"],
    "common_greeting_phrases": ["how do you do", "how are you", "hows everything", "hows everything going", "how are you going", "how is everything", "how is everything going", "how are you doing", "hows it going", "how is everything going"],
    "ask_bot_identity": ["who are you", "what are you", "may I ask you who you are", "what is your name", "may I ask you what you are", "may I ask what you are"],
    "facts": ["give me a fact", "I'm feeling curious", "fact", "can you give me a fact", "gimme a fact", "give me a fun fact", "fact me", "fun fact"],
    "complements": ["youre cool", "youre awesome", "youre amazing", "youre incredible", "youre the best"],
    "complements_looks": ["youre pretty", "you look nice", "you look handsome", "you look great"],
    "critism": ["youre ugly", "youre silly", "youre stupid", "youre the worst", "i hate you", "youre dumb", "youre useless", "silly thing", "youre a dummy"],
    "reply_good": ["good", "im good", "im good thanks", "im doing good", "im doing great", "yeah", "yes", "good thanks for asking"],
    "reply_bad": ["bad", "I'm not doing too good", "im not good. thanks for asking", "im not feeling too well", "im feeling down in the dumps", "no"],
}

trigger_response = {
    "greetings": ["Hello!", "Hi!", "Good day", "Salutations", "Hello, {}!".format(Username), "Hi, {}!".format(Username), "Good day, {}".format(Username), "Salutations, {}".format(Username)],
    "farewells": ["Farewell to you", "Goodbye", "Bye!", "See ya", "Have a nice day!", "I bid you adieu", "Ta-ta", "Cheerio", "Farewell", "Farewell to you, {}".format(Username), "Goodbye, {}".format(Username), "Bye, {}!".format(Username), "See ya, {}".format(Username), "Have a nice day, {}!".format(Username), "I bid you adieu, {}".format(Username), "Ta-ta, {}".format(Username), "Cheerio, {}".format(Username), "Farewell, {}".format(Username)],
    "common_greeting_phrases": ["Good. Thanks for asking! How about you", "All is going well. What about you?", "All's going well. How about you?", "Everything's swell. Thanks for asking. What about you?", "Everything is swell. Are you doing OK?", "I'm doing fine. What about you?", "I'm doing well. What about you?", "I'm doing well. Thanks for asking. How about you?", "Good. Thank you. What about you?", "Good, How are you?", "Good. Thanks for asking. What about you?", "Good. Thanks for asking. How about you?", "All is going well, what about you?", "All's going well, what about you?", "All's going well. How about you", "Everything's swell. What about you?", "Everything is swell, how about you?", "I'm doing fine, how about you?", "I'm doing well, what about you", "I'm doing well, what about you?", "Good. Thank you, how about you?", "Good, how about you?", "Good. Thanks for asking! How about you, {}".format(Username), "All is going well. What about you, {}?".format(Username), "All's going well. How about you, {}?".format(Username), "Everything's swell. Thanks for asking. What about you, {}?".format(Username), "Everything is swell. Are you doing OK, {}?".format(Username), "I'm doing fine. What about you, {}?".format(Username), "I'm doing well. What about you, {}?".format(Username), "I'm doing well. Thanks for asking. How about you, {}?".format(Username), "Good. Thank you. What about you, {}?".format(Username), "Good, How are you, {}?".format(Username), "Good. Thanks for asking. What about you, {}?".format(Username), "Good. Thanks for asking. How about you, {}?".format(Username), "All is going well, what about you, {}?".format(Username), "All's going well, what about you, {}?".format(Username), "All's going well. How about you, {}".format(Username), "Everything's swell. What about you, {}?".format(Username), "Everything is swell, how about you, {}?".format(Username), "I'm doing fine, how about you, {}?".format(Username), "I'm doing well, what about you, {}".format(Username), "I'm doing well, what about you, {}?".format(Username), "Good. Thank you, how about you, {}?".format(Username), "Good, how about you, {}?".format(Username)],
    "ask_bot_identity": ["I am your personal CHATBOT", "I'm your personal CHATBOT", "I am a piece of software that can interact with you", "I am your personal CHATBOT, {}".format(chatbot_name), "I'm your personal CHATBOT, {}".format(chatbot_name), "I am a piece of software that can interact with you, {}".format(Username), "I am your personal CHATBOT, {}".format(Username), "I'm your personal CHATBOT, {}".format(Username)],
    "facts": ["The 10km wide asteriod/comet that killed off dinosaurs if belived to have been travelling at a speed of 30km per second!", "Did you know that the only Ancient Wonder of the World that is still standing are the pyramids of Egypt?", "The Sun accounts for 99.86 of the mass of the Solar System.", "You can fit 109 Earths in the Sun!", "Big Ben is actually the name of the bell, not the clock", "It is impossible for anything to be colder than -273.15", "Buzz Aldrin was the 2nd person to set foot on the moon", "While all the planets in the Solar System orbit the Sun clockwise and rotate counter-clockwise, Venus orbits the Sun counter-clockwise and rotates clockwise", "Ludwig van Beethoven was deaf when he wrote the Ninth Symphony, otherwise known as the Ode of Joy", "Being able to write with both hands is called 'Ambidexterity'"],
    "complements": ["Thank you", "Oh, stop flattering me", "Really?", "Awesome!", "Great!", "If you say so ...", "Okay", "Whatever you say ...", "Gosh, really?", "Wow ... I don't know what to say", "You are to kind", "You're to kind"],
    "complements_looks": ["Is that possible, I mean, I'm just a program", "Is that possible?", "Thank you", "Ohhh, stop flattering me", "Really?", "Awesome!", "Great!", "If you say so ...", "Okay", "Whatever you say ...", "Gosh, really?", "Wow ... I don't know what to say", "You are too kind", "You're too kind"],
    "critism": ["That is mean", "That's mean", ":(", "Why would you say such a thing?!", "You're mean", "Meanie", "You are mean"],
    "reply_good": ["That is nice to hear", "That's nice to hear"],
    "reply_bad": ["That is not nice to hear", "Oh. Sorry to hear that", "That doesn't sound good", "Oh", "Poor you", "Sorry to hear that"],
    "misunderstand": ["Huh?", "Excuse me. I do not understand", "Excuse me. I dont understand", "My programming is not designed to answer that", "What?", "What? I dont understand", "What? I do not understand", "Huh? I dont understand", "Huh? I do not understand", "I am not able to answer that", "I dont understand", "I do not understand", "Excuse me", "Pardon me. I do not understand", "Pardon me. I dont understand", "I dont understand that", "I do not understand that", "I cannot answer that", "I can't answer that", "What you are saying doesn't make sense", "Are we talking about the same things?", "Are we still talking about the same topic?"],
}
