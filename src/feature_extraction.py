import re

def extract_features(text):
    features = {}
    
    # Extract invoice number
    invoice_number_match = re.search(r'Invoice Number: (\d+)', text)
    if invoice_number_match:
        features['invoice_number'] = invoice_number_match.group(1)
    else:
        features['invoice_number'] = None
    
    # Extract date
    date_match = re.search(r'Date: (\d{2}/\d{2}/\d{4})', text)
    if date_match:
        features['date'] = date_match.group(1)
    else:
        features['date'] = None
    
    # Extract total amount
    amount_match = re.search(r'Total Amount: \$(\d+\.\d{2})', text)
    if amount_match:
        features['amount'] = amount_match.group(1)
    else:
        features['amount'] = None
    
    return features
