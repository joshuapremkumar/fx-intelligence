import streamlit as st
import requests
import time

# ---------------- CONFIG ----------------
API_URL = "YOUR_CLOUD_RUN_URL/analyze"  # ← replace this

st.sidebar.header("⚙️ Controls")
refresh_rate = st.sidebar.slider("Refresh Interval (seconds)", 2, 10, 5)

st.set_page_config(
    page_title="FX Intelligence Dashboard",
    layout="wide",
)

# ---------------- STYLING ----------------
st.markdown("""
<style>
.big-font {
    font-size:28px !important;
    font-weight: bold;
}
.metric-card {
    padding: 10px;
    border-radius: 10px;
    background-color: #f5f7fa;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.title("📊 FX Intelligence Dashboard")
st.caption("Real-time currency insights powered by API + Tavily")

# ---------------- INPUTS ----------------
col1, col2 = st.columns(2)

with col1:
    base = st.selectbox("Base Currency", ["USD", "EUR"])

with col2:
    target = st.selectbox("Target Currency", ["INR", "GBP"])

# ---------------- STATE ----------------
if "data" not in st.session_state:
    st.session_state.data = []

placeholder = st.empty()

# ---------------- LOOP ----------------
while True:
    try:
        response = requests.post(API_URL, json={"base": base, "target": target})
        res = response.json()

        rate = res["rate"]
        signal = res["signal"]
        insight = res["insight"]
        news = res["news"]

        st.session_state.data.append(rate)
        st.session_state.data = st.session_state.data[-20:]

        # ---------------- UI RENDER ----------------
        with placeholder.container():

            # --- Top Metrics ---
            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("💱 Pair", res["pair"])

            with col2:
                st.metric("📈 Rate", f"{rate:.2f}")

            with col3:
                if signal == "buy":
                    st.success(f"🟢 Signal: {signal.upper()}")
                elif signal == "sell":
                    st.error(f"🔴 Signal: {signal.upper()}")
                else:
                    st.warning(f"🟡 Signal: {signal.upper()}")

            st.divider()

            # --- Chart ---
            st.subheader("📊 Live Price Movement")
            st.line_chart(st.session_state.data)

            if len(st.session_state.data) > 2:
                if st.session_state.data[-1] > st.session_state.data[-2]:
                    st.success("📈 Uptrend detected")
                else:
                    st.error("📉 Downtrend detected")

            st.divider()

            # --- Insight + News ---
            col1, col2 = st.columns(2)

            with col1:
                st.subheader("🧠 Insight")
                st.info(insight)

            with col2:
                st.subheader("📰 Latest News")
                if news:
                    for n in news:
                        st.write("•", n)
                else:
                    st.write("No recent news available")

    except Exception as e:
        st.error(f"Error: {e}")

    time.sleep(refresh_rate)