import pandas as pd
import streamlit as st
import pandas as pd
import json
import datetime


#query

#function to for uploading data
def submit_data(query):
    # query = st.sidebar.selectbox('Select query', ("1:1 session", "Add New Customer"))
    st.image('logo.jpg',width=600)
    # query = st.sidebar.selectbox('Select query', ("1:1 session", "Add New Customer"))
    data=dict()
    if query == "1:1 session":
        st.title("1:1 session form")

        #customer email
        cust_email = st.selectbox("Enter customer email address",['hemu@gmail.com','abhay@ecom.com','hemjeet.kumar@gmail.com'],)
        data['Email']=cust_email

        #domain of query
        query_domain=st.selectbox("Domain of Query:",("Big Data","Data Science","Career Guidance","Consulting"))
        data['Domain_query']=query_domain

        #if existing query or not
        existing_query=st.radio("Existing Project Query:",("Yes","No"))
        data['Existing_Query']=existing_query

        if existing_query=="Yes":

            #project name
            project_name=st.text_input("Project Name")
            data['Project_Name']=project_name

            #project ID
            project_id=st.number_input("Project ID",step=1)
            data['Project_ID']=project_id

        else:
            data['Project_ID']='NA'
            data['Project_Name']='NA'

        #session topic
        topic = st.text_input("Session Topic")
        data['Session_Topic']=topic

        col1, col2 = st.columns(2)
        with col1:
            #session date
            session_date = st.date_input("Session Date")
            data['Date_of_Session']=session_date
        with col2:

            #session time
            session_time = st.time_input("Time of session",datetime.time(1,10))
            st.write(session_time)
            data['Time_of_Session']=str(session_time)

        #name of expert
        name = st.text_input("Name of Expert")
        data['Name_of_Expert']=name

        #expert email
        exp_email=st.text_input('Expert Email:')
        data['Expert_Email']=exp_email

        #query resolved or not
        query_res = st.radio("Query Resolved:", ("Yes", "No"))
        data['Query_Resolved']=query_res

        #another session required
        another_session = st.radio("Need another session over same topic:", ("Yes", "No"))
        data['Need_Another_Session']=another_session

        #expert remarks
        remarks = st.text_area('Expert Remarks:')
        data['Expert_Remark']=remarks

        #customer feedback
        cust_feed = st.text_area("Customer feedback:")
        data['Customer_feedback']=cust_feed

        #session completed or not
        session_rs = st.selectbox("Session Completed:", ("Yes", "No"))
        data['Session_Completed']=session_rs
        if session_rs == "No":

            #reason for non-completion of session
            session_update = st.selectbox("Reason for non-completion of session:", ("Rescheduled", "Cancelled","Customer Noshow",
                                                                                    "Expert Noshow","Technical Issue"))
            data['session_status']=session_update
            if session_update == "Cancelled":

                #reason for cancellation
                reason = st.text_area("Reason for cancellation:")
                data['Reason_for_Cancellation']=reason
                data['Rescheduled_Date'] = 'NA'
                data['Rescheduled_Time'] = 'NA'

            elif session_update == "Rescheduled":
                data['Reason_for_Cancellation'] = 'NA'
                col3, col4 = st.columns(2)
                with col3:
                    #session rescedule date
                    reschedule_date = st.date_input("Rescheduled Date")
                    data['Rescheduled_Date']=reschedule_date
                with col4:

                    #session reschedule time
                    reschedule_time = st.time_input("Rescheduled time",datetime.time(1,10))
                    data['Rescheduled_Time']=str(reschedule_time)
            elif session_update=='Customer Noshow':

                data['Reason_for_Cancellation']='NA'
                data['Rescheduled_Date'] = 'NA'
                data['Rescheduled_Time'] = 'NA'

            elif session_update=='Expert Noshow':

                data['Reason_for_Cancellation']='NA'
                data['Rescheduled_Date'] = 'NA'
                data['Rescheduled_Time'] = 'NA'

            else:


                data['Reason_for_Cancellation']='NA'
                data['Rescheduled_Date'] = 'NA'
                data['Rescheduled_Time'] = 'NA'


        else:

            data['session_status']='NA'
            data['Reason_for_Cancellation']='NA'
            data['Rescheduled_Date']='NA'
            data['Rescheduled_Time']='NA'

    elif query=='Add New Customer':
        email=st.text_input('Email address of customer')
        if st.button('add'):
            email_id=email
            st.write(email_id)
    # return json.dumps(data,default=str)
    return data

# if __name__ == '__main__':
#     submit_data()
#
#     if st.button('Submit'):
#         st.write(c)
#         st.dataframe(pd.DataFrame(c,index=[0]))

    # st.dataframe(pd.DataFrame.from_dict(c,orient='index'))
    # st.json(c)
    # st.write(json.dumps(c,default=str))

