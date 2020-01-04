"""
This is the template server side for ChatBot
"""
from bottle import route, run, template, static_file, request
import json
import jokes
import feedparser
import curses


@route('/', method='GET')
def index():
    return template("chatbot.html")


@route("/chat", method='POST')
def chat():
    user_message = request.POST.get('msg').lower()
    user_words = user_message.split()
    if any(word in user_words for word in curses.curses):
        return json.dumps({"animation": "no", "msg": curses.curse_res()})
    elif user_message == "hi" or user_message == "hello":
        return json.dumps({"animation": "excited", "msg": "hi how are you?"})
    elif "joke" in user_message:
        return json.dumps({"animation": "laughing", "msg": jokes.tell_a_joke()})
    elif "i love you" in user_message:
        return json.dumps({"animation": "inlove", "msg": "I love you too!"})
    elif "i don't love you" in user_message:
        return json.dumps({"animation": "heartbroke", "msg": "That hurts"})
    elif "money" in user_message:
        return json.dumps({"animation": "money", "msg": "money money money"})
    elif "dog" in user_message:
        return json.dumps({"animation": "dog", "msg": "i love dogs"})
    elif "name" in user_message:
        return json.dumps({"animation": "dancing", "msg": f'Hi {user_words[user_words.index("name")+2].capitalize()},'
                                                          f'nice to meet you.'})
    elif "news" in user_message:
        res = feedparser.parse("https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml")
        return json.dumps({"animation": "ok", "msg": res.entries[0].title})
    elif "sad" in user_message:
        return json.dumps({"animation": "crying", "msg": "That makes me sad"})
    elif "happy" in user_message:
        return json.dumps({"animation": "giggling", "msg": "i am happy too"})
    elif "boo" in user_message:
        return json.dumps({"animation": "afraid", "msg": "I want my mommy"})
    elif "ready" in user_message:
        return json.dumps({"animation": "takeoff", "msg": "I am ready. Are you?"})
    elif "nothing" in user_message:
        return json.dumps({"animation": "bored", "msg": "What shall we do now?"})
    elif "thank you" in user_message:
        return json.dumps({"animation": "excited", "msg": "you are welcome"})
    else:
        return json.dumps({"animation": "confused", "msg": "I'm sorry. I don't understand what you want"})


@route("/test", method='POST')
def chat():
    user_message = request.POST.get('msg')
    return json.dumps({"animation": "inlove", "msg": "I'm sorry. I don't understand what you want"})


@route('/js/<filename:re:.*\.js>', method='GET')
def javascripts(filename):
    return static_file(filename, root='js')


@route('/css/<filename:re:.*\.css>', method='GET')
def stylesheets(filename):
    return static_file(filename, root='css')


@route('/images/<filename:re:.*\.(jpg|png|gif|ico)>', method='GET')
def images(filename):
    return static_file(filename, root='images')


def main():
    run(host='localhost', port=7000)

if __name__ == '__main__':
    main()
