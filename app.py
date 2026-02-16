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
    card_width = 1200
    card_height = 1750

    # Light background (soft decoration)
    card = Image.new("RGB", (card_width, card_height), (248, 248, 255))
    draw = ImageDraw.Draw(card)

    # ---------------- COLORS ----------------
    gold = (184, 134, 11)
    dark_blue = (0, 0, 139)
    light_gray = (220, 220, 220)

    # ---------------- DECORATIVE BORDER ----------------
    draw.rectangle([10, 10, card_width - 10, card_height - 10], outline=gold, width=8)
    draw.rectangle([25, 25, card_width - 25, card_height - 25], outline=dark_blue, width=3)

    # ---------------- FONT SIZES ----------------
    title_font = get_font(40, bold=True)
    sub_font = get_font(32, bold=True)
    text_font = get_font(26)
    small_font = get_font(24)
    footer_font = get_font(22)

    y = 40

    # ---------------- LOGO ----------------
    if os.path.exists("logo.jpeg"):
        logo = Image.open("logo.jpeg").convert("RGB")

        # Maintain aspect ratio
        max_logo_width = 920
        ratio = max_logo_width / logo.width
        new_w = int(logo.width * ratio)
        new_h = int(logo.height * ratio)

        logo = logo.resize((new_w, new_h))
        x_logo = (card_width - new_w) // 2

        card.paste(logo, (x_logo, y))
        y += new_h + 30
    else:
        draw.text((40, y), "logo.jpeg missing", fill="red", font=text_font)
        y += 60

    # ---------------- TITLE ----------------
    title = "AI Workshop Thanksgiving Card"
    bbox = draw.textbbox((0, 0), title, font=title_font)
    title_width = bbox[2] - bbox[0]
    title_x = (card_width - title_width) // 2

    draw.text((title_x, y), title, fill=dark_blue, font=title_font)

    # Decorative underline
    draw.line((title_x, y + 55, title_x + title_width, y + 55), fill=gold, width=5)
    y += 100

    # ---------------- PHOTOS ----------------
    photos = ["BS.jpg", "VK.jpg", "RRK.jpg"]
    photo_size = (240, 280)
    spacing = 60

    total_width = 3 * photo_size[0] + 2 * spacing
    start_x = (card_width - total_width) // 2

    for i, p in enumerate(photos):
        x = start_x + i * (photo_size[0] + spacing)

        if os.path.exists(p):
            img = Image.open(p).convert("RGB").resize(photo_size)

            # Shadow
            shadow_offset = 6
            draw.rectangle(
                [x + shadow_offset, y + shadow_offset,
                 x + photo_size[0] + shadow_offset, y + photo_size[1] + shadow_offset],
                fill=light_gray
            )

            # Paste photo
            card.paste(img, (x, y))

            # Photo frame
            draw.rectangle([x - 4, y - 4, x + photo_size[0] + 4, y + photo_size[1] + 4],
                           outline=dark_blue, width=4)

        else:
            draw.rectangle([x, y, x + photo_size[0], y + photo_size[1]], outline="black", width=3)
            draw.text((x + 60, y + 120), "Missing", fill="red", font=small_font)

    y += photo_size[1] + 60

    # ---------------- MESSAGE BOX ----------------
    box1_top = y
    box1_bottom = y + 380

    draw.rounded_rectangle(
        [60, box1_top, card_width - 60, box1_bottom],
        radius=25, outline=dark_blue, width=4, fill=(255, 255, 255)
    )

    thanks_text = (
        "Respected Dean-SRC, Organizer-HOD, and Resource Person,\n\n"
        "We sincerely thank you for permitting, organizing and delivering a wonderful\n"
        "and highly informative AI Workshop on 14.02.2026.\n\n"
        "Your valuable insights and guidance motivated us to explore AI\n"
        "applications in Academics, and Research.\n\n"
        "We truly appreciate your great support and efforts."
    )

    draw.multiline_text((100, y + 25), thanks_text, fill="black", font=text_font, spacing=12)
    y += 430

    # ---------------- EXPECTATIONS TITLE ----------------
    draw.text((80, y), "Participants' Expectations:", fill="darkgreen", font=sub_font)
    y += 60

    # ---------------- EXPECTATIONS BOX ----------------
    box2_top = y
    box2_bottom = y + 240

    draw.rounded_rectangle(
        [60, box2_top, card_width - 60, box2_bottom],
        radius=25, outline="darkgreen", width=4, fill=(255, 255, 255)
    )

    expectations = (
        "1. More hands-on sessions using AI tools\n"
        "2. Practical training on ML, DL and mainly on XAI\n"
        "3. Real-time project demonstrations\n"
        "4. More examples on AI applications in research"
    )

    draw.multiline_text((100, y + 25), expectations, fill="black", font=small_font, spacing=18)

    # ---------------- FOOTER ----------------
    footer = "With Regards,\nWorkshop Participants-KMJ, CSE/SRC"

    footer_bbox = draw.multiline_textbbox((0, 0), footer, font=footer_font, spacing=8)
    footer_width = footer_bbox[2] - footer_bbox[0]

    footer_x = card_width - footer_width - 90
    footer_y = card_height - 150

    draw.multiline_text((footer_x, footer_y), footer, fill="darkred", font=footer_font, spacing=8)

    # Small decorative footer line
    draw.line((footer_x, footer_y - 10, footer_x + footer_width, footer_y - 10), fill=gold, width=3)

    return card


# ---------------- BUTTON ----------------
if st.button("Generate Thanksgiving Card"):
    card_image = create_card()
    st.image(card_image, caption="Generated Greeting Card", use_column_width=True)





