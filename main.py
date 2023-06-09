import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, SnowballStemmer
from nltk.stem import WordNetLemmatizer


def preprocess(text):
    # Tokenize the text
    tokens = word_tokenize(text)

    # Expand clitic contractions
    expanded_tokens = []
    for i, token in enumerate(tokens):
        if "'" in token:
            if token == "n't":
                if tokens[i-1] == "wo":
                    expanded_tokens.pop()
                    expanded_tokens.append("will")
                    expanded_tokens.append('not')
                elif tokens[i-1] == "ca":
                    expanded_tokens.pop()
                    expanded_tokens.append('can')
                    expanded_tokens.append('not')
                else:
                    expanded_tokens.append("not")
            elif "'s" in token:
                if tokens[i-1] == "let":
                    expanded_tokens.append("us")
                else:
                    expanded_tokens.append("is")
            elif "'m" in token:
                expanded_tokens.append("am")
            elif "'d" in token:
                expanded_tokens.append("would")
            elif "'ve" in token:
                expanded_tokens.append("have")
            elif "'re" in token:
                expanded_tokens.append("are")
            elif "'ll" in token:
                expanded_tokens.append("will")

            else:
                expanded_tokens.append(token)
        else:
            expanded_tokens.append(token)
    # ["m", "s", "d", "ve", "re", "ll"]
    # Tokenize multiword expressions
    # mwes = ["New York", "San Francisco", "Los Angeles", "Washington D.C."]
    # final_tokens = []
    # i = 0
    # while i < len(expanded_tokens):
    #     if i < len(expanded_tokens) - 1 and expanded_tokens[i] + " " + expanded_tokens[i + 1] in mwes:
    #         final_tokens.append(expanded_tokens[i] + " " + expanded_tokens[i + 1])
    #         i += 2
    #     else:
    #         final_tokens.append(expanded_tokens[i])
    #         i += 1

    return expanded_tokens


def stem(tokens):
    # Stem using the Porter stemmer
    porter = PorterStemmer()
    stemmed_tokens = [porter.stem(token) for token in tokens]

    # Stem using the Snowball stemmer
    snowball = SnowballStemmer("english")
    stemmed_tokens_snowball = [snowball.stem(token) for token in tokens]

    return stemmed_tokens, stemmed_tokens_snowball


def lemmatize(tokens):
    # Lemmatize using the WordNet lemmatizer
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]

    return lemmatized_tokens


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # text = "It'll be nice if we can't go outside. Let's stay indoors and watch a movie instead."    #text = "I'm going to New York and we're staying for a week. I love San Francisco, but I've never been to Los Angeles. Have you ever visited Washington D.C.?"
    text = "let's can't won't don't didn't goes playing plays played fairness "
    print(preprocess(text), "Tokens")
    print(stem(preprocess(text)), "Stemmer")
    print(lemmatize(preprocess(text)), "Lemmatizer")

