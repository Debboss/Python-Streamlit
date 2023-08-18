from PIL import Image
import streamlit as st
import requests
from streamlit_lottie import st_lottie

# Define custom HTML and CSS
custom_css = """
<style>
body {
    background-color: #f29dff; /* Replace with your desired background color */
}
</style>
"""

# Display the custom CSS using st.markdown
st.markdown(custom_css, unsafe_allow_html=True)

# Define a function to load Lottie animation from a URL
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# # URL of the Lottie animation
# lottie_url = "https://lottie.host/a8551faf-6374-4ad0-8e0b-52c635d89e8e/wPSPKXdfB6.json"

# # Load the Lottie animation using the function
# lottie_data = load_lottieurl(lottie_url)

# # Set up columns for layout
# col1, col2 = st.columns([1, 6])  # Adjust column widths as needed

# Display the Lottie animation using the st_lottie component in the second column
# with col2:
#     if lottie_data:
#         st_lottie(lottie_data, speed=1, width=200, height=200)
#     else:
#         st.write("Failed to load Lottie animation from the URL.")

# First container
with st.container():
    st.subheader("スターガーディアン")
    st.title("ガーディアンたちを紹介")
    st.write("広大で暗い宇宙の中で、運命により選ばれし、若き戦士たちが星の光を守る。彼らはまばゆく輝き、そして燃え尽きる運命にある。")
    st.write("[こちら >](https://universe.leagueoflegends.com/ja_JP/star-guardian/)")

# Second container
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)

    with left_column:
        st.header("バイオを読みましょう")
        st.write("アーリ")
        st.write(
            """
            - 学年２
            - 血液型 O型
            - 趣味 ダンス
            - 武器 魅了魔法
            """
        )

    with right_column:
        st.write("キコ")
        st.write(
            """
            - 彼女のマジカルコンパニオン
            - キコは、アーリのカリスマ性と生意気さをキツネの形にしたかのような存在だ。
            """
        )

st.header("“私たちの運命は、私たちが決めるのよ”")

# URL of the Lottie animation
lottie_url = "https://lottie.host/a8551faf-6374-4ad0-8e0b-52c635d89e8e/wPSPKXdfB6.json"
# img_contact_form = Image.open("images/A_New_Horizon_Group")


# Load the Lottie animation using the function
lottie_data = load_lottieurl(lottie_url)

# Set up columns for layout
col1, col2 = st.columns([1, 6])  # Adjust column widths as needed

# Display the Lottie animation using the st_lottie component in the second column
with col2:
    if lottie_data:
        st_lottie(lottie_data, speed=1, width=220, height=250)
    else:
        st.write("Failed to load Lottie animation from the URL.")

with st.container():
    st.write("---")
    st.header("私のプロジェクト")
    st.write("##")
    image_column, text_column = st.columns((1, 2))

    with image_column:
        pass

    with text_column:
        st.header("あなたは、星だ！")
        st.write(
            """
            星空へと舞い上がり、街を襲撃するモンスターに立ち向かうスターガーディアンたちを目撃しよう。
            """
        )
        st.markdown("[こちらこそ](https://universe.leagueoflegends.com/ja_JP/star-guardian/)")

