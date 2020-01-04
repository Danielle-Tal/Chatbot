import random

jokes_list = ["My dog used to chase people on a bike a lot. It got so bad, finally I had to take his bike away.",
              "Today at the bank, an old lady asked me to help check her balance. So I pushed her over.",
              "I couldn't figure out why the baseball kept getting larger. Then it hit me.",
              "I know a lot of jokes about unemployed people but none of them work.",
              "Did you hear about the italian chef that died? He pasta way",
              "Why is there a fence around a cemetery? People are dying to get in."]


def tell_a_joke():
    return random.choice(jokes_list)



