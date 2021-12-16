import streamlit as st
# 만든 eda_app.py를 연결해주자.
# 다른 파일에 있는 함수를 사용하기 위해 import 한다.
from eda_app import run_eda_app
from ml_app import run_ml_app
# 코드가 많아지면 빠르게 처리하는데 문제가 있기에
# 관리 편의성을 위해 파일을 분리해 처리하기로 한다.

def main() :
    st.title('파일 분리 앱')

    menu = ['Home', 'EDA', 'ML', 'About']
    choice = st.sidebar.selectbox("메뉴", menu)

    if choice == 'Home' :
        st.subheader('홈 화면입니다.')
        
    elif choice == 'EDA' :
        # 컨트롤 누르고 이 밑에 함수에 가져다 대면 설명도 나오고 
        # 그대로 클릭하면 함수를 작성한 곳으로 점프 된다.
        run_eda_app()
    elif choice == 'ML' :
        run_ml_app()
    else : 
        st.subheader('앱 소개 화면입니다.')
