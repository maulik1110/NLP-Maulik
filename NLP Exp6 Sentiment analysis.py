#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install nltk


# In[2]:


import nltk
nltk.download('vader_lexicon')


# In[3]:


from nltk.sentiment.vader import SentimentIntensityAnalyzer

def analyze_sentiment(review):
    analyzer = SentimentIntensityAnalyzer()
    sentiment_score = analyzer.polarity_scores(review)
    return sentiment_score

def main():
    print("Welcome to Movie Review Sentiment Analysis")
    print("-----------------------------------------")
    review = input("Please enter your movie review: ")

    sentiment_score = analyze_sentiment(review)

    print("\nSentiment Analysis Result:")
    print("-------------------------")
    print(f"Positive: {sentiment_score['pos']:.2f}")
    print(f"Neutral: {sentiment_score['neu']:.2f}")
    print(f"Negative: {sentiment_score['neg']:.2f}")
    print(f"Compound: {sentiment_score['compound']:.2f}")

    if sentiment_score['compound'] >= 0.05:
        print("\nOverall Sentiment: Positive")
    elif sentiment_score['compound'] <= -0.05:
        print("\nOverall Sentiment: Negative")
    else:
        print("\nOverall Sentiment: Neutral")


# In[4]:


if __name__ == "__main__":
    main()


# In[5]:


if __name__ == "__main__":
    main()


# In[6]:


if __name__ == "__main__":
    main()


# In[7]:


if __name__ == "__main__":
    main()


# In[ ]:




