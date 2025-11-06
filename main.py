import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="펫뉴비 | PetNewbie", page_icon="🐾", layout="wide")

# 폰트 적용 (Google Fonts)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');
    html, body, [class*="css"] {
        font-family: 'Jua', sans-serif;
    }
    .main-title {
        text-align: center;
        font-size: 64px;
        color: #FF7F50;
        margin-top: 40px;
        margin-bottom: 10px;
    }
    .section-title {
        font-size: 28px;
        color: #333333;
        margin-top: 40px;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# 첫 화면 타이틀
st.markdown("<h1 class='main-title'>🐾 PetNewbie 🐾</h1>", unsafe_allow_html=True)
st.markdown("### 반려동물의 모든 순간을 함께하는 스마트 파트너 🐶🐱")

st.divider()

# 반려동물 정보 입력 섹션
st.markdown("<h3 class='section-title'>반려동물 정보 입력</h3>", unsafe_allow_html=True)

with st.form("pet_info_form"):
    name = st.text_input("이름을 입력하세요 🐾")
    species = st.selectbox("종을 선택하세요", ["강아지", "고양이", "토끼", "기타"])
    age = st.number_input("나이 (년 단위)", min_value=0, max_value=50, step=1)
    personality = st.text_input("성격을 입력해주세요 (예: 활발함, 차분함 등)")
    health = st.selectbox("현재 건강 상태", ["좋음", "보통", "관리 필요"])

    submitted = st.form_submit_button("완료 ✅")

# 다음 페이지로 이동 (조건부 렌더링)
if submitted:
    st.success(f"{name}의 정보를 저장했습니다!")

    st.markdown("<h3 class='section-title'>맞춤형 조언 💡</h3>", unsafe_allow_html=True)

    # 기본적인 조언 로직
    advice = ""
    if species == "강아지":
        if age < 2:
            advice = "아직 어린 강아지네요! 예방접종과 사회화 훈련을 꾸준히 해주세요 🐕"
        elif age < 8:
            advice = "활동량이 많은 시기예요. 규칙적인 산책과 균형 잡힌 식단이 중요합니다 🦴"
        else:
            advice = "노령견이라면 관절과 체중 관리에 신경 써주세요 ❤️"
    elif species == "고양이":
        if age < 2:
            advice = "호기심 많은 시기! 놀이 시간을 충분히 주세요 🐈"
        elif age < 8:
            advice = "적당한 운동과 스트레스 관리가 필요해요 😺"
        else:
            advice = "노령묘는 신장 건강과 수분 섭취를 잘 챙겨주세요 💧"
    else:
        advice = "다양한 종의 동물이 있네요! 건강한 식단과 청결 유지가 중요합니다 🩺"

    st.info(advice)

    st.divider()

    # 추가 기능 섹션
    st.markdown("<h3 class='section-title'>📋 펫뉴비 주요 기능</h3>", unsafe_allow_html=True)
    st.markdown("""
    - 🩺 **예방접종 · 건강검진 알림 기능**  
      등록된 종과 나이에 따라 맞춤 알림을 제공합니다.  

    - 🍖 **체중 · 식사 기록**  
      날짜별 체중, 식사량, 사료 종류 등을 기록할 수 있습니다.  

    - 🏥 **병원 방문 기록 & 영수증 관리**  
      진료 이력과 비용을 손쉽게 관리하세요.  

    - 📅 **스마트 일정 관리**  
      병원 예약, 산책 일정 등 자동 알림을 받아보세요.  
    """)

else:
    st.info("반려동물 정보를 입력하고 ‘완료’ 버튼을 눌러주세요!")


