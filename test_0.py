import pandas as pd
import numpy as np
import sqlite3
import streamlit as st
from io import BytesIO
import PyPDF2
import pdfplumber
from pdf2image import convert_from_bytes
import pytesseract
from api import main_func

# Function to get data from the database
def get_data():
    conn = sqlite3.connect('financial_data.db')
    query = "SELECT * FROM transactions"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def extract_text_from_pdf(byte_io_pdf):
    all_text = ""
    with pdfplumber.open(BytesIO(byte_io_pdf.getvalue())) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            print(f"Extracting text from page {page_num}...")
            page_text = page.extract_text()
            if page_text:
                all_text += f"--- Page {page_num} ---\n{page_text}\n\n"
            else:
                print(f"Warning: No text extracted from page {page_num} using pdfplumber. Trying OCR...")
                all_text += ocr_extract_from_pdf_page(byte_io_pdf, page_num)

    return all_text

# Function to extract text using OCR (for scanned PDFs)
def ocr_extract_from_pdf_page(byte_io_pdf, page_num):
    # Specify poppler_path for convert_from_bytes (if needed)
    poppler_path = "C:/Users/sneh/Desktop/poppler-24.08.0/Library/bin"  # Update this with the actual path if different

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update this path if necessary
    # Convert from ByteIO instead of file path
    images = convert_from_bytes(byte_io_pdf.getvalue(), first_page=page_num, last_page=page_num, poppler_path=poppler_path)
    
    ocr_text = ""

    for img in images:
        text = pytesseract.image_to_string(img, lang='eng')  # OCR the image to extract text
        ocr_text += text

    return ocr_text



# Function to update the data in the database
def update_data(row_id, client_name, bank_name, account_number, transaction_date, credit_debit, description, amount, balance):
    conn = sqlite3.connect('financial_data.db')
    cursor = conn.cursor()
    cursor.execute('''UPDATE transactions 
                      SET client_name = ?, bank_name = ?, account_number = ?, 
                          transaction_date = ?, credit_debit = ?, description = ?, 
                          amount = ?, balance = ?
                      WHERE id = ?''',
                   (client_name, bank_name, account_number, transaction_date, credit_debit, description, amount, balance, row_id))
    conn.commit()
    conn.close()

def insert_data_into_db(df):
    conn = sqlite3.connect('financial_data.db')
    cursor = conn.cursor()
    
    for _, row in df.iterrows():
        cursor.execute('''INSERT INTO transactions (client_name, bank_name, account_number, 
                                                    transaction_date, credit_debit, description, 
                                                    amount, balance)
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', 
                       (row['client_name'], row['bank_name'], row['account_number'], 
                        row['transaction_date'], row['credit_debit'], row['description'], 
                        row['amount'], row['balance']))
    
    conn.commit()
    conn.close()

# Display the title
st.title('Financial Transactions')

# Debugging: Check if Streamlit is rendering the title correctly
st.write("Debug: App started, rendering title and file uploader.")

# Step 1: Upload PDF
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")






# Debugging: Check if file is uploaded
# st.write("Debug: Uploaded file: ", uploaded_file)

if uploaded_file is not None:
    
    # Step 2: Process the uploaded PDF and extract data
    # Placeholder for your data extraction logic
    st.info("Processing the PDF file...")

    # INSERT TANAY's CODE HERE (return a data *pd.DataFrame*)
    # text=extract_text_from_pdf(uploaded_file)

    text = """[
        ("Mr. John Doe", "B1 Bank", "1261234567", "08/19/2020", "Credit", "Correction: Cash Withdrawal Cpg", 100.00, 132.27),
        ("Mr. John Doe", "B1 Bank", "1261234567", "08/19/2020", "Credit", "Correction: ATS Cash vataraval Fee", 6.56, 138.83),
        ("Mr. John Doe", "B1 Bank", "1261234567", "08/31/2020", "Credit", "Banking App Payment Received A Pieterse", 1000.00, 1138.83),
        ("Mr. John Doe", "B1 Bank", "1261234567", "08/31/2020", "Debit", "Banking App Payment Luna", 100.00, 1038.83),
        ("Mr. John Doe", "B1 Bank", "1261234567", "08/31/2020", "Debit", "Banking App Payment Fee", 1.60, 1037.23),
        ("Mr. John Doe", "B1 Bank", "1261234567", "08/31/2020", "Debit", "ATM Balance Enquiry Fee", 5.55, 1031.68),
        ("Mr. John Doe", "B1 Bank", "1261234567", "08/31/2020", "Debit", "ATM Cash Withdrawal Spar Panorama (Card 1551)", 1000.00, 31.68),
        ("Mr. John Doe", "B1 Bank", "1261234567", "08/31/2020", "Debit", "Cash Withdrawal Fee (ATM)", 8.83, 22.85),
        ("Mr. John Doe", "B1 Bank", "1261234567", "08/31/2020", "Credit", "Interest Received", 1.49, 24.34),
        ("Mr. John Doe", "B1 Bank", "1261234567", "08/31/2020", "Debit", "SMS Notification Fee", 0.80, 23.54),
        ("Mr. John Doe", "B1 Bank", "1261234567", "08/31/2020", "Debit", "Monthly Account Admin Fee", 5.80, 17.74),
        ("Mr. John Doe", "B1 Bank", "1261234567", "09/01/2020", "Credit", "Banking App Payment Received A Pieterse", 200.00, 217.74)
    ]"""

    data = main_func(text)   ###IDHAR COMMENT KIYA HAI

    print(f"DATAFRAME: {data}")

    # Example Data Extraction Process (Replace this with your actual PDF extraction code)
    # DATA EXTRACTION CODE HERE
    st.write("Debug: PDF processing step")

    # For demo purposes, we're creating a dummy DataFrame
    # data = pd.DataFrame({
    #     'id': [1, 2, 3],
    #     'client_name': ['Alice', 'Bob', 'Charlie'],
    #     'bank_name': ['Bank A', 'Bank B', 'Bank C'],
    #     'account_number': ['123456', '234567', '345678'],
    #     'transaction_date': ['2024-01-10', '2024-02-11', '2024-03-12'],
    #     'credit_debit': ['Credit', 'Debit', 'Credit'],
    #     'description': ['Transaction A', 'Transaction B', 'Transaction C'],
    #     'amount': [1000.0, 2000.0, 3000.0],
    #     'balance': [15000.0, 18000.0, 21000.0]
    # })

    st.success("PDF processed successfully!")
    st.write("Debug: Data extracted, displaying DataFrame")

    # Display the extracted data
    st.subheader("Extracted Data")
    st.dataframe(data)

    if st.button('Save Extracted Data to Database'):
        conn = sqlite3.connect('financial_data.db')
        print(f"Connection Successful to DB : {conn}")
        data.to_sql('transactions', conn, if_exists='append', index=False)
        conn.close()
        st.success("Data saved to database successfully!")
        # insert_data_into_db(data)
        st.write("Debug: Data saved to DB")


# check is connection was successful with db

    # Step 3: After saving, load the data from the database
    data = get_data()

    if len(data) > 0:
        # Display data in a table-like format
        st.subheader('Editable Data from Database')
        st.dataframe(data)

        # Allow the user to edit a specific row of the data
        selected_id = st.number_input('Enter the row ID to edit', min_value=1, max_value=len(data), step=1)

        if selected_id:
            row_data = data[data['id'] == selected_id].iloc[0]

            # Create editable fields
            client_name = st.text_input('Client Name', row_data['client_name'])
            bank_name = st.text_input('Bank Name', row_data['bank_name'])
            account_number = st.text_input('Account Number', row_data['account_number'])
            transaction_date = st.text_input('Transaction Date', row_data['transaction_date'])
            credit_debit = st.selectbox('Credit/Debit', ['Credit', 'Debit'], index=(0 if row_data['credit_debit'] == 'Credit' else 1))
            description = st.text_input('Description', row_data['description'])
            amount = st.number_input('Amount', value=row_data['amount'])
            balance = st.number_input('Balance', value=row_data['balance'])

            # Save button to update the data
            if st.button('Save Changes'):
                update_data(selected_id, client_name, bank_name, account_number, transaction_date, credit_debit, description, amount, balance)
                st.success(f'Row {selected_id} updated successfully!')
    else:
        st.warning("No data available for display.")
else:
    st.info("Please upload a PDF file to begin.")