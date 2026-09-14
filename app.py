import streamlit as st
import base64


# -----------------------------------
# PAGE CONFIGURATION
# -----------------------------------

st.set_page_config(
    page_title="Skincare Marketing Generator",
    page_icon="🫧",
    layout="centered"
)


# -----------------------------------
# BACKGROUND
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
# BANNER
# -----------------------------------

st.image(
    "skincare_banner.png.png",
    use_container_width=True
)


# -----------------------------------
# TITLE
# -----------------------------------

st.title("🫧 Skincare Marketing Content Generator")

st.write(
    "Create professional marketing content for your skincare brand in seconds."
)


# -----------------------------------
# BRAND INFORMATION
# -----------------------------------

st.header("🪞 Brand Information")

brand_name = st.text_input(
    "Brand Name *"
)

product_name = st.text_input(
    "Product Name *"
)

target_audience = st.text_input(
    "Target Audience *",
    placeholder="Example: Young adults with sensitive skin"
)

benefits = st.text_area(
    "Product Benefits *",
    placeholder="Example: Hydrates skin, reduces dryness, gives a natural glow"
)

category = st.selectbox(
    "Product Category",
    [
        "Face Serum",
        "Moisturizer",
        "Cleanser",
        "Sunscreen",
        "Face Mask",
        "Eye Cream",
        "Body Care",
        "Lip Care",
        "Other"
    ]
)


# -----------------------------------
# CAMPAIGN SETTINGS
# -----------------------------------

st.subheader("📋 Campaign Details")

campaign_objective = st.selectbox(
    " 📋What is the campaign objective?",
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

st.subheader("📞 Contact Information")

contact_person = st.text_input(
    "Contact Person *"
)

contact_role = st.text_input(
    "Contact Role",
    placeholder="Example: Marketing Manager"
)

contact_email = st.text_input(
    "Contact Email *"
)

contact_phone = st.text_input(
    "Contact Phone"
)


# -----------------------------------
# CONTENT TYPE
# -----------------------------------

st.subheader("📢 What would you like to generate?")

content_type = st.selectbox(
    "Select Marketing Content",
    [
        "💌 Marketing Email",
        "💼 LinkedIn Post",
        "📸 Instagram Caption",
        "🏷️ Tagline"
    ]
)
# Show the selected platform logo
if content_type == "LinkedIn Post":
    st.image("linkedin_logo.png", width=45)

elif content_type == "Instagram Caption":
    st.image("instagram_logo.png", width=45)

# -----------------------------------
# GENERATE CONTENT
# -----------------------------------

if st.button("🚀 Generate Content"):

    # -----------------------------------
    # VALIDATION
    # -----------------------------------

    if (
        not brand_name
        or not product_name
        or not target_audience
        or not benefits
        or not contact_person
        or not contact_email
    ):

        st.warning(
            "Please fill in all the required fields marked with *."
        )

    else:

        # -----------------------------------
        # MARKETING EMAIL
        # -----------------------------------

        if content_type == "📧 Marketing Email":

            email = f"""
Subject: Discover {product_name} by {brand_name}

Dear Customer,

We are excited to introduce {product_name}, a thoughtfully
designed {category.lower()} from {brand_name}.

Created especially for {target_audience}, {product_name}
is designed to provide {benefits}.

Why you'll love {product_name}:

✨ {benefits}

Our current campaign focuses on
{campaign_objective.lower()} and communicates through a
{tone.lower()} approach.

Ready to make {product_name} part of your skincare routine?

{cta} and discover what {brand_name} has to offer.

For more information, please feel free to contact us.

Warm regards,

{contact_person}
{contact_role}
{brand_name}

Email: {contact_email}
Phone: {contact_phone}
"""

            st.subheader("📧 Marketing Email")

            st.text_area(
                "Generated Email",
                email,
                height=450
            )


        # -----------------------------------
        # LINKEDIN POST
        # -----------------------------------

        elif content_type == "💼 LinkedIn Post":

            linkedin = f"""
✨ Introducing {product_name} by {brand_name}

At {brand_name}, we believe skincare should be simple,
effective and easy to make part of everyday life.

Designed especially for {target_audience},
our {category.lower()} is created to provide
{benefits}.

Our campaign focuses on {campaign_objective.lower()}
with a {tone.lower()} approach.

We are proud to bring thoughtful skincare solutions
to today's consumers.

{cta} and discover {product_name} today. ✨

#Skincare #Beauty #SelfCare #SkincareRoutine
#{brand_name.replace(" ", "")}
"""

            st.subheader("💼 LinkedIn Post")

            st.text_area(
                "Generated LinkedIn Post",
                linkedin,
                height=350
            )


        # -----------------------------------
        # INSTAGRAM CAPTION
        # -----------------------------------

        elif content_type == "📸 Instagram Caption":

            instagram = f"""
✨ Meet {product_name} by {brand_name} ✨

Your skincare routine deserves something special. 🤍

Designed for {target_audience}, {product_name} is a
{category.lower()} created to provide:

✨ {benefits}

Simple routine.
Thoughtful skincare.
Beautiful results. 🌸

Our {campaign_objective.lower()} campaign is all about
making skincare feel {tone.lower()} and easy to enjoy.

Ready to make {product_name} part of your routine?

{cta}! ✨

#Skincare #Beauty #SelfCare #Glow
#SkincareRoutine #HealthySkin
"""

            st.subheader("📸 Instagram Caption")

            st.text_area(
                "Generated Instagram Caption",
                instagram,
                height=350
            )


        # -----------------------------------
        # TAGLINE
        # -----------------------------------

        elif content_type == "🏷️ Tagline":

            tagline = (
                f"{brand_name} – "
                f"Where Better Skincare Begins."
            )

            st.subheader("🏷️ Tagline")

            st.success(tagline)