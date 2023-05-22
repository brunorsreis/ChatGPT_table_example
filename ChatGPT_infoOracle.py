#!/usr/bin/env python
# coding: utf-8

# In[32]:


import cx_Oracle


# Function to check if the text was created by ChatGPT

def is_text_from_chatgpt(text):
    # Create a DSN to connect to the Pluggable Database (PDB)
    dsn = cx_Oracle.makedsn(
        host='localhost',
        port=1521,
        sid='XE',
        service_name='XEPDB1'
    )
    
    # Establish connection to Oracle database
    #If the connection is made via `sys`, it is necessary to use the `cx_Oracle.SYSDBA` clause after the `dsn` parameter.
    conn = cx_Oracle.connect('brunotechdatabasket', 'YDq9QEh)Fsrw45vE',dsn)

    # Create a cursor to execute SQL queries
    cursor = conn.cursor()
    
    # Test the function
    text_to_check = "Mount Everest is approximately 8,848 meters (29,029 feet) tall."

    # Prepare the SQL query
    query = "SELECT COUNT(*) FROM brunotechdatabasket.chatgpt_information WHERE response =:text"
    
    # Execute the query
    cursor.execute(query, text=text)  # Bind the variable text
    
    # Fetch the result
    result = cursor.fetchone()
    
    # Close the cursor and connection
    cursor.close()
    conn.close()
    
    # Check if the text exists in the database
    if result[0] > 0:
        return True
    else:
        return False



if is_text_from_chatgpt(text_to_check):
    print("The text was created by ChatGPT.")
else:
    print("The text was not created by ChatGPT.")


# In[ ]:





# In[ ]:




