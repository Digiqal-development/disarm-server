﻿import spacy
nlp = spacy.load('en_core_web_sm')
import sys
        
def find_root_of_sentence(doc):
    root_token = None
    for token in doc:
        if (token.dep_ == "ROOT"):
            root_token = token
    return root_token
    

def find_other_verbs(doc, root_token):
    other_verbs = []
    for token in doc:
        ancestors = list(token.ancestors)
        if (token.pos_ == "VERB" and len(ancestors) == 1\
            and ancestors[0] == root_token):
            other_verbs.append(token)
    return other_verbs


def get_clause_token_span_for_verb(verb, doc, all_verbs):
    first_token_index = len(doc)
    last_token_index = 0
    this_verb_children = list(verb.children)
    for child in this_verb_children:
        if (child not in all_verbs):
            if (child.i < first_token_index):
                first_token_index = child.i
            if (child.i > last_token_index):
                last_token_index = child.i
    return(first_token_index, last_token_index)

def testMethod():
    return 3;



def main_part(text):
    sentence = text.get('sentence')
  
    doc = nlp(sentence)

    for token in doc:
        ancestors = [t.text for t in token.ancestors]
        children = [t.text for t in token.children]
        
    root_token = find_root_of_sentence(doc)
    other_verbs = find_other_verbs(doc, root_token)

    token_spans = []
    all_verbs = [root_token] + other_verbs

    for other_verb in all_verbs:
        (first_token_index, last_token_index) =  get_clause_token_span_for_verb(other_verb, doc, all_verbs)
        token_spans.append((first_token_index, last_token_index))

    sentence_clauses = []

    for token_span in token_spans:
        start = token_span[0]
        end = token_span[1]
        if (start < end):
            clause = doc[start:end]
            sentence_clauses.append(clause)

    sentence_clauses = sorted(sentence_clauses, key=lambda tup: tup[0])

    clauses_text = [clause.text for clause in sentence_clauses]
    print(clauses_text)
    return clauses_text


if __name__ == "__main__":
   
    if len(sys.argv) != 2:
        print("Argument length is longer than 1!")
        sys.exit(1)

    input_string = sys.argv[1]
    main_part(input_string)





