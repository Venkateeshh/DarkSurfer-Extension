import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from joblib import dump

selected_classification = "Pattern Category"

df = pd.read_csv('dataset.csv')

df = df[pd.notnull(df["text"])]
col = ["text", selected_classification]
df = df[col]

df["category_id"] = df[selected_classification].factorize()[0]
category_id_df = df[[selected_classification, 'category_id']
                    ].drop_duplicates().sort_values('category_id')
category_to_id = dict(category_id_df.values)
id_to_category = dict(
    category_id_df[['category_id', selected_classification]].values)

tfidf = TfidfVectorizer(sublinear_tf=True, min_df=5, norm='l2',
                        encoding='latin-1', ngram_range=(1, 2), stop_words='english')

features = tfidf.fit_transform(df["text"]).toarray()
labels = df.category_id

X_train, X_test, y_train, y_test = train_test_split(
    df['text'], df[selected_classification], train_size=.3)
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(X_train)
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

clf = MultinomialNB().fit(X_train_tfidf, y_train)

y_pred = clf.predict(count_vect.transform(X_test))

print("Accuracy:", metrics.accuracy_score(y_pred, y_test))

dump(clf, 'category_classifier.joblib')
dump(count_vect, 'category_vectorizer.joblib')

num_examples = 5 



print("\nExamples of Predicted vs Actual Labels:")
for i in range(min(num_examples, len(X_test))):
    try:
        actual_label = id_to_category[y_test.iloc[i]]
    except KeyError:
        actual_label = f" (ID: {y_test.iloc[i]})"
    
    try:
        predicted_label = id_to_category[y_pred[i]]
    except KeyError:
        predicted_label = f" (ID: {y_pred[i]})"
    
    print(f"\nExample {i + 1}:")
    print(f"Text: {X_test.iloc[i]}")
    print(f"Actual Label: {actual_label}")
    print(f"Predicted Label: {predicted_label}")

print("Unique values in y_test:", y_test.unique())
print("Unique values in y_pred:", pd.Series(y_pred).unique())

print("id_to_category dictionary:", id_to_category)
