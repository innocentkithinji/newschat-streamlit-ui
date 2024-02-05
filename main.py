import requests
import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space


def on_submit_click():
    st.toast("Processing... Please wait...", icon="⏳")

    s = requests.Session()

    full_response = []

    with s.post('http://api.newschat.ikithinji.com/chat/', stream=True,
                json={"input": st.session_state.text_input}) as r:
        for line in r.iter_content():
            full_response.append(line.decode('utf-8'))
            result = "".join(full_response).strip()

            with streaming_box.container():
                st.markdown('---')
                st.markdown('## Response')
                st.markdown(result)
                st.markdown('---')

        st.session_state.output_text = "".join(full_response).strip()
        st.toast("Done! ✅", icon="👍🏽")


# Main Form

with st.form(key='my_form'):
    text_input = st.text_input(label='What do you want to Know?', key='text_input')
    submit_button = st.form_submit_button(label='Submit', on_click=on_submit_click)

with st.sidebar:
    st.title("News Chat 📰 💬")
    st.markdown('''
        ## About
        This is a comical news answering machine. It give you feedback on news articles in a comical and funny way.
        
        
        Was built using:
         - [Streamlit](https://streamlit.io)
         - [LangChain](https://langchain.io)
         - [OpenAI](https://openai.com)  
         - [Milvus](https://milvus.io)          
    ''')
    st.write("Built with ❤️ by [Innocent Kithinji](https://www.linkedin.com/in/ikithinji/)")

streaming_box = st.empty()

# For Showing the Completed Output
if "output_text" in st.session_state:
    st.markdown("---")
    st.markdown("#### Response:")
    st.markdown(st.session_state["output_text"])
    st.markdown("---")
