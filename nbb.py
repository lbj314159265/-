import streamlit as st

from datetime import time, date
from PIL import Image
import io
# 设置页面配置
st.set_page_config(
    page_title="个人简历生成器",
    page_icon="📄",
    layout="wide"
)

# 添加标题和描述
st.title("🎨个人简历生成器")
st.caption("使用Streamlit创建您的个性化简历")
##初始化session_state（存储上传的图片）
if 'uploaded_image' not in st.session_state:
    st.session_state.uploaded_image = None
if 'languages' not in st.session_state:
    st.session_state.languages = ["中文"]  # 设置默认语言
if 'skills' not in st.session_state:
    st.session_state.skills = []
if 'bio' not in st.session_state:  # 添加个人简介的初始化
    st.session_state.bio = " "     
# 创建两列布局
col1, col2 = st.columns([1, 2], gap="large")

with col1:
    st.header("个人信息表单", divider="blue")
    
    # 基本信息部分
    st.subheader("基本信息")
    
    # 姓名和职位布局 - 已去除下拉效果
    st.text_input("姓名", key="name")
    st.selectbox("职位",[" ","工人","组长", "厂长", "CEO"],key="position")      
    phone_types = [" ","水果16", "OPPO A5", "菠萝手机","小米15pro", "其他"]
    phone_type = st.selectbox("电话", phone_types, key="phone_type")
    
    # 当选择"其他"时，显示自定义输入框
    if phone_type == "其他":
        custom_phone = st.text_input("请输入您的电话", key="custom_phone")        
        if custom_phone:
            phone_type = custom_phone
    
    email = st.text_input("邮箱", key="email")
    st.date_input("出生日期", value=date(2015, 6, 13), key="birth_date")    
    # 性别和学历布局
    gender = st.radio("性别", ["男", "女", "其他物种"], horizontal=True, key="gender")
    education = st.selectbox("学历", [" ","小学","初中","高中", "大专", "本科", "硕士", "博士"], key="education")
    st.text_input("毕业院校", key="school")
    
    # 工作经验和期望薪资
    
    st.session_state.languages = st.multiselect(
        "语言能力",
        options=["中文", "英语四级", "英语六级", "德语", "日语", "法语", "俄罗斯语"],
        default=st.session_state.languages,
        placeholder="Choose an option...", 
        key="languages_selector"
    )
    
    st.session_state.skills = st.multiselect(
        "技能（可多选）",
        options=["Python", "Java", "JavaScript", "HTML/CSS", "SQL", "数据分析", "深度学习", "项目管理"],
        default=st.session_state.skills,
        placeholder="Choose an option...",
        key="skills_selector"
    )
   
    experience = st.slider("工作经验(年)", 0, 30, 9, key="experience")
    salary = st.slider("期望薪资", 10,3000,50, key="salary")
    
    bio_input = st.text_area(
        "个人简介",
        value=st.session_state.bio,
        placeholder="请简单介绍您的专业背景、职业目标和个人特长和兴趣爱好...",
        key="bio_input"
    )
    st.session_state.bio = bio_input

    # 联系时间和语言能力
    contact_time = st.time_input("每日最佳联系时间", time(9, 0), key="contact_time")
     # 图片上传区域
 
    uploaded_file = st.file_uploader(
        "上传个人照片",
        type=["jpg", "jpeg", "png"],
        key="photo_upload"
    )
    if uploaded_file is not None:
        st.session_state.uploaded_image = uploaded_file.read()
with col2:
    st.header("个人简历", divider="blue")
    # 简历顶部布局（头像+基本信息）
    col2_1, col2_2 = st.columns([1, 2])
    
    with col2_1:
        st.subheader(st.session_state.name if 'name' in st.session_state else ' ')
        # 显示上传的图片或占位图
        if st.session_state.uploaded_image:
            st.image(Image.open(io.BytesIO(st.session_state.uploaded_image)), width=150)
        else:
            st.image("https://via.placeholder.com/150", width=150)      
        st.write(f"**职位：** {st.session_state.position if 'position' in st.session_state else " "}")
        st.write(f"**电话：** {st.session_state.phone_type if 'phone_type' in st.session_state else " "}")
        st.write(f"**邮箱：** {st.session_state.email if 'email' in st.session_state else " "}")  
        st.write(f"**出生日期:** {st.session_state.birth_date.strftime('%Y/%m/%d') if 'birth_date' in st.session_state else '未填写'}")
    with col2_2:    
        st.write(f"**性别:** {st.session_state.gender if 'gender' in st.session_state else '未填写'}")       
        st.write(f"**学历:** {st.session_state.education if 'education' in st.session_state else '未填写'}")
        st.write(f"**毕业院校:** {st.session_state.school if 'school' in st.session_state else '未填写'}")
        st.write(f"**工作经历:** {st.session_state.experience}年" if 'experience' in st.session_state else "**工作经历:** 未填写")
        st.write(f"**期望薪资:** {st.session_state.salary}元" if 'salary' in st.session_state else "**期望薪资:** 未填写")
        st.write(f"**最佳联系时间:** {st.session_state.contact_time.strftime('%H:%M') if 'contact_time' in st.session_state else '未填写'}")
        st.write(f"**语言能力:** {', '.join(st.session_state.languages) if st.session_state.languages else '未填写'}")   
            
                 
      # 基本信息区块      

    
    # 个人简介区块
    st.divider()
    st.subheader("个人简介")
    st.write(st.session_state.bio if st.session_state.bio else "请填写个人简介...")
    # 专业技能区块
    st.subheader("专业技能")
    if 'skills' in st.session_state and st.session_state.skills:
        cols = st.columns(3)  # 3列布局显示技能
        for i, skill in enumerate(st.session_state.skills):
            cols[i % 3].write(f"• {skill}")
    else:
        st.write("请添加您的技能...")

    # 底部装饰文本
        