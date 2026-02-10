import streamlit as st
import os
from supabase import create_client

# --- Supabase setup ---
SUPABASE_URL = 
SUPABASE_KEY = 

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# --- UI ---
st.set_page_config(page_title="Product Image Viewer", layout="centered")

st.title("🖼️ Product Image Viewer")

prod_id = st.number_input(
    "Enter product ID",
    min_value=1,
    step=1
)

if st.button("Load image"):
    with st.spinner("Fetching image..."):
        res = (
            supabase
            .table("prod_url")
            .select("url")
            .eq("prod_id", prod_id)
            .single()
            .execute()
        )

        if res.data is None:
            st.error("❌ No image found for this product ID")
        else:
            img_url = res.data["url"]

            st.success("✅ Image found")
            st.image(
                img_url,
                caption=f"Product ID: {prod_id}",
                use_container_width=True
            )
