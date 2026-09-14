import streamlit as st
import base64
from google import genai

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])


# -----------------------------------
# PAGE BACKGROUND + CUSTOM CSS
# -----------------------------------
def set_background(image_file):
    with open(image_file, "rb") as file:
        encoded = base64.b64encode(file.read()).decode()

    st.markdown(
        f"""
        <style>

        /* PAGE BACKGROUND */
        .stApp {{
            background-color: #EAF6FF;
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}

        /* TEXT INPUT BOXES */
        .stTextInput input {{
            background-color: white !important;
            color: black !important;
        }}

        /* TEXT AREA */
        .stTextArea textarea {{
            background-color: white !important;
            color: black !important;
        }}

        /* ==============================
           FORCE ALL DROPDOWNS WHITE
           ============================== */

        div[data-testid="stSelectbox"] [data-baseweb="select"],
        div[data-testid="stSelectbox"] [data-baseweb="select"] > div,
        div[data-testid="stSelectbox"] [data-baseweb="base-input"],
        div[data-testid="stSelectbox"] [data-baseweb="input"],
        div[data-testid="stSelectbox"] [role="combobox"] {{
            background-color: #FFFFFF !important;
            background: #FFFFFF !important;
        }}

        /* Selected value */
        div[data-testid="stSelectbox"] [data-baseweb="select"] span {{
            color: #222222 !important;
        }}

        /* Arrow */
        div[data-testid="stSelectbox"] [data-baseweb="select"] svg {{
            fill: #222222 !important;
        }}

        /* Dropdown menu */
        div[role="listbox"] {{
            background-color: #FFFFFF !important;
        }}

        div[role="option"] {{
            background-color: #FFFFFF !important;
            color: #222222 !important;
        }}

        div[role="option"]:hover {{
            background-color: #EAF6FF !important;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )


set_background("skincare_background.png.png")

# -----------------------------------
# SKINCARE MARKETING CONTENT GENERATOR
# -----------------------------------

st.title("✨ Skincare Marketing Content Generator")

st.write(
    "Create professional marketing content for your skincare brand in seconds."
)


# -----------------------------------
# WEBSITE BANNER
# -----------------------------------

st.image("skincare_banner.png.png", use_container_width=True)


# -----------------------------------
# BRAND & PRODUCT INFORMATION
# -----------------------------------

st.subheader("📋 Brand & Product Information")

brand_name = st.text_input(
    "🏷️ What is the name of the brand?"
)

product_name = st.text_input(
    "🧴 What is the name of the product?"
)

target_audience = st.text_input(
    "👥 Who is the target audience?"
)

benefits = st.text_area(
    "✨ What are the product benefits?"
)

category = st.text_input(
    "📦 What is the product category?"
)


# -----------------------------------
# CAMPAIGN SETTINGS
# -----------------------------------

st.subheader("🎯 Campaign Settings")

campaign_objective = st.selectbox(
    "🎯 What is the campaign objective?",
    [
        "🆕 Product Launch",
        "🎉 Festive Campaign",
        "🛍️ Promotional Sale",
        "🌱 Brand Awareness",
        "💕 Customer Engagement"
    ]
)

tone = st.selectbox(
    "🎨 Choose the tone",
    [
        "Professional",
        "Friendly",
        "Exciting",
        "Luxury",
        "Casual"
    ]
)

cta = st.selectbox(
    "📢 Choose a Call-to-Action",
    [
        "Shop Now",
        "Buy Now",
        "Learn More",
        "Try It Today",
        "Get 20% Off",
        "Sign Up Now",
        "Discover More"
    ]
)


# -----------------------------------
# CONTACT INFORMATION
# -----------------------------------

st.subheader("📇 Contact Information")

contact_person = st.text_input(
    "👤 Who can customers contact?"
)

contact_role = st.text_input(
    "💼 What is their role? (e.g. Marketing Manager)"
)

contact_email = st.text_input(
    "📧 What is their email address?"
)

contact_phone = st.text_input(
    "📞 What is their contact number?"
)

# -----------------------------------
# CONTENT TYPE
# -----------------------------------

st.markdown("""
<div style="
    background-color: white;
    padding: 15px 20px 10px 20px;
    border-radius: 10px;
    margin-bottom: 15px;
">
""", unsafe_allow_html=True)

content_type = st.selectbox(
    "What do you want to generate?",
    ["📝 Text", "🖼️ Image"]
)

st.markdown("</div>", unsafe_allow_html=True)


# -----------------------------------
# GENERATE CONTENT
# -----------------------------------

if st.button("🚀 Generate Content"):

    # -----------------------------------
    # CHECK REQUIRED INFORMATION
    # -----------------------------------

    if (
        not brand_name
        or not product_name
        or not target_audience
        or not benefits
        or not category
        or not contact_person
        or not contact_email
    ):

        st.warning(
            "Please fill in all the required information before generating content."
        )

    else:

        # -----------------------------------
        # IMAGE GENERATION
        # -----------------------------------

        if content_type == "🖼️ Image":

            st.subheader("🖼️ AI Generated Marketing Image")

            image_prompt = f"""
            Create a professional skincare marketing advertisement.

            Brand name: {brand_name}
            Product name: {product_name}
            Product category: {category}
            Target audience: {target_audience}
            Product benefits: {benefits}

            Campaign objective: {campaign_objective}
            Marketing tone: {tone}
            Call to action: {cta}

            Create a beautiful premium skincare advertisement.

            Visual style:
            - Soft pastel blue background
            - Elegant skincare product photography
            - Botanical leaves
            - Subtle flowers
            - Soft natural lighting
            - Clean and modern design
            - Premium beauty brand aesthetic
            - Professional social media advertisement
            - Attractive composition
            """

            with st.spinner("✨ Creating your skincare image..."):

                try:

                    response = client.models.generate_content(
                        model="gemini-3.1-flash-image-preview",
                        contents=image_prompt
                    )

                    image_found = False

                    for part in response.candidates[0].content.parts:

                        if part.inline_data is not None:

                            image_bytes = part.inline_data.data

                            st.image(
                                image_bytes,
                                caption=f"{product_name} — AI Marketing Creative",
                                use_container_width=True
                            )

                            image_found = True

                    if not image_found:

                        st.warning(
                            "Gemini did not return an image. Please try again."
                        )

                except Exception as e:

                    st.error(
                        f"Unable to generate the image. Error: {e}"
                    )


        # -----------------------------------
        # TEXT GENERATION
        # -----------------------------------

        else:

            # -----------------------------------
            # MARKETING EMAIL
            # -----------------------------------

            email = f"""
Subject: Discover {product_name} by {brand_name}

Dear Customer,

We are pleased to introduce {product_name}, a thoughtfully designed
{category.lower()} from {brand_name}, created especially for
{target_audience}.

Your skincare routine should be simple, effective and enjoyable.
{product_name} is designed to offer {benefits}.

Why you'll love {product_name}:

• {benefits}

This campaign focuses on {campaign_objective.lower()} and is designed
to connect with customers through a {tone.lower()} approach.

Whether you're looking to refresh your daily skincare routine or
give your skin a little extra care, {product_name} makes it easy
to take the next step.

Ready to discover {product_name}?

{cta} and explore what {brand_name} has to offer.

For more information, please feel free to get in touch with us.

Warm regards,

{contact_person}
{contact_role}
{brand_name}

Email: {contact_email}
Phone: {contact_phone}
"""


            # -----------------------------------
            # LINKEDIN POST
            # -----------------------------------

            linkedin = f"""
✨ Introducing {product_name} by {brand_name}

At {brand_name}, we believe skincare should be simple, effective
and easy to make a part of everyday life.

Designed especially for {target_audience}, our {category.lower()}
is created to deliver {benefits}.

Our campaign focuses on {campaign_objective.lower()} with a
{tone.lower()} approach designed to connect with today's consumers.

With {product_name}, we are bringing together thoughtful skincare
and an experience designed around the needs of today's consumers.

{cta} and discover {product_name} today. ✨

#Skincare #Beauty #SelfCare #{brand_name.replace(" ", "")}
"""


            # -----------------------------------
            # INSTAGRAM CAPTION
            # -----------------------------------

            instagram = f"""
✨ Meet {product_name} by {brand_name} ✨

Your skincare routine deserves something special. 🤍

Designed for {target_audience}, {product_name} is a
{category.lower()} created to help you enjoy:

✨ {benefits}

Simple routine. Thoughtful skincare. Beautiful results.

Our {campaign_objective.lower()} campaign is all about making
skincare feel {tone.lower()} and easy to enjoy.

Ready to make {product_name} part of your everyday routine?

{cta}! ✨

#Skincare #Beauty #SelfCare #Glow #SkincareRoutine
"""


            # -----------------------------------
            # TAGLINE
            # -----------------------------------

            tagline = f"{brand_name} – Where Better Skincare Begins."


            # -----------------------------------
            # DISPLAY RESULTS
            # -----------------------------------

            st.subheader("📧 Marketing Email")

            st.text_area(
                "Generated Email",
                email,
                height=450
            )


            st.subheader("💼 LinkedIn Post")

            st.text_area(
                "Generated LinkedIn Post",
                linkedin,
                height=300
            )


            st.subheader("📸 Instagram Caption")

            st.text_area(
                "Generated Instagram Caption",
                instagram,
                height=300
            )


            st.subheader("🏷️ Tagline")

            st.success(tagline)