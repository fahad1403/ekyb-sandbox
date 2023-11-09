import streamlit as st

def set_custom_css():
    custom_css = """
    <style>
     .title {
    color: #459877; /* Title color */
    font-size: 36px; /* Title font size */
    font-weight: bold; /* Bold font weight */
    text-align: center; /* Text alignment */
    margin-bottom: 20px; /* Add some spacing below the title */
 
} 
  .st-emotion-cache-16idsys p{
  font-weight:bold;
  font-size:14px;
  }
  .st-cp{
  color: #00FF00 !important;
  }
  .st-emotion-cache-5rimss p{
  font-size:15px;
#   font-weight:bold;
#   text-align:center;
#   align:center;
  }
  .st-emotion-cache-1y04v0k{
  align:center;
  text-align:center;
  }
  .st-emotion-cache-7ym5gk:hover{
  color: white !important;
  background-color: #009877;
  }
   .creds{
   color:white;
    font-weight:bold;
   }
 .stTextInput  > label {
    color:white;
    font-weight:bold;
    }
    
    # .st-emotion-cache-10trblm{
    # align:center;
    # text-align:center;
    # }
    # .modal-overlay{
    # color:white;
    # width:90%;
    # height:90%;
    # }
    .st-emotion-cache-1gulkj5{
        background: linear-gradient(to bottom, #009877 0%,#008988 100%);

    }
    .st-emotion-cache-r421ms{
        background: linear-gradient(to bottom, #009877 0%,#008988 100%);

    }
    .div:first-child{
    overflow:auto;
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
        background-color: #009877;
        border: 1px solid white;
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
        border: 2px solid white;
    }
    .st-cf {
    color: #789877
    }
    .st-cf:hover {
    color: #009877
    }
    .st-cp {
        background-color: #009877;
    }
#     .st-emotion-cache-10oheav{
#      background:linear-gradient(to bottom, #009877  0%,#00ffff  100%);
#      height:100%;
#      width:100%
#    }
#    .st-emotion-cache-10oheav h2{
#    align:center;
#    text-align:center;
#    font-size:20px;
#    color:white;
#    font-weight:bold;
#    }
#    .st-emotion-cache-16idsys p{
#    align:center;
#    text-align:center;
#    color:white;
#    font-weight:bold;
#    }
#    .st-emotion-cache-fblp2m{
#    color:white;
#    }
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
    .st-emotion-cache-1y04v0k{
        background: linear-gradient(to bottom, #009877 0%, #008988 100%);
     
    color: white; /* Set the text color to white or any color that contrasts well with the gradient */
    align:center;
    /* Add other styling as needed */
    }
    .st-em{
    text-align:center;
    align:center;
    font-size:15px;
    font-weight:bold;
    }
    .st-gf{
    text-align:center;
    align:center;
    font-size:15px;
    font-weight:bold;
    }
    .st-emotion-cache-16idsys p{
    text-align:center;
    font-weight:bold;
    }
    h3 {
     color: #3498db !important;
     text-align:center;
    align:center;
    font-weight:bold;
    }
    .sub-title{
    text-align:center;
    align:center;
    font-weight:bold;
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
    div[data-modal-container='true'][key='Details_Modal'] > div:first-child > div:first-child{
                             max-height: 700px; /* Adjust the maximum height as needed */
                            overflow-y: auto !important;
    }
    .st-emotion-cache-rj5w3t e1f1d6gn0{
                width:90%;
                height:80%;
                top:70%;
                left:70%;
                }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)
   