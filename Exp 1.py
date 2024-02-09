#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
from nltk.tokenize import word_tokenize, sent_tokenize, regexp_tokenize, TweetTokenizer , SpaceTokenizer


# In[2]:


nltk.download('punkt')


# In[3]:


text = input("Enter your text: ")


# In[4]:


word_tokens = word_tokenize(text)
print("Word Tokenization:")
print(word_tokens)


# In[7]:


tweet_tokenizer = TweetTokenizer()
tweet_tokens = tweet_tokenizer.tokenize(text)
print("\nTweet Tokenization:")
print(tweet_tokens)


# In[8]:


space_tokenizer = SpaceTokenizer()
space_tokens = space_tokenizer.tokenize(text)
print("Space Tokenization:")
print(space_tokens)


# In[9]:


text = input("maulik is building @pets app @CU")


# In[10]:


regexp_tokens = regexp_tokenize(text, pattern=r'\w+|\$[\d\.]+|\S+')
print("\nRegExp Tokenization:")
print(regexp_tokens)


# In[11]:


import re


# In[16]:


text = "maulik is building @pets app, @CU."
pattern = r'\w+|\S'
regexp_tokens = re.findall(pattern, text)


# In[17]:


print(regexp_tokens)


# In[18]:


text="@here is good #deal"
tweet_tokenizer = TweetTokenizer()
tweet_tokens = tweet_tokenizer.tokenize(text)
print("\nTweet Tokenization:")
print(tweet_tokens)


# In[ ]:




