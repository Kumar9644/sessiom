import streamlit_authenticator as stauth

import database as db

names = ['John Smith','Rebecca Briggs','Kumar Hemjeet','kedar kanhere','Mohammad Hassan']
usernames = ['jsmith','rbriggs','kumar','kedar','hassan']
passwords = ['123','456','1135','abc123','md1234']
hashed_passwords = stauth.Hasher(passwords).generate()


for (username, name, hash_password) in zip(usernames, names, hashed_passwords):
    db.insert_user(username, name, hash_password)