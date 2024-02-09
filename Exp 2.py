#!/usr/bin/env python
# coding: utf-8

# In[7]:


import nltk

# Sample sentence
sentence = "The quick brown fox jumps over the lazy dog."

# Tokenize the sentence
tokens = nltk.word_tokenize(sentence)

# Perform POS tagging
pos_tags = nltk.pos_tag(tokens)

# Print POS tagged tokens
print("POS tagged tokens:")
print(pos_tags)


# In[8]:


import nltk
nltk.download('averaged_perceptron_tagger')


# In[11]:


import nltk


# In[26]:


sentence = "i am creating a posttagging maulik."

tokens = nltk.word_tokenize(sentence)
pos_tags = nltk.pos_tag(tokens)


# In[27]:


print("POS tagged tokens:")
print(pos_tags)


# In[ ]:




