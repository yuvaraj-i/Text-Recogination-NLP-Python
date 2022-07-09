import spacy

# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_sm")

text = ""

# Process whole documents
with open("../testfile.txt", "r") as f:
        text = f.read()

doc = nlp(text)

# Find phrases and concepts
for word in doc:
        if(word.pos_ == "VERB" or word.pos_ == "NOUN"):
                print(word, spacy.explain(word.pos_),)

# Find named entities
for word in doc.ents:
        print(word.text, word.label_, sep="-")


