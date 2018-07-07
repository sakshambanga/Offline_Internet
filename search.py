import wikipedia
def s(query):
    return wikipedia.summary(query,sentences = 5)
