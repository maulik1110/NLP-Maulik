#!/usr/bin/env python
# coding: utf-8

# In[1]:


from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# In[2]:


def preprocess(text):
    tokens = word_tokenize(text.lower()) # Convert to lowercase for consistency

    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]

    return tokens


# In[3]:


def vectorize(tokens):
    # Vectorization
    vectorizer = CountVectorizer()
    token_matrix = vectorizer.fit_transform([" ".join(tokens), text]) # Create a matrix of token counts
    return token_matrix


# In[4]:


def summarize(text, top_n=2):
    tokens = preprocess(text)

    token_matrix = vectorize(tokens)

    similarity = cosine_similarity(token_matrix)[0] # Calculate similarity between the tokenized text and each sentence

    top_indices = similarity.argsort()[-top_n:][::-1] # Get indices of most similar sentences
    summary = [sentences[i] for i in top_indices] # Extract most similar sentences

    return ' '.join(summary)


# In[5]:


# Example text
text = """
Natural language processing (NLP) is a subfield of linguistics, computer science, and artificial intelligence concerned with the interactions between computers and human language. In particular, how to program computers to process and analyze large amounts of natural language data. Challenges in natural language processing frequently involve speech recognition, natural language understanding, and natural language generation.
"""


# In[8]:


sentences = sent_tokenize(text)

print(summary)


# In[9]:


def summarize(text, top_n=2):
    # Preprocess
    tokens = preprocess(text)

    token_matrix = vectorize(tokens)

    similarity = cosine_similarity(token_matrix)[0] # Calculate similarity between the tokenized text and each sentence
    print("Vector Similarity Scores:")
    for i, score in enumerate(similarity):
        print(f"Sentence {i+1}: {score}")

    top_indices = similarity.argsort()[-top_n:][::-1] # Get indices of most similar sentences
    sentences = sent_tokenize(text)
    summary = [sentences[i] for i in top_indices] # Extract most similar sentences

    return ' '.join(summary)

text = """
Natural language processing (NLP) is a subfield of linguistics, computer science, and artificial intelligence concerned with the interactions between computers and human language. In particular, how to program computers to process and analyze large amounts of natural language data. Challenges in natural language processing frequently involve speech recognition, natural language understanding, and natural language generation.
"""

summary = summarize(text)
print("\nSummary:")
print(summary)


# In[ ]:




