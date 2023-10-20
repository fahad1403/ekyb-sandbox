import streamlit as st
import pandas as pd
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from streamlit_modal import Modal
import json
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode, JsCode

def admin_dash():
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
    copy_df["CR_DATA"] = copy_df["CR_DATA"].apply(lambda x: json.loads(x) if x else {})
    copy_df["VAT_Data"] = copy_df["VAT_Data"].apply(lambda x: json.loads(x) if x else {})
    copy_df["ID_Data"] = copy_df["ID_Data"].apply(lambda x: json.loads(x) if x else {})
    copy_df["Sentiments"] = copy_df["Sentiments"].apply(lambda x: json.loads(x) if x else {})

    new_df["Business_Name"] = copy_df["CR_DATA"].apply(lambda x: x.get("business_name") if x else None)
    new_df["CR_Number"] = copy_df["CR_DATA"].apply(lambda x: x.get("cr_number") if x else None)
    new_df["CR_Expiry_Date"] = copy_df["CR_DATA"].apply(lambda x: x.get("expiry_date_hijri") if x else None)
    new_df["Owner_Name"] = copy_df["CR_DATA"].apply(lambda x: x.get("business_owner_1") if x else None)
    new_df["VAT_Reg_Number"] = copy_df["VAT_Data"].apply(lambda x: x.get("vat_reg_number") if x else None)
    new_df["VAT_Due_Date"] = copy_df["VAT_Data"].apply(lambda x: x.get("vat_exp_date") if x else None)
    new_df["Average_Sentiment"] = copy_df["Sentiments"].apply(lambda x: f"{round(x.get('Average'),2)*100}%" if x else None)
    new_df['Company_Name'] = copy_df['Company_Url']
    new_df['Timestamp'] = copy_df['Timestamp']

    print(f"\n\nCols: {new_df.columns}\n\n")
    print(f"\n\nnew_df: {new_df}\n\n")

    # Add a title and subtitle
    st.title("Dashboard")

    # Add filters
    col1, col2, col3 = st.columns([1, 1, 1])
    # col1, col2 = st.columns([1, 1])

    with col1:
        sentiment_filter_options = ['All', 'High', 'Low']
        sentiment_filter = st.selectbox("Sentiment", sentiment_filter_options)

    with col2:
        risk_label_filter_options = ['All'] + list(new_df["Company_Name"].unique())
        risk_label_filter = st.selectbox("Company Name", risk_label_filter_options)

    with col3:
        date_range_filter_options = ['All'] + [date.strftime('%Y-%m-%d') for date in new_df["Timestamp"].unique()]
        date_range_filter = st.selectbox("Date Range", date_range_filter_options)

    # Filter the data based on the selected filters
    filtered_df = new_df
    if sentiment_filter != 'All':
        filtered_df = filtered_df[
        (filtered_df['Average_Sentiment'].str.rstrip('%').astype(float) > 50) if sentiment_filter == 'High' 
        else (filtered_df['Average_Sentiment'].str.rstrip('%').astype(float) <= 50)
    ]
    if risk_label_filter != 'All':
        filtered_df = filtered_df[filtered_df['Company_Name'] == risk_label_filter]
    if date_range_filter != 'All':
        selected_date = datetime.strptime(date_range_filter, '%Y-%m-%d')
        filtered_df = filtered_df[filtered_df['Timestamp'] == selected_date]


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
            # with st.expander("Flow Details", expanded=True):
            col1 = st.columns(1)
            st.info(f"Busines Name: {sel_row[0]['Business_Name']}")
            st.write(f"CR Number: {sel_row[0]['CR_Number']}")              

            selected_index = sel_row[0]['_selectedRowNodeInfo']['nodeRowIndex']

            cr_wathq_resp = copy_df.loc[selected_index, 'CR_DATA_WATHQ']
            cr_pdf = copy_df.loc[selected_index, 'CR_PDF']

            vat_resp = copy_df.loc[selected_index, 'VAT_Data']
            vat_pdf = copy_df.loc[selected_index, 'VAT_PDF']

            st.write(f"CR File: {cr_pdf}")
            with st.expander("CR Wathq Response"):
                st.json(f"{cr_wathq_resp}")
            st.write(f"ZAKAT/VAT File: {cr_pdf}")
            with st.expander("ZAKAT/VAT Data"):
                st.json(f"{vat_resp}")

            image_links = copy_df.loc[selected_index, 'ID_Image'].split(',')  # Split the comma-separated links
            for link in image_links:
                st.image(link, use_column_width='always', output_format='JPEG', width=300) 
                st.markdown(
                f'<style>.stImage > img {{max-height: 300px;}}</style>', 
                unsafe_allow_html=True
                )
    

# if st.session_state.modal_row is not None:
#     selected_row = st.session_state.modal_row
#     modal_expander = st.expander("Data Details", expanded=True)
#     with modal_expander:
#         st.table(filtered_df.iloc[selected_row])

# modal = Modal(key="Demo Key", title="test")
# cols = st.columns(1)
# col = cols[0]

# style = """
#     <style>
#     .streamlit-modal.st-ewKvni {
#         width: 50%;
#         height: 70% !important;
#         top: 50% !important;
#         left: 50% !important;
#         transform: translate(-50%, -50%) !important;
#     }
#     </style>
# """

# with modal.container():
#     st.markdown('<div id="modal_content"></div>', unsafe_allow_html=True)

# # Add javascript for opening and closing modal
# st.markdown(
#     """
#     <script>
#         function openModal(row_id) {
#             const modal = document.querySelector('.streamlit_modal')
#             const content = modal.querySelector('#modal_content')
#             const rowContent = document.querySelector('#row_' + row_id).innerHTML
#             content.innerHTML = rowContent
#             modal.style.display = (modal.style.display === 'block') ? 'none' : 'block'
#         }
#     </script>
#     """,
#     unsafe_allow_html=True
# )

# # Display the data in a table
# if filtered_df.empty:
#     st.warning('No data to display with the current filters.')
# else:
#     st.table(filtered_df)


# modal = Modal(key="Demo Key",title="test")
# cols = st.columns(1)
# col = cols[0]

# style = """
#     <style>
#     .streamlit-modal.st-ewKvni {
#         width: 50%;
#         height: 70% !important;
#         top: 50% !important;
#         left: 50% !important;
#         transform: translate(-50%, -50%) !important;
#     }
#     </style>
# """

# with col:
#     open_modal = st.button(label='button')
#     if open_modal:
#         with modal.container():
#             st.markdown('testtesttesttesttesttesttesttest')


