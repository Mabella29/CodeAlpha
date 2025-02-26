import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

class FAQChatbot:
    def __init__(self, csv_path):
        # Load the FAQ dataset
        self.data = pd.read_csv(csv_path)
        self.questions = self.data['Question'].tolist()
        self.answers = self.data['Answer'].tolist()

        # greeting questions and responses
        self.greetings = {
            'hi': 'Hello! How can I assist you today?',
            'hello': 'Hi there! How may I help you?',
            'hey': 'Hi there! How may I help you?',
            'good morning': 'Good morning! What can I do for you?',
            'good evening': 'Good evening! How can I assist you today?',
        }
        
        # Initialize NLP tools
        self.lemmatizer = WordNetLemmatizer()
        self.vectorizer = TfidfVectorizer()

        # Preprocess all questions once
        self.processed_questions = [self.preprocess_text(q) for q in self.questions]
        # Create TF-IDF matrix for all questions
        self.question_vectors = self.vectorizer.fit_transform(self.processed_questions)

    def preprocess_text(self, text):
        """Preprocess the input text"""
        # Convert to lowercase and remove punctuation
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)
        
        # Tokenize
        tokens = word_tokenize(text)
        
        # Remove stopwords and lemmatize
        tokens = [self.lemmatizer.lemmatize(word) 
                 for word in tokens 
                 if word not in stopwords.words()]
        
        return ' '.join(tokens)

    def find_best_match(self, user_question, threshold=0.3):
        """Find the most similar question in the FAQ dataset"""
        
        # Check if the question is a greeting
        user_question_lower = user_question.lower()
        if user_question_lower in self.greetings:
            return {
                'answer': self.greetings[user_question_lower],
                'confidence': 1.0,
                'matched_question': user_question
            }
        
        # Preprocess user question
        processed_question = self.preprocess_text(user_question)
        
        # Vectorize user question using the same vectorizer
        question_vector = self.vectorizer.transform([processed_question])
        
        # Calculate similarity with all FAQ questions
        similarities = cosine_similarity(question_vector, self.question_vectors)[0]
        
        # Find best match
        best_match_idx = np.argmax(similarities)
        
        if similarities[best_match_idx] >= threshold:
            return {
                'answer': self.answers[best_match_idx],
                'confidence': similarities[best_match_idx],
                'matched_question': self.questions[best_match_idx]
            }
        else:
            return {
                'answer': "I'm sorry, I couldn't find a good match for your question. Could you please rephrase it?",
                'confidence': similarities[best_match_idx],
                'matched_question': None
            }

# Example usage
def main():
    # Initialize chatbot
    chatbot = FAQChatbot('university_faq.csv')  # Update with the correct file path
    
    # Interactive loop
    while True:
        user_input = input("Enter your question (or 'quit' to exit): ")
        if user_input.lower() == 'quit':
            break
            
        response = chatbot.find_best_match(user_input)
        print("\nMatched Question:", response['matched_question'])
        print("Confidence Score:", response['confidence'])
        print("Answer:", response['answer'])
        print()

if __name__ == "__main__":
    main()
