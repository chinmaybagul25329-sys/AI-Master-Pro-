import streamlit as st

# --- 1. APP CONFIG (Professional Icon) ---
st.set_page_config(
    page_title="AI Master 2.0",
    page_icon="🤖",
    layout="wide"
)

# --- 2. THEME: PITCH BLACK & TEAL (Gemini Style) ---
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #E3E3E3; }
    section[data-testid="stSidebar"] { background-color: #111111; border-right: 1px solid #333333; }
    .stButton>button {
        background-color: #1A1A1A; color: #10A37F; border: 1px solid #4D4D4F;
        border-radius: 12px; padding: 10px 24px; font-weight: bold; transition: 0.4s;
    }
    .stButton>button:hover {
        border-color: #10A37F; box-shadow: 0 0 15px rgba(16, 163, 127, 0.4); color: white;
    }
    input { background-color: #202123 !important; color: white !important; border: 1px solid #4D4D4F !important; border-radius: 10px !important; }
    h1, h2 { color: #74AA9C; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. PERSISTENT LOGIN (Baar-baar password nahi mangega) ---
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.markdown("<h1 style='text-align: center;'>🤖 AI Master Login</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: gray;'>Commander, system unlock karne ke liye key dalein.</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        password = st.text_input("", type="password", placeholder="Password yahan likhen...")
        if st.button("Unlock Power ⚡"):
            if password == "bhai":
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("Galat Key!")
else:
    # --- 4. MAIN DASHBOARD ---
    st.sidebar.title("🤖 Master Control")
    task = st.sidebar.radio("Mission:", ["🎬 Video AI", "🎨 Image AI", "🧪 Science 3D", "🧠 Master Search"])

    # --- VIDEO CREATOR ---
    if task == "🎬 Video AI":
        st.title("🎬 AI Video Generation")
        prompt = st.text_input("Kya video banana hai?", placeholder="A futuristic city with flying cars...")
        if st.button("Generate Video ⚡"):
            st.info("AI रेंडरिंग शुरू हो गई है... (HuggingFace Engine)")
            st.components.v1.iframe("https://guoyww-animatediff.hf.space", height=600)

    # --- IMAGE CREATOR ---
    elif task == "🎨 Image AI":
        st.title("🎨 AI Image Artist")
        img_prompt = st.text_input("Apni kalapna likhen:")
        if st.button("Create Image ✨"):
            with st.spinner("AI is painting..."):
                url = f"https://pollinations.ai/p/{img_prompt.replace(' ', '%20')}?width=1024&height=1024&nologo=true"
                st.image(url, caption="Commander, apki kalapna hakikat mein!")

    # --- SCIENCE LAB ---
    elif task == "🧪 Science 3D":
        st.title("🧪 3D Science Lab")
        sci_topic = st.text_input("Physics/Bio Topic:")
        if st.button("Show Animation"):
            st.video(f"https://www.youtube.com/results?search_query={sci_topic}+3d+animation")

    # --- SEARCH ---
    elif task == "🧠 Master Search":
        st.title("🧠 Universal Brain")
        query = st.text_input("Mujhse kuch bhi puche:")
        if st.button("Analyze"):
            st.markdown(f"👉 **[Full Result Here](https://www.google.com/search?q={query.replace(' ', '+')})**")

    if st.sidebar.button("Logout"):
        st.session_state.authenticated = False
        st.rerun()
      
