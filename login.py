import streamlit as st
import streamlit_authenticator as stauth
from app import *
import database as db
# import mysql.connector as c
# con=c.connect(
#     host='localhost',
#     user='root',
#     passwd='Kariman2#',
#     database='streamlit'

# )
# cursor=con.cursor()

#fetching users from database
users=db.fetch_users()
usernames=[user['key'] for user in users]
names=[user['name'] for user in users]
hashed_passwords=[user['password'] for user in users ]

authenticator = stauth.Authenticate(names,usernames,hashed_passwords,
    'some_cookie_name','some_signature_key',cookie_expiry_days=30)
name, authentication_status, username = authenticator.login('Login','main')

#Authentication
if authentication_status:
    authenticator.logout('Logout', 'sidebar')
    st.write('Welcome *%s*' % (name))
    # st.title('Some content')
    ##Application
    query = st.sidebar.selectbox('Select query', ("1:1 session", "Add New Customer"))
    if query=='1:1 session':
        c=submit_data(query)
        if st.button('Submit'):
            st.success('Data Uploaded !!')
            st.write(c)
            data_frame=pd.DataFrame(pd.DataFrame(c,index=[0]))
            st.write(data_frame.shape)
            # a = len(data_frame.values[0])
            # tup = tuple(data_frame.values[0][i] for i in range(a))
            # cols = "`,`".join([str(i) for i in data_frame.columns.tolist()])
            # sql = "INSERT INTO new_session_form  (`" + cols + "`) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            # cursor.execute(sql,tup)
            # con.commit()
            st.write(data_frame.values)
    elif query=='Add New Customer':
        email = st.text_input('Email address of customer')
        if st.button('add'):
            email_id=email
            st.write(email_id)

#if usermame/password isn't correct
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')