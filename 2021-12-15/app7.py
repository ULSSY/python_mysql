import streamlit as st
from PIL import Image

# 설정 : 웹페이지의 타이틀(탭에 표시되는 아이콘과 제목) 바꾸기
img = Image.open('data/image_03.jpg')
st.set_page_config(page_title='Machine Learning', page_icon= img, layout='wide', initial_sidebar_state='collapsed')

def main() :
    pass

if __name__ == '__main__' :
    main()