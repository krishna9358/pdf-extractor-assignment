from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def compute_cosine_similarity(doc1, doc2):
    vectorizer = TfidfVectorizer().fit_transform([doc1, doc2])
    vectors = vectorizer.toarray()
    return cosine_similarity(vectors)[0, 1]
