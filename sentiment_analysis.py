
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download VADER lexicon (run once)
nltk.download('vader_lexicon')

# Load CSV file (replace with your file path)
df = pd.read_csv("your_file.csv")

# Merge all feedback columns into one
feedback_columns = [
    'Well versed with the subject',
    'Explains concepts in an understandable way',
    'Use of presentations',
    'Degree of difficulty of assignments',
    'Solves doubts willingly',
    'Structuring of the course',
    'Provides support for students going above and beyond',
    'Course recommendation based on relevance'
]

df['All_Feedback'] = df[feedback_columns].fillna("").astype(str).agg(" ".join, axis=1)

# Sentiment Analysis
analyzer = SentimentIntensityAnalyzer()

def get_sentiment(text):
    score = analyzer.polarity_scores(text)['compound']
    if score > 0.05:
        return "Positive"
    elif score < -0.05:
        return "Negative"
    else:
        return "Neutral"

df['Sentiment'] = df['All_Feedback'].apply(get_sentiment)

# Plot Sentiment Distribution
sns.countplot(x='Sentiment', data=df, palette='coolwarm')
plt.title("Sentiment Distribution")
plt.show()

# Save results
df.to_csv("feedback_with_sentiment.csv", index=False)
print("Sentiment analysis complete. Saved as feedback_with_sentiment.csv")
