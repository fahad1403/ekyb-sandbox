import streamlit as st

def set_custom_css():
    custom_css = """
    <style>
     .title {
    color: #3498db; /* Title color */
    font-size: 36px; /* Title font size */
    font-weight: bold; /* Bold font weight */
    text-align: center; /* Text alignment */
    margin-bottom: 20px; /* Add some spacing below the title */
 
} 
   .creds{
   color:white;
    font-weight:bold;
   }
 .stTextInput  > label {
    color:white;
    font-weight:bold;
    }
    .st-emotion-cache-1gulkj5{
    background:linear-gradient(to bottom, #3399ff  0%,#00ffff  100%);
    }
    .st-emotion-cache-r421ms{
    background:linear-gradient(to bottom, #3399ff  0%,#00ffff  100%);
    }
    # .st-emotion-cache-10trblm{
    #  color:white;
    # font-weight:bold;
    # align:center
    # text-align:center;
    # }
    # .st-emotion-cache-1aehpvj{
    # color:white;
    # font-weight:bold;
    # align:center
    # text-align:center;
    # }
    # .st-emotion-cache-1fttcpj{
    # color:white;
    # font-weight:bold;
    # align:center
    # text-align:center;
    # }
    .stButton>button {
        display: block;
        margin: 0 auto;
        align-items: center;
        background-image: linear-gradient(144deg, #AF40FF, #5B42F3 50%, #00DDEB);
        border: 0;
        border-radius: 6px;
        box-shadow: rgba(151, 65, 252, 0.2) 0 15px 30px -5px;
        box-sizing: border-box;
        color: #FFFFFF;
        display: flex;
        font-family: Phantomsans, sans-serif;
        font-size: 20px;
        justify-content: center;
        line-height: 1em;
        max-width: 100%;
        min-width: 140px;
        padding: 19px 24px;
        text-decoration: none;
        user-select: none;
        -webkit-user-select: none;
        touch-action: manipulation;
        white-space: nowrap;
        cursor: pointer;
    }
    .stButton>button:hover {
        color: #00FF00 !important;
    }
    .stButton>button:active {
        color: #00FF00 !important;
    }
    @media (max-width: 768px) {
        .stButton>button {
            font-size: 16px;
            padding: 15px 20px;
        }
    }
    .st-emotion-cache-9ycgxx{
    color:white;
    font-weight:bold;
    # text-align:right;
    # align:right;
    }
    .st-emotion-cache-1aehpvj{
     color:white;
    font-weight:bold;
    #  text-align:right;
    # align:right;
    }
    @media screen and (max-width: 768px) {{
        .st-emotion-cache-5rimss {{
            width: 100%;
        }}
        .st-emotion-cache-5rimss {{
            width: {value}%;
            font-size: 10px;
        }}
    }}
    @media (max-width: 768px){
    .st-emotion-cache-5rimss{
     width: 100%;
    }
    .st-emotion-cache-5rimss{
    width: {value}%;
    font-size: 10px;
    }
    }
    @media (max-width: 768px){
    .st-emotion-cache-fg4pbf {
     font-size: 12px;
    }
    }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)
   