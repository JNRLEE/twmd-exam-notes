import pdfplumber
import sys

def parse_ans(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        tables = pdf.pages[0].extract_tables()
        if not tables:
            print("No tables found by pdfplumber")
            text = pdf.pages[0].extract_text()
            print("Text mode instead:")
            print(text[:200])
        else:
            print("Table mode:")
            print(tables[0][:5])

parse_ans("/Users/jnrle/Documents/Projects/TWMD_EXAM/02_past_exams/raw_pdfs/mod_ans_med3.pdf")
