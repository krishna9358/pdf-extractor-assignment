# Invoice Comparator

This project compares invoices based on text content and structure using cosine similarity. 

## Project Structure

- `data/`: Directory containing invoice PDFs.
- `src/`: Directory containing source code.
  - `text_extraction.py`: Functions to extract text from PDFs.
  - `feature_extraction.py`: Functions to extract features from text.
  - `similarity_calculation.py`: Functions to calculate similarity between invoices.
  - `database.py`: Functions to manage the invoice database.
  - `main.py`: Main script to run the program.
- `requirements.txt`: Dependencies for the project.
- `README.md`: Project documentation.


## Setup

1. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
2. Place your invoice PDFs in the `data` directory. Create `data` directory and inside it create two more directory named as `train` and `test`.  

3. Run the script:
    ```
    python src/main.py
    ```
