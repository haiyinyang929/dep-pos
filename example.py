import spacy
from spacy import displacy

# load the sapcy
nlp = spacy.load('en_core_web_sm')

while True:
    user_input = input("Enter a sentence: ")
    if not user_input or user_input == "":
        print("You did not enter a sentence. Please try again.")

    else:
        doc = nlp(user_input)

        for token in nlp(user_input):
            try:
                user_input = str(token)
            except ValueError:
                print("This sentences contains invalid characters. Please try again.")

        html = displacy.render(doc, style="dep")
        with open('dependency_graph.html', 'w', encoding='utf-8') as f:
            f.write(html)

        print("Dependency graph is written to dependency_graph.html")
        print("Here is the part of speech tagging of the sentence: ")
        for token in doc:
            print(f"{token.text}: {token.pos_}")
        break

