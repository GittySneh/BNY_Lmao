def correct_json_format(extracted_text):
    """
    This function parses the extracted text to ensure that it ends with a valid closing bracket for the list.
    If there is a misplaced ')' after the last transaction, it will be removed, and the correct ']' bracket
    will be placed.
    """
    # Find the last occurrence of closing square bracket ']'
    closing_bracket_pos = extracted_text.rfind(']')
    
    # If the closing bracket is found, discard everything after it
    if closing_bracket_pos != -1:
        return extracted_text[:closing_bracket_pos + 1]  # Include the closing bracket and discard the rest
    
    # If no closing bracket ']' is found, look for a misplaced ')' and fix it
    closing_parenthesis_pos = extracted_text.rfind(')')
    
    if closing_parenthesis_pos != -1:
        # Replace the ')' with a ']'
        corrected_text = extracted_text[:closing_parenthesis_pos] + ']'
        return corrected_text
    
    # If neither is found, just return the original string as a fallback
    return extracted_text

def main_func(extracted_text1):
    import pandas as pd
    import ast
    import os
    os.environ["GOOGLE_API_KEY"]="AIzaSyAjEGxP6kezlPGu4NTFTId3KsYLldzCMro"
    # Import the Python SDK
    import google.generativeai as genai
    # Used to securely store your API key
    import google.generativeai as genai
    import os

    # Retrieve the API key from environment variables
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    genai.configure(api_key=GOOGLE_API_KEY)

    model = genai.GenerativeModel('gemini-pro')

    print("DATA RECEIVED", extracted_text1)

    instruction1 =''' You are a brilliant bank statment extractor .Using the following example , extract bank statements in the exact format as given below.
    1) YOU MUST RETURN THE EXACT FORMAT GIVEN BELOW AND DO NOT DEVIATE FROM IT
    2) RETURN A LIST CONSISTING OF VARIOUS TRANSACTIONS WITH THEIR ATTRIBUTES
    3) COMPLETE EACH TRANSACTION AND END WITH "]"
    For example  :-
    SUMMARY:-
    Savings Account Statement Summary
    Account Holder: Mr. John Doe
    Address: 1 Stuart Place, Northcliff Ext1, Test City, 21950

    Bank: B1 Bank Limited
    Branch: 470010
    Device: 9003
    Statement Date: 30/09/2020
    Account Number: 1261234567

    Account Summary
    Previous Balance: R453.61
    Total Money In: R4,061.00
    Total Money Out: R3,793.00
    New Balance: R1,936.42
    Transactions
    Money In:

    31/08/2020: Correction: Cash Withdrawal Cpg. - R100.00
    31/08/2020: Correction: ATM Cash Withdrawal Fee - R6.56
    31/08/2020: Banking App Payment Received A Pieterse - R1,000.00
    31/08/2020: Banking App Payment Lung - R1.49
    31/08/2020: ATM Balance Enquiry Fee - R200.00
    31/08/2020: ATM Cash Withdrawal Spar Panorama (Card 1551) - R200.00
    31/08/2020: Interest Received - R1,600.00
    31/08/2020: SMS Notification Fee - R150.00
    01/09/2020: Monthly Account Admin Fee - R500.00
    01/09/2020: Banking App Payment Received A Pieterse - R1,600.00
    01/09/2020: Cash Withdrawal Fee (ATM) - R150.00
    02/09/2020: ATM Cash Withdrawal Spar Panorama (Card 1551) - R1,000.00
    02/09/2020: Banking App Payment Received A Pieterse - R400.00
    02/09/2020: Banking App Payment Received A Pieterse - R100.00
    02/09/2020: Purchase & Cash: Mode! Melkwinkel N16227 - R200.00
    03/09/2020: Banking App Payment Received A Pieterse - R1,600.00
    03/09/2020: ATM Cash Withdrawal Spar Panorama (Card 1551) - R1,000.00
    03/09/2020: Cash Withdrawal Fee (ATM) - R150.00
    04/09/2020: SMS Notification Fee - R1,000.00
    05/09/2020: ATM Cash Withdrawal Absa Magalies Centre (Card 1551) - R1,000.00
    Total Money In: R4,061.00

    Money Out:

    31/08/2020: Cash Withdrawal Fee (ATM) - R132.27
    31/08/2020: Banking App Payment Fee - R138.83
    31/08/2020: ATM Cash Withdrawal Spar Panorama (Card 1551) - R1,000.00
    01/09/2020: Cash Withdrawal Fee (ATM) - R1.60
    01/09/2020: ATM Balance Enquiry Fee - R5.55
    01/09/2020: Banking App Payment Received A Pieterse - R100.00
    01/09/2020: SMS Notification Fee - R8.83
    02/09/2020: Cash Withdrawal Fee (ATM) - R24.34
    02/09/2020: ATM Balance Enquiry Fee - R0.80
    02/09/2020: ATM Cash Withdrawal Spar Panorama (Card 1551) - R5.55
    02/09/2020: Banking App Payment Received A Pieterse - R100.00
    02/09/2020: SMS Notification Fee - R8.83
    02/09/2020: ATM Cash Withdrawal Absa Magalies Centre (Card 1551) - R0.40
    03/09/2020: Cash Withdrawal Fee (ATM) - R8.83
    03/09/2020: ATM Cash Withdrawal Absa Magalies Centre (Card 1551) - R230.00
    04/09/2020: Banking App Payment Received J Bronn - R70.00
    04/09/2020: ATM Cash Withdrawal Absa Panorama Centre (Card 1551) - R600.00
    05/09/2020: Cash Withdrawal Fee (ATM) - R1.20
    05/09/2020: Banking App Prepaid Purchase MTN - R50.00
    Total Money Out: R3,793.00

    Notes:

    VAT Registration Number: 46812345678
    Document Number: 2c05a1ce-6b84-47e9-9863-1fde19b1ea8e
    For inquiries, please contact B1 Bank Limited.

    EXTRACTION :-

    [
        ("Mr. John Doe", "B1 Bank", "1261234567", "08/19/2020", "Credit", "Correction: Cash Withdrawal Cpc", 100.00, 132.27),
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
        ("Mr. John Doe", "B1 Bank", "1261234567", "09/01/2020", "Credit", "Banking App Payment Received A Pieterse", 200.00, 217.74),
        ("Mr. John Doe", "B1 Bank", "1261234567", "09/01/2020", "Debit", "ATM Cash Withdrawal Spar Panorama (Card 1551)", 190.00, 27.74),
        ("Mr. John Doe", "B1 Bank", "1261234567", "09/01/2020", "Debit", "Cash Withdrawal Fee (ATM)", 8.83, 18.91),
        ("Mr. John Doe", "B1 Bank", "1261234567", "09/01/2020", "Credit", "Banking App Payment Received A Pieterse", 200.00, 218.91),
        ("Mr. John Doe", "B1 Bank", "1261234567", "09/01/2020", "Credit", "Banking App Payment Received A Pieterse", 1000.00, 1218.91),
        ("Mr. John Doe", "B1 Bank", "1261234567", "09/01/2020", "Debit", "Purchase & Cash: Model Melkwinkel N16227 Brits (Card 1551)", 1031.70, 187.21),
        ("Mr. John Doe", "B1 Bank", "1261234567", "09/01/2020", "Debit", "Till Cash Withdrawal Fee", 1.61, 185.60),
        ("Mr. John Doe", "B1 Bank", "1261234567", "09/01/2020", "Credit", "Banking App Payment Received A Pieterse", 400.00, 585.60),
        ("Mr. John Doe", "B1 Bank", "1261234567", "09/01/2020", "Credit", "Banking App Payment Received A Pieterse", 100.00, 685.60),
        ("Mr. John Doe", "B1 Bank", "1261234567", "09/01/2020", "Debit", "ATM Balance Enquiry Fee", 5.55, 680.05),
        ("Mr. John Doe", "B1 Bank", "1261234567", "09/01/2020", "Debit", "ATM Cash Withdrawal Spar Panorama (Card 1551)", 600.00, 80.05),
        ("Mr. John Doe", "B1 Bank", "1261234567", "09/01/2020", "Debit", "Cash Withdrawal Fee (ATM)", 8.83, 71.22),
        ("Mr. John Doe", "B1 Bank", "1261234567", "09/01/2020", "Debit", "SMS Notification Fee", 2.80, 68.42),
        ("Mr. John Doe", "B1 Bank", "1261234567", "09/02/2020", "Credit", "Banking App Payment Received A Pieterse", 1600.00, 1668.42),
        ("Mr. John Doe", "B1 Bank", "1261234567", "09/02/2020", "Debit", "ATM Balance Enquiry Fee", 5.55, 1662.87),
        ("Mr. John Doe", "B1 Bank", "1261234567", "09/02/2020", "Debit", "ATM Cash Withdrawal Absa Magalies Centre (Card 1551)", 1350.00, 312.87),
        ("Mr. John Doe", "B1 Bank", "1261234567", "09/02/2020", "Debit", "Cash Withdrawal Fee (ATM)", 8.83, 304.04),
        ("Mr. John Doe", "B1 Bank", "1261234567", "09/02/2020", "Debit", "SMS Notification Fee", 1.20, 302.84),
        ("Mr. John Doe", "B1 Bank", "1261234567", "09/01/2020", "Debit", "Lulu's Liquors Brits (Card 1551)", 50.00, 252.84),
        ("Mr. John Doe", "B1 Bank", "1261234567", "09/04/2020", "Credit", "Banking App Payment Received J Bronn", 150.00, 402.84),
        ("Mr. John Doe", "B1 Bank", "1261234567", "09/04/2020", "Debit", "ATM Cash Withdrawal Absa Panorama Centre (Card 1551)", 140.00, 262.84),
        ("Mr. John Doe", "B1 Bank", "1261234567", "09/04/2020", "Debit", "Cash Withdrawal Fee (ATM)", 8.83, 254.01),
        ("Mr. John Doe", "B1 Bank", "1261234567", "09/04/2020", "Debit", "SMS Notification Fee", 0.40, 253.61),
        ("Mr. John Doe", "B1 Bank", "1261234567", "09/02/2020", "Debit", "Oklahoma Supermar Brits (Card 1551)", 230.00, 23.61),
        ("Mr. John Doe", "B1 Bank", "1261234567", "09/05/2020", "Credit", "Payment Received: Absa Bank Deon Transfer", 500.00, 523.61),
        ("Mr. John Doe", "B1 Bank", "1261234567", "09/05/2020", "Debit", "Banking App Prepaid Purchase MTN", 70.00, 453.61)
    ]

    BANK STATEMENTS:-

    '''

    summaryprompt = '''
    You are a brilliant bank statement summarizer. .Using the following example , summarize bank statements in the exact format as given below.
    1) DO NOT DEVIATE FROM THE FORMAT SHOWN BELOW
    2) DO NOT HALLUCINATE
    For example  :-
    BANK STATEMENT:-
    Savings Account Statement

    B1 Bank Limited
    1 Random Street
    Test City
    7600123

    Personal Details
    Mr. John Doe

    1 STUART PLACE
    NORTHCLIFF EXT1

    TEST CITY
    21950

    , Transaction
    Posting Date pote

    31/08/2020 19/08/2020
    31/08/2020 19/08/2020
    31/08/2020 31/08/2020
    31/08/2020 31/08/2020
    31/08/2020 31/08/2020
    31/08/2020 31/08/2020
    31/08/2020 31/08/2020

    31/08/2020 31/08/2020
    31/08/2020 31/08/2020
    31/08/2020 31/08/2020
    31/08/2020 31/08/2020
    01/09/2020 01/09/2020
    01/09/2020 01/09/2020

    01/09/2020 01/09/2020
    01/09/2020 01/09/2020
    01/09/2020 01/09/2020
    01/09/2020 01/09/2020

    01/09/2020 01/09/2020
    01/09/2020 01/09/2020
    01/09/2020 01/09/2020
    01/09/2020 01/09/2020
    01/09/2020 01/09/2020

    01/09/2020 01/09/2020
    01/09/2020 01/09/2020
    02/09/2020 02/09/2020
    02/09/2020 02/09/2020
    02/09/2020 02/09/2020

    02/09/2020 02/09/2020
    02/09/2020 02/09/2020
    03/09/2020 01/09/2020
    04/09/2020 04/09/2020
    04/09/2020 04/09/2020

    04/09/2020 04/09/2020
    04/09/2020 04/09/2020
    05/09/2020 02/09/2020
    05/09/2020 05/09/2020
    05/09/2020 05/09/2020

    B1 Bank is an

    B1 Bank

    30/09/2020
    Branch: 470010
    Device: 9003

    Description

    Correction: Cash Withdrawal Cpg.

    Correction: ATM Cash Withdrawal Fee
    Banking App Payment Received A Pieterse
    Banking App Payment Lung,

    Banking App Payment Fee

    ATM Balance Enquiry Fee

    ATM Cash Withdrawal Spar Panorama (Card
    1551)

    Cash Withdrawal Fee (ATM)

    Interest Received

    SMS Notification Fee

    Monthly Account Admin Fee

    Banking App Payment Received A Pieterse
    ATM Cash Withdrawal Spar Panorama (Card
    1551)

    Cash Withdrawal Fee (ATM)

    Banking App Payment Received A Pieterse
    Banking App Payment Received A Pieterse
    Purchase & Cash: Mode! Melkwinkel N16227
    Brits (Card 1551)

    Till Cash Withdrawal Fee

    Banking App Payment Received A Pieterse
    Banking App Payment Received A Pieterse
    ATM Balance Enquiry Fee

    ATM Cash Withdrawal Spar Panorama (Card
    1551)

    Cash Withdrawal Fee (ATM)

    SMS Notification Fee

    Banking App Payment Received A Pieterse
    ATM Balance Enquiry Fee

    ATM Cash Withdrawal Absa Magalies Centre
    (Card 1551)

    Cash Withdrawal Fee (ATM)

    SMS Notification Fee

    Lulu's Liquors Brits (Card 1551)

    Banking App Payment Received J Bronn
    ATM Cash Withdrawal Absa Panorama Centre
    (Card 1551)

    Cash Withdrawal Fee (ATM)

    SMS Notification Fee

    Oklahoma Supermar Brits (Card 1551)
    Payment Received: Absa Bank Deon Transfer
    1319444263

    Banking App Prepaid Purchase MTN



    Tax Invoice

    VAT Registration Number
    46812345678

    From Date: 08/12/2020



    07/01/2021
    07/01/2021

    Account Number 1261234567

    Money In (R)

    100.00
    6.56
    1 000.00

    1.49

    200.00

    200.00
    1000.00

    400.00
    100.00

    1600.00

    150.00

    500.00

    Money Out (R) Balance (R)
    132.27

    138.83

    1 138.83

    100.00 1 038.83
    1.60 1037.23
    5.55 1031.68
    1000.00 31.68
    8.83 22.85
    24.34

    0.80 23.54
    5.80 17.74
    217.74

    190.00 27.74
    8.83 18.91
    218.91

    1218.91

    1031.70 187.21
    161 185.60
    585.60

    685.60

    5.55 680.05
    600.00 80.05
    8.83 71.22
    2.80 68.42

    1 668.42

    5.55 1 662.87
    1350.00 312.87
    8.83 304.04
    1.20 302.84
    50.00 252.84
    402.84

    140.00 262.84
    8.83 254.01
    0.40 253.61
    230.00 23.61
    523.61

    70.00 453.61

    and registered credit provider (ABC1234). B1 Bank Limited Reg. No.: 1234/123456/

    aulnoazed foancialsecuces “ABC125)
    Unique Document No.: 2c05a1ce-6b84-47e9-9863-1fde19b1ea8e / 204 / V6.0 - 01/04/2020 (ddmmerxa.)

    Page 1 of 1

    SUMMARY:-
    Savings Account Statement Summary
    Account Holder: Mr. John Doe
    Address: 1 Stuart Place, Northcliff Ext1, Test City, 21950

    Bank: B1 Bank Limited
    Branch: 470010
    Device: 9003
    Statement Date: 30/09/2020
    Account Number: 1261234567

    Account Summary
    Previous Balance: R1,668.42
    Total Money In: R4,061.00
    Total Money Out: R3,793.00
    New Balance: R1,936.42
    Transactions
    Money In:

    31/08/2020: Correction: Cash Withdrawal Cpg. - R100.00
    31/08/2020: Correction: ATM Cash Withdrawal Fee - R6.56
    31/08/2020: Banking App Payment Received A Pieterse - R1,000.00
    31/08/2020: Banking App Payment Lung - R1.49
    31/08/2020: ATM Balance Enquiry Fee - R200.00
    31/08/2020: ATM Cash Withdrawal Spar Panorama (Card 1551) - R200.00
    31/08/2020: Interest Received - R1,600.00
    31/08/2020: SMS Notification Fee - R150.00
    01/09/2020: Monthly Account Admin Fee - R500.00
    01/09/2020: Banking App Payment Received A Pieterse - R1,600.00
    01/09/2020: Cash Withdrawal Fee (ATM) - R150.00
    02/09/2020: ATM Cash Withdrawal Spar Panorama (Card 1551) - R1,000.00
    02/09/2020: Banking App Payment Received A Pieterse - R400.00
    02/09/2020: Banking App Payment Received A Pieterse - R100.00
    02/09/2020: Purchase & Cash: Mode! Melkwinkel N16227 - R200.00
    03/09/2020: Banking App Payment Received A Pieterse - R1,600.00
    03/09/2020: ATM Cash Withdrawal Spar Panorama (Card 1551) - R1,000.00
    03/09/2020: Cash Withdrawal Fee (ATM) - R150.00
    04/09/2020: SMS Notification Fee - R1,000.00
    05/09/2020: ATM Cash Withdrawal Absa Magalies Centre (Card 1551) - R1,000.00
    Total Money In: R4,061.00

    Money Out:

    31/08/2020: Cash Withdrawal Fee (ATM) - R132.27
    31/08/2020: Banking App Payment Fee - R138.83
    31/08/2020: ATM Cash Withdrawal Spar Panorama (Card 1551) - R1,000.00
    01/09/2020: Cash Withdrawal Fee (ATM) - R1.60
    01/09/2020: ATM Balance Enquiry Fee - R5.55
    01/09/2020: Banking App Payment Received A Pieterse - R100.00
    01/09/2020: SMS Notification Fee - R8.83
    02/09/2020: Cash Withdrawal Fee (ATM) - R24.34
    02/09/2020: ATM Balance Enquiry Fee - R0.80
    02/09/2020: ATM Cash Withdrawal Spar Panorama (Card 1551) - R5.55
    02/09/2020: Banking App Payment Received A Pieterse - R100.00
    02/09/2020: SMS Notification Fee - R8.83
    02/09/2020: ATM Cash Withdrawal Absa Magalies Centre (Card 1551) - R0.40
    03/09/2020: Cash Withdrawal Fee (ATM) - R8.83
    03/09/2020: ATM Cash Withdrawal Absa Magalies Centre (Card 1551) - R230.00
    04/09/2020: Banking App Payment Received J Bronn - R70.00
    04/09/2020: ATM Cash Withdrawal Absa Panorama Centre (Card 1551) - R600.00
    05/09/2020: Cash Withdrawal Fee (ATM) - R1.20
    05/09/2020: Banking App Prepaid Purchase MTN - R50.00
    Total Money Out: R3,793.00

    Notes:

    VAT Registration Number: 46812345678
    Document Number: 2c05a1ce-6b84-47e9-9863-1fde19b1ea8e
    For inquiries, please contact B1 Bank Limited.

    BANK STATEMENT:-
    '''
    resumeSummary1 = model.generate_content(instruction1 + extracted_text1)
    summ1 = model.generate_content(summaryprompt + extracted_text1 )

    resumeSummary = model.generate_content(instruction1 + summ1.text )

    data_string = correct_json_format(resumeSummary.text)
    data_string = resumeSummary.text ## KEEP THIS
    # data_string = extracted_text1 ## OR THIS
    # print(data_string)
    #  # Debug: Print extracted text before processing
    # print("Debug: Extracted text before processing:\n", data_string)

    # # Clean the extracted text to avoid parsing issues
    # cleaned_text = data_string.strip().replace('\n', ' ').replace('\r', '')

    # try:
    #     # Validate the format before evaluating
    #     if not cleaned_text.startswith('[') or not cleaned_text.endswith(']'):
    #         raise ValueError("Extracted text is not a valid list of tuples.")

    #     # Attempt to evaluate the string as a literal Python expression
    #     data_tuples = ast.literal_eval(cleaned_text)
    # except (SyntaxError, ValueError) as e:
    #     # Log the error and print the problematic string for debugging
    #     print(f"Error: Failed to parse extracted text: {e}")
    #     print("Problematic string:\n", cleaned_text)
    #     data_tuples = []  # Use an empty list as fallback

    # # If parsing succeeded, create a DataFrame
    # if data_tuples:
    #     columns = ['client_name', 'bank_name', 'account_number', 'transaction_date',
    #                'credit_debit', 'description', 'amount', 'balance']
    #     df = pd.DataFrame(data_tuples, columns=columns)
    # else:
    #     # Return an empty DataFrame if parsing failed
    #     df = pd.DataFrame(columns=['client_name', 'bank_name', 'account_number',
    #                                'transaction_date', 'credit_debit', 'description',
    #                                'amount', 'balance'])
    # Clean data_string by stripping extra spaces and newlines
    # data_string = data_string.strip()

    # # Replace problematic characters (if any)
    # data_string = data_string.replace('\n', ' ').replace('\r', '')

    # # Debug print to inspect cleaned string
    # print("Cleaned data_string:\n", data_string)

    # Evaluate the string
####################WORKING VERSION 0.1##########################################333
    # print(f"DATA GIVEN BY API CALL: {data_string}")

    # data_tuples = ast.literal_eval(data_string)

    # # Convert the string to a list of tuples using ast.literal_eval
    # # data_tuples = ast.literal_eval(data_string)

    # # Define the columns for the DataFrame
    # columns = ['client_name', 'bank_name', 'account_number', 'transaction_date', 'credit_debit', 'description', 'amount', 'balance']

    # # Create a DataFrame
    # df = pd.DataFrame(data_tuples, columns=columns)
#############################################################################################
    import ast
    import pandas as pd
    import re
    cleaned_string = re.sub(r'R([\d,]+\.\d+)', lambda x: x.group(1).replace(',', ''), data_string)

    # Step 2: Convert the cleaned string to a list of tuples using ast.literal_eval
    data_tuples = ast.literal_eval(cleaned_string)

    # Step 3: Define columns for the DataFrame
    columns = ['client_name', 'bank_name', 'account_number', 'transaction_date', 
            'credit_debit', 'description', 'amount', 'balance']

    # Step 4: Create a DataFrame
    df = pd.DataFrame(data_tuples, columns=columns)



    #print(ressume)
    print("\n----------------------------------------------\n")
    print(df)
    print("\n----------------------------------------------\n")


    return df