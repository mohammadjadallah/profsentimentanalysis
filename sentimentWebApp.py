import streamlit as st
import pandas as pd
import numpy as np
import textblob as blob

# st.title("Sentiment Analyzer Online For Free")
# change the name and the icon of web app
st.set_page_config(page_title="professorSA", page_icon='heart.png')

# Hide the made with streamlit and humburgur menu
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


# unsafe_allow_html to allow writing html tags, you can writing just text
st.write("<center><h1 style='font-size:60px; font-family: Trebuchet MS, sans-serif;'>Sentiment Analyzer</h1></center><br>",
         unsafe_allow_html=True)

# Simple text
st.write("""<center>
<h4 style='text-align:center; font-family: Trebuchet MS, sans-serif;'>
 Detect emotions in textual data with <br> the speediest
 sentiment analyzer.</h4>
 </center><br>""",
         unsafe_allow_html=True)

# Radio Button | choose if subjectivity or polarity
# st.write("<b>Choose Option:<b>", unsafe_allow_html=True)
radio = st.radio(label='Choose Option:',
         options=['Polarity', 'Subjectivity'],
         label_visibility="visible")

# User text erea
user_input_text = st.text_area(label='', placeholder="Write your text here...",
             height=250, label_visibility="hidden")

# you can create columns to better manage the flow of your page
# this command makes 3 columns of equal width
col1, col2, col3 = st.columns(3, gap='large')
with col2:
    clicked = st.button("Anlyze The Text", type="primary",
                        )

# Sentiment Analysis Code
# Intialize the object
textblob = blob.TextBlob(user_input_text)


def table_html(type_of_sentiment: str, value: float, tag=None) -> str:
    if type_of_sentiment == "Subjectivity":
        html_tabel = f"""
            <table style="margin-left: 150px;
             margin-top:40px;
             width:300px">
                <thead style="text-align:center">
                    <td style="padding:20px 20px;
                    color: rgb(188, 182, 174);
                     font-weight: bold;">{type_of_sentiment}</td>
                    <td style="padding:20px 20px;
                     font-weight: bold;
                     color: rgb(80, 213, 138);">{round(value * 100)}%</td>
                </thead>
            </table>
        """
        return html_tabel
    else:
        html_tabel = f"""
                    <table style="margin-left: 150px;
                     margin-top:40px;
                     width:300px;">
                        <thead style="text-align:center">
                            <td style="padding:20px 20px; 
                            color: rgb(188, 182, 174);
                             font-weight: bold;">{type_of_sentiment}</td>
                            <td style="padding:20px 20px; font-weight: bold;
                            color: rgb(173, 194, 212);">{tag}</td>
                            <td style="padding:20px 20px; color: rgb(80, 213, 138);
                             font-weight: bold;">{round(value * 100, 1)}%</td>
                        </thead>
                    </table>
                """
        return html_tabel

if clicked:
    if "Polarity" == radio:
        def polarity_analyzer():
            # find the polarity
            polarity = textblob.sentiment.polarity
            rounding = polarity  # round(polarity, 2)
            if polarity > 0:
                st.write(table_html(type_of_sentiment="Polarity",
                                    value=rounding, tag="Positive"),
                         unsafe_allow_html=True)
            elif polarity < 0:
                st.write(table_html(type_of_sentiment="Polarity",
                                    value=abs(rounding), tag="Negative"),
                         unsafe_allow_html=True)
            else:
                st.write(table_html(type_of_sentiment="Polarity",
                                    value=rounding, tag="Natural"),
                         unsafe_allow_html=True)

        polarity_analyzer()

    else:
        def subjectivity_analyzer():
            import tabulate as table
            # find the subjectivity
            subjectivity = textblob.sentiment.subjectivity
            rounding = subjectivity  # round(subjectivity, 2)
            if subjectivity > 0.5:
                st.write(table_html(type_of_sentiment="Subjectivity",
                                    value=rounding),
                         unsafe_allow_html=True)
            elif subjectivity < 0.5:
                st.write(table_html(type_of_sentiment="Subjectivity",
                                    value=rounding),
                         unsafe_allow_html=True)

        subjectivity_analyzer()


# df = pd.DataFrame(data={})
# st.write(df)


