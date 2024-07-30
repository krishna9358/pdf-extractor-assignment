from text_extraction import extract_text_from_pdf
from feature_extraction import extract_features
from similarity_calculation import compute_cosine_similarity
from database import add_invoice_to_database, get_database

import os

def add_invoice(file_path):
    text = extract_text_from_pdf(file_path)
    features = extract_features(text)
    add_invoice_to_database(file_path, text, features)

def find_most_similar_invoice(file_path):
    text = extract_text_from_pdf(file_path)
    features = extract_features(text)
    
    highest_similarity = 0
    most_similar_invoice = None
    
    for db_file_path, db_text, db_features in get_database():
        similarity = compute_cosine_similarity(text, db_text)
        if similarity > highest_similarity:
            highest_similarity = similarity
            most_similar_invoice = (db_file_path, similarity)
    
    return most_similar_invoice

def load_train_invoices(train_dir):
    for invoice_file in os.listdir(train_dir):
        add_invoice(os.path.join(train_dir, invoice_file))

def compare_test_invoices(test_dir):
    results = []
    for invoice_file in os.listdir(test_dir):
        test_invoice_path = os.path.join(test_dir, invoice_file)
        most_similar = find_most_similar_invoice(test_invoice_path)
        if most_similar:
            results.append((invoice_file, most_similar[0], most_similar[1]))
        else:
            results.append((invoice_file, None, 0))
    return results

if __name__ == "__main__":
    # Directories containing train and test invoices
    train_dir = '../data/train/'
    test_dir = '../data/test/'

    # Load train invoices into the database
    load_train_invoices(train_dir)

    # Compare test invoices and print the results
    results = compare_test_invoices(test_dir)
    for test_file, similar_file, score in results:
        if similar_file:
            print(f"Test Invoice: {test_file} | Most Similar: {similar_file} | Similarity Score: {score}")
        else:
            print(f"Test Invoice: {test_file} | No similar invoice found.")
