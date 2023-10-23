import streamlit as st
import pandas as pd
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from streamlit_modal import Modal
import json
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode, JsCode
from common import set_custom_css
import streamlit.components.v1 as components

pep_data = ["PEP", "AML", "Sanctions"]
aml_data = ["Pass", "Pass", "Fail"]

def admin_dash():
   
    set_custom_css()
    # st.set_page_config(layout="wide")
    st.session_state.modal_row = None
    GDRIVE_CREDS = {
        "type": "service_account",
        "project_id": "st-project-387317",
        "private_key_id": "e5778cc6315dac8480eb841efa093147fa47d996",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCwK8/wpxa4JRWx\n7KfObiLoebmjLrAjYpv8E+3yTHqp3X+p/xBgQYrics//LCX8sXsFG77dW4vLib0V\nw2U4uygIvi2juzQKGUpDlb9aZ2jKexuToX+UZoa+RUxZICX+J0oDylK3vqcfsPAD\nhivGzveZSmW9cuuop1PMT/nl9vjEzUjcP3YrCcoMdRCUyVj21u3Vy6Qy0zkZU+iv\nZUfQo4kqDQuQU3qSrgvHrzx/zxhLcHvYXKXcaz31Llbd9kyKo35zaq8XnNOAczpn\ncVmeFbxkcrYfu8JtyIv97lOgTHsuxIDauJ8of5I+3Ng+wMW8uo7z8KawBM8a/YFA\nQzVBP0YLAgMBAAECggEAO4oDE90Uk5WM+H331I9qYtFIyPqtcrgP6ai+oUXxqtj+\nHXDjkvRzwMZ2v1GnYPiGkBppbhxTaa2aZvGLkxnFlPbZK93H36XecGr6qc4LH2tt\nzX4mRPxFi6aWAAUacgPLQu6s+AaKKu68nyRIRT+LdJYtPlLJjE1Ix+M7nNnUB4ad\nsJgG0KiMJib4q721VoEpQCfzgNsKN2TX0pJovokNv8slULMKouul94bSfRn7WeEo\nSyVceewz2JNMmym529bcnrdkSWujLEzXrA5V8GFaNgUcc+oSDlm7maPu9uSMFTv/\nceXgCKikYqik5XOFXjy4xpOnTII9cMUi8nkEWox+AQKBgQDkGBQ0AO1WOWylNCmH\n0Wk53m8701JSOsigG3ZXz7sQYa9rL57bkAk+T4oKL4AS2F14ARo672G2jlga8MY+\nGwBII8eStqtvBgpbfFR458rQT9QmeN59xExHxlDQHq6x9BV27cBb4fr6i9+YnGG0\nGwL3FWx09BSlPgGKIHK8xITJCwKBgQDFuYEPmf08fNq7fWZHqQvU++ma7iuUSCNW\n0v3YAnWO3EIm0rvFjpXzp7t8crkkcywj6TmFtttMm7mXT5nY53C4nDiLl72d8hfr\nFCTXY1NLgucj9AsM1OZnqV0g0FgXUXPFyr4acjYT990Qf9HF/KHLZztkLuxci5jb\np7zht4+XAQKBgQCOBiw2QUmGwdTTfQpLBmqV3Nm4D5oXl4CqqM7kWHVq+thGTm2E\n20fWI6KZOwBtO4nfmhgiEEHwcOuNQtS9gQSI5rZytQlD5Sf31Q+oBPQ1By/bELHA\n78RrgKF7JU+zgH8JAXsf+zLSZNvB48W2ZodPIGja3cwpI9XDkva+cUMZBwKBgDPB\nqjHuSiaCPDNl0NcjPfCjfHPMsmWfOHjqw/2+Lw2VRE+rS/GbsE7WcjJSSXpsF3rS\n+vawddkozjz4Xjoz4wLACeEoeD8W9wHXBQnIey5B9sUnhZj3RdSOtcz4HIcGEDsP\nJhIAIX26nQhLnRqpVaTLwfUof0B+XiXpU3z2MsUBAoGBAME1VwH07HSFjsjRKK+C\n/GphuvXBpBED1hGX7YIE4mF3HCVM8WilvW+2c5cxOnIPEL/M5W69h8Wl5okojpNQ\ngQiXCEd4PAnRNUeAw7fGq9jnl0ax/wmLIXnDl3czojhpKmrKg5cNhRQw0OYjEZrG\nmAO3VDeMT0xk9E1SoTMqTiEO\n-----END PRIVATE KEY-----\n",
        "client_email": "collection-app@st-project-387317.iam.gserviceaccount.com",
        "client_id": "116665121729126589127",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/collection-app%40st-project-387317.iam.gserviceaccount.com",
        "universe_domain": "googleapis.com"
        }

    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_dict(GDRIVE_CREDS, scope)
    client = gspread.authorize(creds)
    sheet = client.open("streamlit_data").worksheet('flow_data')

    data = sheet.get_all_records()
    df = pd.DataFrame(data)
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    copy_df = df
    new_df = pd.DataFrame()

    # Parsing data for specific columns
    # Parse the JSON data in the "Social_Check" column
    copy_df["Social_Check"] = copy_df["Social_Check"].apply(lambda x: json.loads(x) if x else None)
    # Extract Twitter and Google values
    copy_df["Social_Checks_Twitter"] = copy_df["Social_Check"].apply(lambda x: x.get("Twitter") if x else None)
    copy_df["Social_Checks_Google"] = copy_df["Social_Check"].apply(lambda x: x.get("Google") if x else None)
    copy_df["CR_DATA"] = copy_df["CR_DATA"].apply(lambda x: json.loads(x) if x else {})
    copy_df["VAT_Data"] = copy_df["VAT_Data"].apply(lambda x: json.loads(x) if x else {})
    # copy_df["ID_Data_info"] = copy_df["ID_Data"].apply(lambda x: json.loads(x) if x else {})
    copy_df["Sentiments"] = copy_df["Sentiments"].apply(lambda x: json.loads(x) if x else {})
    copy_df["BUSINESS_GOSI_Data"] = copy_df["BUSINESS_GOSI_Data"].apply(lambda x: json.loads(x) if x else {})
    copy_df["Address"] = copy_df["Address"].apply(lambda x: json.loads(x) if x else {})
    copy_df["Address1"] = copy_df["Address"].apply(lambda x: x.get("user_address") if x else None)
    copy_df["Address2"] = copy_df["Address"].apply(lambda x: x.get("google_address") if x else None)
    copy_df["VAT_Data_reg_number"] = copy_df["VAT_Data"].apply(lambda x: x.get("vat_reg_number") if x else None)
    copy_df["VAT_Data_reg_date"] = copy_df["VAT_Data"].apply(lambda x: x.get("vat_reg_date") if x else None)
    copy_df["BUSINESS_GOSI_issue_date"] = copy_df["BUSINESS_GOSI_Data"].apply(lambda x: x.get("gosi_issue_date") if x else None)
    copy_df["BUSINESS_GOSI_number"] = copy_df["BUSINESS_GOSI_Data"].apply(lambda x: x.get("gosi_expiry_date") if x else None)
    copy_df["BUSINESS_owner_name"] = copy_df["CR_DATA"].apply(lambda x: x.get("business_owner_1") if x else None)
    copy_df["BUSINESS_location"] = copy_df["CR_DATA"].apply(lambda x: x.get("location") if x else None)

    new_df["Business_Name"] = copy_df["CR_DATA"].apply(lambda x: x.get("business_name") if x else None)
    new_df["CR_Number"] = copy_df["CR_DATA"].apply(lambda x: x.get("cr_number") if x else None)
    new_df["CR_Expiry_Date"] = copy_df["CR_DATA"].apply(lambda x: x.get("expiry_date_hijri") if x else None)
    new_df["Owner_Name"] = copy_df["CR_DATA"].apply(lambda x: x.get("business_owner_1") if x else None)
    new_df["VAT_Reg_Number"] = copy_df["VAT_Data"].apply(lambda x: x.get("vat_reg_number") if x else None)
    new_df["Average_Sentiment"] = copy_df["Sentiments"].apply(lambda x: f"{round(x.get('Average'),2)*100}%" if x else None)
    new_df['Company_Name'] = copy_df['Company_Name']
    new_df['Company_Url'] = copy_df['Company_Url']
    new_df['Timestamp'] = copy_df['Timestamp']
    

    print(f"\n\nCols: {new_df.columns}\n\n")
    print(f"\n\nnew_df: {new_df}\n\n")
    st.sidebar.header("Filter")
    # set_custom_css()
   # Sentiment filter
    custom_css ="""
    <style>
    .st-emotion-cache-10oheav h2{
     align:center;
     text-align:center
     color:blue;
    }  
    </style>
"""
       
    st.markdown(custom_css, unsafe_allow_html=True)
    sentiment_filter_options = ['All', 'High', 'Low']
    sentiment_filter = st.sidebar.selectbox("Sentiment", sentiment_filter_options)

    # Company Name filter
    company_name_filter_options = ['All'] + list(new_df["Company_Name"].unique())
    company_name_filter = st.sidebar.selectbox("Company Name", company_name_filter_options)

    # Date Range filter
    date_range_filter_options = ['All'] + [date.strftime('%Y-%m-%d') for date in new_df["Timestamp"].unique()]
    date_range_filter = st.sidebar.selectbox("Date Range", date_range_filter_options)

   # Calculate the unique sentiment values and their percentages
    unique_sentiments = new_df['Average_Sentiment'].unique()
    sentiment_percentages = [f"{int(sentiment)}-{int(sentiment) + 25}%" for sentiment in range(0, 100, 25)]
    sentiment_percentages.append("100%")

    # Clear All button
    if st.sidebar.button("Clear All"):
        date_range_filter = "Select Date"
        company_name_filter  = "All"
        sentiment_filter = "All"
    
# Filter the data based on the selected filters
    filtered_df = new_df

    if sentiment_filter != 'All':
        filtered_df = filtered_df[
        (filtered_df['Average_Sentiment'].str.rstrip('%').astype(float) > 50) if sentiment_filter == 'High' 
        else (filtered_df['Average_Sentiment'].str.rstrip('%').astype(float) <= 50)
    ]

    if company_name_filter != 'All':
        filtered_df = filtered_df[filtered_df['Company_Name'] == company_name_filter]

    if date_range_filter != 'All':
        selected_date = datetime.strptime(date_range_filter, '%Y-%m-%d')
        filtered_df = filtered_df[filtered_df['Timestamp'] == selected_date]

    logo_url='https://objectstorage.me-jeddah-1.oraclecloud.com/n/idcsprod/b/me-jeddah-idcs-1-9E6C09D36371AB1B7C12FA52FA120B95980D070A43765EF7F2A2F0B0F82948E6/o/images/202109131530/1631547034999/Alraedah-Logo-Landscape-2.jpg'
    # Create a custom layout using HTML and CSS
    custom_layout = f"""
        <div style="display: flex; align-items: center;">
            <img src="{logo_url}" alt="Logo" style="width: 200px; height: 60px; margin-right: 50px;">
            <h1 class="title">Dashboard View</h1>
        </div>
    """

    # Display the custom layout with the logo and title
    st.markdown(custom_layout, unsafe_allow_html=True)
    render_image = JsCode('''
        function renderImage(params) {
            const container = document.createElement("div");
            const textNode = document.createTextNode(params.value); // Assuming 'params.value' is the text to be displayed
            container.appendChild(textNode);
            return container.outerHTML;
        }
    ''')
    if filtered_df.empty:
        st.warning('No data to display with the current filters.')
    else:
        options_builder = GridOptionsBuilder.from_dataframe(filtered_df)
        options_builder.configure_column('Timestamp', cellRenderer = render_image)
        options_builder.configure_selection(selection_mode="single", use_checkbox=True)
        options_builder.configure_default_column(width=150, resizable=True)
        options_builder.configure_grid_options(domLayout='autoHeight', autoSizeColumns=True)
        grid_options = options_builder.build()

        # Create AgGrid component
        grid = AgGrid(filtered_df, 
                        gridOptions = grid_options,
                        allow_unsafe_jscode=True,
                        height=200, width=500, theme='streamlit')
        
        sel_row = grid["selected_rows"]
        if sel_row:
            modal = Modal(key="Details_Modal",title="Comprehensive Details")
            open_modal = st.button("View Details")
            if open_modal:
                modal.open()

            if modal.is_open():
                with modal.container():
                     # Apply CSS to make the modal container scrollable
                    col1, col2 = st.columns([1, 1])
                
                    tab1, tab2, tab3  = st.tabs(["Overview", "Documents", "PEP & AML"])

                    with col1:
                        selected_index = sel_row[0]['_selectedRowNodeInfo']['nodeRowIndex']
                        gosi_issue_date=copy_df.loc[selected_index,'BUSINESS_GOSI_issue_date']
                        vat_reg_number=copy_df.loc[selected_index,'VAT_Data_reg_number']
                        company_url=copy_df.loc[selected_index,'Company_Url']
                        st.write(f"<b>Business Name: </b>{sel_row[0]['Business_Name']}",unsafe_allow_html=True)
                        st.write(f"<b>CR Number: </b>{sel_row[0]['CR_Number']}",unsafe_allow_html=True)
                        st.write(f"<b>Vat Registration Number : </b>{vat_reg_number}",unsafe_allow_html=True)
                        st.write(f"<b>Gosi Issue Date : </b>{gosi_issue_date}",unsafe_allow_html=True)
                        # st.write(f"<b> GOSI Issue Date: </b>{gosi_issue_date}",unsafe_allow_html=True)
                        # st.write(f"<b> GOSI Issue Date: </b>{sel_row[0]['']}",unsafe_allow_html=True) 


                        cr_wathq_resp = copy_df.loc[selected_index, 'CR_DATA_WATHQ']
                        cr_pdf = copy_df.loc[selected_index, 'CR_PDF']
                        # gosi_business_expander= copy_df.loc[selected_index, 'BUSINESS_GOSI_Data']
                        
                        gosi_business_pdf = copy_df.loc[selected_index, 'BUSINESS_GOSI_PDF']
                        vat_resp = copy_df.loc[selected_index, 'VAT_Data']
                        vat_pdf = copy_df.loc[selected_index, 'VAT_PDF']
                        business_gosi_data=copy_df.loc[selected_index,'BUSINESS_GOSI_Data']
                        # id_data=copy_df.loc[selected_index,'ID_Data']
                        expense_data=json.loads(df.loc[selected_index,'Expense_Data'])
                        customer_gosi_pdf=copy_df.loc[selected_index,'BUSINESS_GOSI_PDF']
                        bank_statement_pdf=copy_df.loc[selected_index,'BANK_STATEMENT']

                # button_id = "show_pdf_button"
                # pdf_container_id = "pdf_container"

                    with col2:
                            vat_reg_date=copy_df.loc[selected_index,'VAT_Data_reg_date']
                            cr_location=copy_df.loc[selected_index,'BUSINESS_location']
                            gosi_expiry_date=copy_df.loc[selected_index,'BUSINESS_GOSI_number']
                            business_owner_name=copy_df.loc[selected_index,'BUSINESS_owner_name']
                            # Display the "CR File.pdf" text
                            st.write(f"<b>Business Owner: </b>{business_owner_name}",unsafe_allow_html=True)
                            st.write(f"<b>Business Location : </b>{cr_location}",unsafe_allow_html=True) 
                            st.write(f"<b>Vat Registration Date: </b>{vat_reg_date}",unsafe_allow_html=True) 
                            st.write(f"<b>Gosi Expiry Date: </b>{gosi_expiry_date}",unsafe_allow_html=True)
                            
                            
                        
                    
                            data=json.loads(copy_df.loc[selected_index, 'Expense_Data'])
                                
                            df = pd.DataFrame(data)



                    with tab1:
                            col1,col2=st.columns([1,1])
                            with col1:
                                socialcheck_twitter=copy_df.loc[selected_index,'Social_Checks_Twitter']
                                socialcheck_google=copy_df.loc[selected_index,'Social_Checks_Google']
                                average_sentiment=filtered_df.loc[selected_index,'Average_Sentiment']
                                st.write(f"<b>Business Name: </b>{sel_row[0]['Business_Name']}",unsafe_allow_html=True)
                                st.write(f"<b>Business URL: </b>{sel_row[0]['Company_Url']}",unsafe_allow_html=True)
                                user_entered_address = copy_df.loc[selected_index, 'Address1']
                                google_address = copy_df.loc[selected_index, 'Address2']
                                st.write(f"<b>User Entered Address : </b>{user_entered_address}",unsafe_allow_html=True)
                                st.write(f"<b>Google Fetched Address : </b>{google_address}",unsafe_allow_html=True)
                                st.write(f"<b>Average Sentiment : </b>{average_sentiment}",unsafe_allow_html=True)
                                st.write(f"<b>Social Check Twitter : </b>{socialcheck_twitter}✅",unsafe_allow_html=True)
                                st.write(f"<b>Social Check Google : </b>{socialcheck_google}✅",unsafe_allow_html=True)
                                
                            with col2:
                                with st.expander("CR Wathq Response"):
                                    st.json(f"{cr_wathq_resp}")
                                    
                                with st.expander("ZAKAT/VAT Data"):
                                    st.json(f"{vat_resp}")
                                with st.expander("Business Gosi Data"):
                                    st.json(f"{business_gosi_data}")
                                with st.expander("Id Data"):
                                    id_data=json.loads(copy_df.loc[selected_index,'ID_Data'])
                                    data= id_data
                                    print(id_data)
                                    df=pd.DataFrame(data, index=[0])
                                    st.table(df)
                                with st.expander("Expense Data"):
                                    data=json.loads(copy_df.loc[selected_index, 'Expense_Data'])
                                    df=pd.DataFrame(data)
                                    st.table(df)
                    with tab2:
                            col1, col2, col3,  = st.columns([1, 1, 1])
                            col4, col5, col6 =st.columns([1,1,1])
                            with col1:
                                # Center-align the text "CR File"
                                st.markdown('<div style="text-align: left; margin-bottom: 20px;"><b>CR File</b></div>', unsafe_allow_html=True)
                                st.markdown(f'<iframe src="https://drive.google.com/viewerng/viewer?embedded=true&url={cr_pdf}"  height="300" frameborder="0"></iframe>', unsafe_allow_html=True)
                            #    st.write(f"<b>CR File: </b>{cr_pdf}",unsafe_allow_html=True)
                            with col2:
                                # Center-align the text "ZAKAT/VAT File"
                                # Center-align the text "CUSTOMER GOSI FILE" with some vertical spacing
                                st.markdown('<div style="text-align: left; margin-bottom: 20px;"><b>VAT/ZAKAT FILE</b></div>', unsafe_allow_html=True)
                                st.markdown(f'<iframe src="https://drive.google.com/viewerng/viewer?embedded=true&url={vat_pdf}"   height="300" frameborder="0"></iframe>', unsafe_allow_html=True)
                                # st.write(f"<b>CR File: </b>{cr_pdf}",unsafe_allow_html=True)
                            
                            # st.write(f"<b>ZAKAT/VAT File: </b>{cr_pdf}",unsafe_allow_html=True)
                            with col3:
                                # Center-align the text "ZAKAT/VAT File"
                                st.markdown('<div style="font-weight:bold; font-size:15px; text-align: left; margin-bottom: 20px;"><b>BUSINESS GOSI FILE</b></div>', unsafe_allow_html=True)
                                st.markdown(f'<iframe src="https://drive.google.com/viewerng/viewer?embedded=true&url={gosi_business_pdf} height="300" frameborder="0"></iframe>', unsafe_allow_html=True)
                                
                            with col4:
                                # Center-align the text "ZAKAT/VAT File"
                                st.markdown('<div style="text-align: left; margin-top: 20px;"><b>CUSTOMER GOSI FILE</b></div>', unsafe_allow_html=True)
                                st.markdown(f'<iframe src="https://drive.google.com/viewerng/viewer?embedded=true&url={customer_gosi_pdf} height="300" frameborder="0"></iframe>', unsafe_allow_html=True)
                            with col5:
                                # Center-align the text "ZAKAT/VAT File"
                                st.markdown('<div style="text-align: left; margin-top: 20px;"><b>BANK STATEMENT FILE</b></div>', unsafe_allow_html=True)
                                st.markdown(f'<iframe src="https://drive.google.com/viewerng/viewer?embedded=true&url={bank_statement_pdf}height="300"  frameborder="0"></iframe>', unsafe_allow_html=True)
                                
                            with col6:
                                image_links = copy_df.loc[selected_index, 'ID_Image'].split(',')  # Split the comma-separated links
                                image_width=300
                                image_height=400
                                print('This is image links',image_links)
                                for link in image_links:
                                    st.image(link, use_column_width='always', output_format='JPEG') 
                                    st.markdown(
                                    f'<style>.stImage > img {{max-height: 200px;max-width:200px;margin-top:20px}}</style>', 
                                    unsafe_allow_html=True
                                    )
                                print('this is the link',link)

                    with tab3:
                            # Title for tab3
                            st.write("<h2>PEP & AML</h2>", unsafe_allow_html=True)

                            # Create a column layout
                            col1, col2, col3 = st.columns(3)

                            # Display PEP data and status
                            col1.write("PEP List")
                            col1.write("AML List")
                            col1.write("Sanctions List")

                            col2.write("<b>Pass</b>✅",unsafe_allow_html=True)
                            col2.write("<b>Pass</b>✅",unsafe_allow_html=True)
                            col2.write("<b>Pass</b>✅",unsafe_allow_html=True)
                            print('this is modal container',modal.container)
                    html_string = '''
                        <style>
                        div[data-modal-container='true'][key='Details_Modal'] > div:first-child div:first-child {
                                overflow: auto;
                            }
                        </style>
                        
                    <script language="javascript">
                    </script>
                        '''
                    components.html(html_string)



    # Add filters
    col1, col2, col3 = st.columns([1, 1, 1])
    