import streamlit as st
import pandas as pd
# 이미지 처리를 위한 라이브러리
from PIL import Image

def main():
    ## 넘파이이다.
    img =Image.open('data/image_03.jpg')
    print(img)
    st.image(img)
    
    st.image(img, use_column_width= True)
    #웹상의 이미지를 띄우겠다
    st.image('http://www.outdoornews.co.kr/news/photo/202009/32077_90504_551.jpg')
    
    # 동영상도 플레이 시킬 수 있다.
    # open은 파이썬의 함수이다. rb는 읽기아 바이너리로 열어라
    video_file = open('data/Lake_video.mp4', 'rb')
    st.video(video_file)

    # 오디오파일은 아래와같이 플레이 할 수 있다.
    # audio_file = open('data/song.mp3', 'rb')
    # st.audio(audio_file.read(), format = 'audio/mp3')
    

if __name__ == '__main__' :
    main()