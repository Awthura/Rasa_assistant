import json
import csv
import pandas as pd
import spacy
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

csv_file = 'book_clusters.csv'
with open('names.json', 'r') as f:
        book_names = json.load(f)


def custom_feature_extraction(book_names, important_words):
    # Create an empty dataframe to store the features
    features = pd.DataFrame()
    # Loop through the important words and create a binary feature for each word
    for word in important_words:
        features[word] = [int(word in name) for name in book_names]
    return features


def json_to_tfidf(json_file):
    # Load the JSON file
    with open(json_file, 'r') as f:
        book_names = json.load(f)
    # Create an instance of the CountVectorizer
    stop_words = ["book", "buch"]
    stop_words.extend(CountVectorizer(stop_words='english').get_stop_words())
    vectorizer = CountVectorizer(stop_words=stop_words,max_df=0.95, min_df=0.05,ngram_range=(1, 2))
    X = vectorizer.fit_transform(book_names)
    book_names_df = pd.DataFrame(book_names, columns=["book_name"])
    book_features = custom_feature_extraction(book_names_df['book_name'], important_words)
    X = np.concatenate([X.toarray(), book_features], axis=1)
    return X

important_words = ["engineering","medical","business", "english", "machine", "market", "programming", "computer", "politics","logic","economy","environment","geography"]
json_file = 'names.json'
book_vectors = json_to_tfidf(json_file)



def cluster_books(book_vectors, n_clusters):
    best_score = -1
    best_n_components = None
    for n_components in range(2, n_clusters + 1):
        # Create an instance of the GMM model
        gmm = GaussianMixture(n_components=n_components)
        # Fit the model to the book features
        labels = gmm.fit_predict(book_vectors)
        # Compute the silhouette score
        score = silhouette_score(book_vectors, labels)
        if score > best_score:
            best_score = score
            best_n_components = n_components
    # Re-train the model with the best number of components
    gmm = GaussianMixture(n_components=best_n_components)
    labels = gmm.fit_predict(book_vectors)
    return labels

n_clusters = 20
book_labels = cluster_books(book_vectors, n_clusters)

def cluster_books(book_vectors, n_clusters):
    best_score = -1
    best_n_components = None
    for n_components in range(2, n_clusters + 1):
        # Create an instance of the GMM model
        gmm = GaussianMixture(n_components=n_components)
        # Fit the model to the book vectors
        labels = gmm.fit_predict(book_vectors)
        # Compute the silhouette score
        score = silhouette_score(book_vectors, labels)
        if score > best_score:
            best_score = score
            best_n_components = n_components
    # Re-train the model with the best number of components
    gmm = GaussianMixture(n_components=best_n_components)
    labels = gmm.fit_predict(book_vectors)
    return labels


from sklearn.metrics import davies_bouldin_score

def evaluate_clusters_dbi(book_vectors, labels):
    # Compute the Davies-Bouldin index
    score = davies_bouldin_score(book_vectors, labels)
    return score

cluster_score_dbi = evaluate_clusters_dbi(book_vectors, book_labels)
print("Davies-Bouldin index: ", cluster_score_dbi)


def evaluate_clusters(book_vectors, labels):
    # Compute the silhouette score
    score = silhouette_score(book_vectors, labels)
    return score

cluster_score = evaluate_clusters(book_vectors, book_labels)
print("Silhouette Score: ", cluster_score)

import csv

def write_to_csv(book_names, labels, csv_file):
    with open(csv_file, mode='w', newline='') as csv_file:
        fieldnames = ['Book Name', 'Cluster Label']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for i in range(len(book_names)):
            writer.writerow({'Book Name': book_names[i], 'Cluster Label': labels[i]})


write_to_csv(book_names, book_labels, csv_file)