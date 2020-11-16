import nltk

def main(something):
    sentence = "At eight o'clock on Thursday morning Arthur didn't feel very good."
    entities = nltk.chunk.ne_chunk(tagged)

    return {"message": entities}
