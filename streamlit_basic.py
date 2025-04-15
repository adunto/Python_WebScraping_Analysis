# streamlit run streamlit_basic.py

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

plt.rc('font', family='NanumGothic')

# 샘플 데이터 생성
data = {'선거구': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C'],
        '성별': ['남', '여', '남', '여', '남', '여', '남', '여', '남']}
df = pd.DataFrame(data)

# Streamlit 앱
st.title("📊 Pandas DataFrame & Seaborn Plot")

df_random = pd.DataFrame(
        np.random.randn(10, 20),
        columns=('col %d' % i for i in range(20)),
)
st.dataframe(df_random)

# DataFrame 출력
st.subheader("📋 데이터 테이블")
st.dataframe(df)

# 시각화
st.subheader("📈 Seaborn 그래프")
fig, ax = plt.subplots()
sns.countplot(data=df, x='선거구', hue='성별', palette={'남': 'navy', '여': 'orange'}, ax=ax)
st.pyplot(fig)