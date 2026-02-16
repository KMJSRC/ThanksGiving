import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import os

st.set_page_config(page_title="AI Workshop Thanksgiving Card", layout="centered")

st.title("AI Workshop Thanksgiving Card Generator")
st.write("Click the button below to generate the greeting card.")


# ---------------- SAFE FONT FUNCTION ----------------
def get_font(size, bold=False):
    try:
        if bold:
            return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", size)
        else:
            return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", size)
    except:
        return ImageFont.load_default()


def create_card():
    card_width = 1000
    card_height = 1500

    card = Image.new("RGB", (card_width, card_height), (255, 255, 255))
    draw = ImageDraw.Draw(card)

    # ---------------- FONT SIZES (INCREASED) ----------------
    title_font = get_font(35, bold=True)   # Bigger title
    text_font = get_font(28)              # Bigger main text
    small_font = get_font(25)             # Bigger list text
    footer_font = get_font(20)            # Footer text

    y = 20

    # ---------------- LOGO ----------------
    if os.path.exists("logo.jpeg"):
        logo = Image.open("logo.jpeg").convert("RGB")
        logo = logo.resize((900, 220))
        card.paste(logo, ((card_width - 900) // 2, y))
        y += 250
    else:
        draw.text((20, y), "logo.jpeg missing", fill="red", font=text_font)
        y += 50

    # ---------------- TITLE (CENTER) ----------------
    title = "AI Workshop Thanksgiving Card"
    bbox = draw.textbbox((0, 0), title, font=title_font)
    title_width = bbox[2] - bbox[0]
    draw.text(((card_width - title_width) // 2, y), title, fill="darkblue", font=title_font)
    y += 80

    # ---------------- PHOTOS ----------------
    photos = ["BS.jpg", "VK.jpg", "RRK.jpg"]
    photo_size = (240, 260)
    spacing = 50
    total_width = 3 * photo_size[0] + 2 * spacing
    start_x = (card_width - total_width) // 2

    for i, p in enumerate(photos):
        x = start_x + i * (photo_size[0] + spacing)

        if os.path.exists(p):
            img = Image.open(p).convert("RGB").resize(photo_size)
            card.paste(img, (x, y))
        else:
            draw.rectangle([x, y, x + photo_size[0], y + photo_size[1]], outline="black", width=3)
            draw.text((x + 60, y + 120), "Missing", fill="red", font=small_font)

    y += photo_size[1] + 50

    # ---------------- MESSAGE ----------------
    thanks_text = (
        "Respected Dean-SRC, Organizer-HOD, and Resource Person,\n\n"
        "We sincerely thank you for permitting, organizing and delivering a wonderful\n"
        "and highly informative AI Workshop on 14.02.1026.\n\n"
        "Your valuable insights and guidance motivated us to explore AI\n"
        "applications in Academics, and Research.\n\n"
        "We truly appreciate your great support and efforts."
    )

    draw.multiline_text((80, y), thanks_text, fill="black", font=text_font, spacing=12)
    y += 350

    # ---------------- EXPECTATIONS ----------------
    draw.text((80, y), "Participants' Expectations:", fill="darkgreen", font=title_font)
    y += 60

    expectations = (
        "1. More hands-on sessions using AI tools\n"
        "2. Practical training on ML and Deep Learning\n"
        "3. Real-time project demonstrations\n"
        "4. More examples on AI applications in research\n"
    )

    draw.multiline_text((100, y), expectations, fill="black", font=small_font, spacing=25)

    # ---------------- FOOTER ----------------
    footer = "With Regards,\nWorkshop Participants-KMJ, CSE/SRC"
    draw.multiline_text((680, 1380), footer, fill="darkred", font=footer_font, spacing=10)

    return card


# ---------------- BUTTON ----------------
if st.button("Generate Thanksgiving Card"):
    card_image = create_card()
    st.image(card_image, caption="Generated Greeting Card", use_column_width=True)












