import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from joblib import dump

# Read the dataset
df = pd.read_csv('dataset.csv')

# Drop rows with missing 'text' values
df = df[pd.notnull(df["text"])]

# Select relevant columns
selected_classification = "Pattern Category"
col = ["text", selected_classification]
df = df[col]

# Create category_id column
df["category_id"] = df[selected_classification].factorize()[0]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    df['text'], df['category_id'], test_size=0.3, random_state=42
)

# Create a CountVectorizer to convert text into a matrix of token counts
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(X_train)

# Create a TfidfTransformer to transform the count matrix to TF-IDF representation
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

# Train a Multinomial Naive Bayes classifier
clf = MultinomialNB()
clf.fit(X_train_tfidf, y_train)

# Make predictions on the test set
X_test_counts = count_vect.transform(X_test)
X_test_tfidf = tfidf_transformer.transform(X_test_counts)
y_pred = clf.predict(X_test_tfidf)

# Evaluate the accuracy of the model
accuracy = metrics.accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Save the trained model and vectorizer for future use
dump(clf, 'category_classifier.joblib')
dump(count_vect, 'category_vectorizer.joblib')
