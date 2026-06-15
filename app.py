import streamlit as st
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import urllib.parse

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Dhundho 🔍", page_icon="🛍️", layout="centered")

st.title("🛍️ Dhundho")
st.caption("Saw something in a reel and want to know where to buy it? Upload a screenshot and we'll find it for you!")

# ---------- LOAD MODEL (cached so it loads only once) ----------
@st.cache_resource
def load_model():
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    return processor, model

processor, model = load_model()

# ---------- CATEGORY DETECTION (simple keyword-based) ----------
CATEGORY_KEYWORDS = {
    "fashion": ["shirt", "dress", "jacket", "shoes", "sneaker", "jeans", "t-shirt", "kurta", "saree", "hoodie", "bag", "watch"],
    "electronics": ["phone", "laptop", "headphone", "earbuds", "camera", "speaker", "smartwatch", "tablet"],
    "food": ["food", "dish", "plate", "pizza", "burger", "cake", "noodles", "biryani", "drink"],
    "decor": ["room", "sofa", "lamp", "table", "chair", "decor", "wall", "vase", "curtain", "shelf"]
}

def detect_category(caption: str) -> str:
    caption_lower = caption.lower()
    for category, keywords in CATEGORY_KEYWORDS.items():
        if any(word in caption_lower for word in keywords):
            return category
    return "general"

# ---------- SEARCH LINK GENERATION ----------
def generate_links(caption: str, category: str) -> dict:
    query = urllib.parse.quote_plus(caption)
    links = {}

    # Common e-commerce always shown
    links["Amazon"] = f"https://www.amazon.in/s?k={query}"
    links["Flipkart"] = f"https://www.flipkart.com/search?q={query}"

    if category == "fashion":
        links["Myntra"] = f"https://www.myntra.com/{query.replace('+', '-')}"
        links["Meesho"] = f"https://www.meesho.com/search?q={query}"
    elif category == "electronics":
        links["Croma"] = f"https://www.croma.com/searchB?q={query}"
    elif category == "food":
        links["Zomato"] = f"https://www.zomato.com/search?q={query}"
        links["Swiggy"] = f"https://www.swiggy.com/search?query={query}"
    elif category == "decor":
        links["Pepperfry"] = f"https://www.pepperfry.com/site_product/search?q={query}"
        links["IKEA"] = f"https://www.ikea.com/in/en/search/?q={query}"

    return links

# ---------- MAIN UI ----------
uploaded_file = st.file_uploader("📸 Upload a screenshot from a reel", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Your uploaded image", use_container_width=True)

    with st.spinner("AI is analyzing... 🔍"):
        inputs = processor(image, return_tensors="pt")
        out = model.generate(**inputs, max_new_tokens=30)
        caption = processor.decode(out[0], skip_special_tokens=True)

    category = detect_category(caption)

    st.success(f"**AI sees:** {caption}")
    st.info(f"**Category detected:** {category.capitalize()}")

    st.subheader("🛒 Find it here:")
    links = generate_links(caption, category)
    for site, url in links.items():
        st.markdown(f"🔗 [Search on {site}]({url})")

    st.divider()
    st.caption("⚠️ Note: This is a basic version — AI only describes the image, not an exact product match. For better accuracy, CLIP-based visual similarity search can be added.")
else:
    st.info("👆 Upload a screenshot to get started")