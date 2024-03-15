#!/usr/bin/env python
# coding: utf-8

# In[9]:


import re
from collections import Counter


# In[10]:


def tokenize_text(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return words


# In[11]:


def count_words(words):
    word_count = Counter(words)
    return word_count


# In[12]:


def main():
    input_text = input("Please enter the text: ")

    words = tokenize_text(input_text)

    word_count = count_words(words)

    for word, count in word_count.items():
        print(f'{word}: {count}')


# In[13]:


if __name__ == "__main__":
    main()

