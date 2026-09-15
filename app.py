import streamlit as st
import base64
import random


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Skincare Marketing Generator",
    page_icon="🫧",
    layout="centered"
)


# ============================================================
# BACKGROUND
# ============================================================

def set_background(image_file):

    with open(image_file, "rb") as file:
        encoded = base64.b64encode(file.read()).decode()

    st.markdown(
        f"""
        <style>

        .stApp {{
            background-color: #EAF6FF;
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}

        .stTextInput input {{
            background-color: white !important;
            color: black !important;
        }}

        .stTextArea textarea {{
            background-color: white !important;
            color: black !important;
        }}

        div[data-testid="stSelectbox"] [data-baseweb="select"],
        div[data-testid="stSelectbox"] [data-baseweb="select"] > div,
        div[data-testid="stSelectbox"] [data-baseweb="base-input"],
        div[data-testid="stSelectbox"] [data-baseweb="input"],
        div[data-testid="stSelectbox"] [role="combobox"] {{
            background-color: #FFFFFF !important;
            background: #FFFFFF !important;
        }}

        div[data-testid="stSelectbox"] [data-baseweb="select"] span {{
            color: #222222 !important;
        }}

        div[data-testid="stSelectbox"] [data-baseweb="select"] svg {{
            fill: #222222 !important;
        }}

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


# ============================================================
# TITLE
# ============================================================

st.image(
    "skincare_banner.png.png",
    use_container_width=True
)

st.title("🫧 Skincare Marketing Content Generator")

st.write(
    "Create creative, platform-specific marketing content "
    "for your skincare brand."
)


# ============================================================
# BRAND INFORMATION
# ============================================================

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


# ============================================================
# CATEGORY
# ============================================================

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


# ============================================================
# ADDITIONAL INFORMATION
# ============================================================

additional_info = st.text_area(
    "💡 Anything else you'd like us to know? (Optional)",
    placeholder=(
        "Example: Vegan, cruelty-free, launching during Diwali, "
        "perfect for busy college students... "
        "If you selected 'Other' as the product category, "
        "you can describe your product here."
    )
)


# ============================================================
# HANDLE NA / NOTHING
# ============================================================

no_info_values = {
    "",
    "na",
    "n/a",
    "n.a.",
    "n a",
    "none",
    "nothing",
    "nothing else",
    "no",
    "not applicable",
    "no additional information"
}

if additional_info.strip().lower() in no_info_values:
    additional_info = ""


# ============================================================
# CAMPAIGN SETTINGS
# ============================================================

st.subheader("📋 Campaign Details")

campaign_objective = st.selectbox(
    "What is the campaign objective?",
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


# ============================================================
# CREATIVITY LEVEL
# ============================================================

st.subheader("✨ Creativity Level")

creativity_level = st.select_slider(
    "How creative should your content be?",
    options=[
        "Simple",
        "Balanced",
        "Highly Creative"
    ],
    value="Balanced"
)


# ============================================================
# CONTACT INFORMATION
# ============================================================

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


# ============================================================
# CONTENT TYPE
# ============================================================

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


# ============================================================
# SMART INFORMATION UNDERSTANDING
# ============================================================

def understand_additional_info(text):

    text = text.lower()

    information = {
        "attributes": [],
        "campaign_context": [],
        "audience_context": [],
        "preferences": [],
        "general": []
    }

    # --------------------------------------------------------
    # PRODUCT ATTRIBUTES
    # --------------------------------------------------------

    attribute_keywords = {
        "vegan": "vegan",
        "cruelty free": "cruelty-free",
        "cruelty-free": "cruelty-free",
        "organic": "organic",
        "natural": "natural",
        "dermatologist": "dermatologist-related positioning",
        "eco friendly": "eco-friendly",
        "eco-friendly": "eco-friendly",
        "recyclable": "recyclable packaging",
        "sustainable": "sustainability"
    }

    for keyword, meaning in attribute_keywords.items():

        if keyword in text:
            information["attributes"].append(meaning)


    # --------------------------------------------------------
    # CAMPAIGN CONTEXT
    # --------------------------------------------------------

    campaign_keywords = {
        "diwali": "Diwali",
        "holi": "Holi",
        "christmas": "Christmas",
        "valentine": "Valentine's Day",
        "new year": "New Year",
        "birthday": "birthday",
        "launch": "product launch",
        "festival": "festive campaign"
    }

    for keyword, meaning in campaign_keywords.items():

        if keyword in text:
            information["campaign_context"].append(meaning)


    # --------------------------------------------------------
    # AUDIENCE CONTEXT
    # --------------------------------------------------------

    audience_keywords = {
        "college student": "college students",
        "college students": "college students",
        "student": "students",
        "students": "students",
        "working professional": "working professionals",
        "working professionals": "working professionals",
        "teenager": "teenagers",
        "teenagers": "teenagers",
        "young adult": "young adults",
        "young adults": "young adults",
        "busy": "busy consumers"
    }

    for keyword, meaning in audience_keywords.items():

        if keyword in text:
            information["audience_context"].append(meaning)


    # --------------------------------------------------------
    # CUSTOMER NEEDS / PREFERENCES
    # --------------------------------------------------------

    preference_keywords = {
        "sensitive skin": "sensitive-skin concerns",
        "dry skin": "dry-skin concerns",
        "oily skin": "oily-skin concerns",
        "acne": "acne-related concerns",
        "simple routine": "preference for a simple routine",
        "quick": "preference for a quick routine",
        "affordable": "affordability",
        "budget": "budget-conscious consumers",
        "not expensive": "affordability"
    }

    for keyword, meaning in preference_keywords.items():

        if keyword in text:
            information["preferences"].append(meaning)


    # --------------------------------------------------------
    # IF USER SELECTED OTHER
    # --------------------------------------------------------

    if category == "Other" and text.strip():

        information["general"].append(
            "User-defined product category/details"
        )


    # --------------------------------------------------------
    # REMOVE DUPLICATES
    # --------------------------------------------------------

    for key in information:
        information[key] = list(dict.fromkeys(information[key]))

    return information


# ============================================================
# CAMPAIGN IDEA GENERATOR
# ============================================================

def create_campaign_idea():

    info = understand_additional_info(additional_info)

    context = []

    if info["attributes"]:
        context.append(
            "Key product attributes: "
            + ", ".join(info["attributes"])
        )

    if info["campaign_context"]:
        context.append(
            "Campaign context: "
            + ", ".join(info["campaign_context"])
        )

    if info["audience_context"]:
        context.append(
            "Audience context: "
            + ", ".join(info["audience_context"])
        )

    if info["preferences"]:
        context.append(
            "Customer needs/preferences: "
            + ", ".join(info["preferences"])
        )

    if info["general"]:
        context.append(
            "Additional product details provided by user"
        )


    # --------------------------------------------------------
    # SELECT CAMPAIGN CONCEPT
    # --------------------------------------------------------

    if "Diwali" in info["campaign_context"]:

        campaign_name = f"✨ {product_name} – The Diwali Glow"

        big_idea = (
            f"Position {product_name} as part of a festive "
            f"self-care routine, connecting skincare with "
            f"the excitement of Diwali."
        )

        hook = (
            "This Diwali, let your skin join the celebration. ✨"
        )


    elif "college students" in info["audience_context"]:

        campaign_name = (
            f"🎓 {product_name} – Glow On The Go"
        )

        big_idea = (
            f"Show how {product_name} fits easily into the "
            f"busy lifestyle of college students."
        )

        hook = (
            "Busy schedule? Your skincare routine doesn't have to be."
        )


    elif "vegan" in info["attributes"]:

        campaign_name = (
            f"🌱 {product_name} – Beauty With Purpose"
        )

        big_idea = (
            f"Highlight the vegan positioning of {product_name} "
            f"while connecting skincare with conscious choices."
        )

        hook = (
            "Good skincare. Thoughtful choices."
        )


    elif campaign_objective == "🆕 Product Launch":

        campaign_name = f"✨ Meet {product_name}"

        big_idea = (
            f"Introduce {product_name} as a fresh skincare "
            f"solution designed specifically for "
            f"{target_audience}."
        )

        hook = (
            "Your new skincare essential has arrived."
        )


    elif campaign_objective == "🎉 Festive Campaign":

        campaign_name = "✨ Glow Into The Celebration"

        big_idea = (
            f"Connect {product_name} with festive self-care "
            f"and feel-good skincare moments."
        )

        hook = (
            "Celebrate every moment. Glow through every one."
        )


    elif campaign_objective == "🛍️ Promotional Sale":

        campaign_name = (
            f"🛍️ {product_name} – Your Glow, Your Deal"
        )

        big_idea = (
            f"Use an attractive promotional message to "
            f"encourage customers to discover {product_name} "
            f"and take advantage of the current offer."
        )

        hook = (
            "Your skincare upgrade just got even better."
        )


    elif campaign_objective == "💕 Customer Engagement":

        campaign_name = (
            f"💕 Get to Know Your Glow"
        )

        big_idea = (
            f"Create an engaging campaign that encourages "
            f"customers to connect with {brand_name} and "
            f"discover how {product_name} fits their routine."
        )

        hook = (
            "What's your skin's favourite part of the routine?"
        )


    else:

        campaign_name = (
            f"💙 The {product_name} Difference"
        )

        big_idea = (
            f"Focus on why {product_name} deserves a place "
            f"in the customer's everyday skincare routine."
        )

        hook = (
            "Skincare that fits into your everyday."
        )


    return {
        "name": campaign_name,
        "idea": big_idea,
        "hook": hook,
        "context": context
    }


# ============================================================
# CONTENT GENERATOR
# ============================================================

def generate_content(version, campaign):

    info = understand_additional_info(additional_info)

    extra_text = ""

    if info["attributes"]:
        extra_text += (
            "Key attributes: "
            + ", ".join(info["attributes"])
            + ". "
        )

    if info["campaign_context"]:
        extra_text += (
            "Campaign context: "
            + ", ".join(info["campaign_context"])
            + ". "
        )

    if info["audience_context"]:
        extra_text += (
            "Audience context: "
            + ", ".join(info["audience_context"])
            + ". "
        )

    if info["preferences"]:
        extra_text += (
            "Customer needs: "
            + ", ".join(info["preferences"])
            + ". "
        )

    # If Other is selected and the user described the product,
    # use that description in the generated content.

    product_category_text = category.lower()

    if category == "Other" and additional_info.strip():

        product_category_text = (
            "specialized skincare product described by the user"
        )


    # ========================================================
    # VERSION OPENINGS
    # ========================================================

    if version == 1:

        opening = campaign["hook"]


    elif version == 2:

        opening = (
            f"What if your skincare routine could make "
            f"every day feel a little better?"
        )


    else:

        opening = (
            f"✨ Your skin has a story. "
            f"{product_name} is ready to be part of it."
        )


    # ========================================================
    # CREATIVITY LEVEL
    # ========================================================

    if creativity_level == "Simple":

        style = "clear, simple and professional"


    elif creativity_level == "Balanced":

        style = "engaging, warm and creative"


    else:

        style = "bold, memorable, emotional and highly creative"


    # ========================================================
    # MARKETING EMAIL
    # ========================================================

    if content_type == "💌 Marketing Email":

        subject_options = [
            f"Discover {product_name} by {brand_name}",
            f"Meet your new skincare essential: {product_name}",
            f"✨ It's time to discover {product_name}"
        ]

        subject = subject_options[version - 1]

        return f"""
Subject: {subject}

Dear Customer,

{opening}

We are excited to introduce {product_name}, a
{product_category_text} from {brand_name}.

Designed especially for {target_audience},
{product_name} helps provide {benefits}.

{extra_text}

Why you'll love {product_name}:

✨ {benefits}

Our {campaign_objective.lower()} campaign brings a
{style} approach to skincare.

{cta} and discover what {brand_name} has to offer.

Warm regards,

{contact_person}
{contact_role}
{brand_name}

Email: {contact_email}
Phone: {contact_phone}
"""


    # ========================================================
    # LINKEDIN POST
    # ========================================================

    elif content_type == "💼 LinkedIn Post":

        return f"""
✨ {opening}

Introducing {product_name} by {brand_name}.

At {brand_name}, we believe skincare should be
meaningful, accessible and easy to make part of
everyday life.

Our {product_category_text} is designed especially for
{target_audience} and provides {benefits}.

{extra_text}

Campaign idea:

{campaign["name"]}

{campaign["idea"]}

Our goal is to create skincare experiences that
connect with today's consumers.

{cta} and discover {product_name}.

#Skincare #Beauty #Marketing #SelfCare
#{brand_name.replace(" ", "")}
"""


    # ========================================================
    # INSTAGRAM CAPTION
    # ========================================================

    elif content_type == "📸 Instagram Caption":

        hashtags = (
            "#Skincare #Beauty #Glow #SelfCare "
            "#SkincareRoutine #HealthySkin"
        )

        return f"""
✨ {opening} ✨

Meet {product_name} by {brand_name}. 🤍

Your skincare routine deserves something special.

Designed for {target_audience},

✨ {benefits}

{extra_text}

Simple routine.
Thoughtful skincare.
Beautiful results. 🌸

{cta}! ✨

{hashtags}
"""


    # ========================================================
    # TAGLINE
    # ========================================================

    else:

        taglines = [

            f"{brand_name} – Better Skin Starts Here.",

            f"{product_name} – Your Skin's New Essential.",

            f"{brand_name} – Skincare Made to Stand Out."
        ]

        return taglines[version - 1]


# ============================================================
# GENERATE BUTTON
# ============================================================

if st.button(
    "🚀 Generate Content",
    use_container_width=True
):

    if (
        not brand_name.strip()
        or not product_name.strip()
        or not target_audience.strip()
        or not benefits.strip()
        or not contact_person.strip()
        or not contact_email.strip()
    ):

        st.warning(
            "Please fill in all the required fields marked with *."
        )


    else:

        campaign = create_campaign_idea()

        st.session_state["campaign"] = campaign

        # ----------------------------------------------------
        # CAMPAIGN IDEA
        # ----------------------------------------------------

        st.subheader("💡 AI-Inspired Campaign Idea")

        st.success(
            campaign["name"]
        )

        st.write(
            "**Big Idea:** "
            + campaign["idea"]
        )

        st.write(
            "**Creative Hook:** "
            + campaign["hook"]
        )


        # ----------------------------------------------------
        # SMART UNDERSTANDING
        # ----------------------------------------------------

        info = understand_additional_info(additional_info)

        if additional_info:

            st.subheader("🧠 What We Understood")

            if info["attributes"]:
                st.write(
                    "🏷️ **Product attributes:** "
                    + ", ".join(info["attributes"])
                )

            if info["campaign_context"]:
                st.write(
                    "🎉 **Campaign context:** "
                    + ", ".join(info["campaign_context"])
                )

            if info["audience_context"]:
                st.write(
                    "👥 **Audience context:** "
                    + ", ".join(info["audience_context"])
                )

            if info["preferences"]:
                st.write(
                    "💡 **Customer needs:** "
                    + ", ".join(info["preferences"])
                )

            if category == "Other":
                st.write(
                    "📦 **Product category:** "
                    "Other — using your description as additional "
                    "product information."
                )


        # ----------------------------------------------------
        # THREE VERSIONS
        # ----------------------------------------------------

        st.subheader("✨ Choose Your Version")

        version_1 = generate_content(
            1,
            campaign
        )

        version_2 = generate_content(
            2,
            campaign
        )

        version_3 = generate_content(
            3,
            campaign
        )

        st.session_state["versions"] = [
            version_1,
            version_2,
            version_3
        ]


# ============================================================
# DISPLAY GENERATED VERSIONS
# ============================================================

if "versions" in st.session_state:

    versions = st.session_state["versions"]

    tabs = st.tabs(
        [
            "✨ Version 1",
            "💕 Version 2",
            "🔥 Version 3"
        ]
    )

    for i, tab in enumerate(tabs):

        with tab:

            st.text_area(
                f"Generated {content_type}",
                versions[i],
                height=400,
                key=f"version_{i}"
            )


# ============================================================
# REGENERATE / IMPROVE
# ============================================================

if "versions" in st.session_state:

    st.divider()

    st.subheader("🔄 Improve Your Content")

    improvement = st.selectbox(
        "What would you like to change?",
        [
            "Make it more catchy",
            "Make it more emotional",
            "Make it more professional",
            "Make it more luxurious",
            "Make it more persuasive",
            "Make it shorter",
            "Make it more playful",
            "Create a completely new version"
        ]
    )


    if st.button(
        "🔄 Regenerate",
        use_container_width=True
    ):

        campaign = st.session_state.get(
            "campaign",
            create_campaign_idea()
        )

        # ----------------------------------------------------
        # SELECT ONE EXISTING VERSION
        # ----------------------------------------------------

        base_version = random.choice(
            st.session_state["versions"]
        )


        # ----------------------------------------------------
        # IMPROVEMENT OPTIONS
        # ----------------------------------------------------

        if improvement == "Make it more catchy":

            catchy_openings = [
                f"✨ Your glow called. It wants {product_name}.",
                f"Ready to make your skincare routine unforgettable?",
                f"Your next skincare obsession has arrived. ✨"
            ]

            improved = (
                random.choice(catchy_openings)
                + "\n\n"
                + base_version
            )


        elif improvement == "Make it more emotional":

            emotional_openings = [
                "Because your skin deserves a little extra love. 🤍",
                "Take a moment to care for the skin you live in.",
                "Self-care starts with giving yourself a little attention. ✨"
            ]

            improved = (
                random.choice(emotional_openings)
                + "\n\n"
                + base_version
            )


        elif improvement == "Make it more professional":

            professional_intro = (
                f"{brand_name} presents {product_name}, "
                f"a thoughtfully positioned "
                f"{category.lower()} designed for "
                f"{target_audience}."
            )

            improved = (
                professional_intro
                + "\n\n"
                + base_version
            )


        elif improvement == "Make it more luxurious":

            luxury_openings = [
                f"✨ Elevate your everyday skincare ritual with {product_name}.",
                f"Experience skincare designed to feel as exceptional as it performs.",
                f"Discover a more refined approach to everyday skincare."
            ]

            improved = (
                random.choice(luxury_openings)
                + "\n\n"
                + base_version
            )


        elif improvement == "Make it more persuasive":

            persuasive_openings = [
                f"Why settle for an ordinary routine when you can discover {product_name}?",
                f"Give your skincare routine the upgrade it deserves.",
                f"Your next skincare essential could be {product_name}."
            ]

            improved = (
                random.choice(persuasive_openings)
                + "\n\n"
                + base_version
            )


        elif improvement == "Make it shorter":

            lines = base_version.splitlines()

            useful_lines = []

            for line in lines:

                if line.strip():

                    useful_lines.append(line.strip())

            improved = "\n\n".join(
                useful_lines[:8]
            )


        elif improvement == "Make it more playful":

            playful_openings = [
                f"✨ Psst... your skincare routine just got more exciting!",
                f"Glow mode: ON. ✨",
                f"Good skin days are calling! 📞✨"
            ]

            improved = (
                random.choice(playful_openings)
                + "\n\n"
                + base_version
            )


        else:

            new_version_number = random.randint(1, 3)

            improved = generate_content(
                new_version_number,
                campaign
            )


        # ----------------------------------------------------
        # DISPLAY REGENERATED CONTENT
        # ----------------------------------------------------

        st.subheader("✨ Regenerated Content")

        st.text_area(
            "Improved Version",
            improved,
            height=450,
            key="regenerated_content"
        )

        st.success(
            "Your content has been regenerated successfully!"
        )


# ============================================================
# FOOTER
# ============================================================

 st.success(
            "Your content has been regenerated successfully!"
        )