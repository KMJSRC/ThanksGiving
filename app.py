import gradio as gr
from PIL import Image, ImageDraw, ImageFont
import os

def create_card():
    card_width = 1000
    card_height = 1200
    card = Image.new("RGB", (card_width, card_height), (255, 255, 255))
    draw = ImageDraw.Draw(card)

    # Use default fonts (safe for HuggingFace)
    title_font = ImageFont.load_default()
    text_font = ImageFont.load_default()
    small_font = ImageFont.load_default()

    y = 20

    # Logo
    if os.path.exists("logo.jpeg"):
        logo = Image.open("logo.jpeg").convert("RGB")
        logo = logo.resize((800, 200))
        card.paste(logo, ((card_width - 800) // 2, y))
        y += 230
    else:
        draw.text((20, y), "logo.jpeg missing", fill="red", font=text_font)
        y += 50

    # Title
    title = "AI Workshop Thanksgiving Card"
    draw.text((250, y), title, fill="darkblue", font=title_font)
    y += 60

    # Photos
    photos = ["BS.jpg", "VK.jpg", "RRK.jpg"]
    photo_size = (220, 220)
    spacing = 40
    total_width = 3 * photo_size[0] + 2 * spacing
    start_x = (card_width - total_width) // 2

    for i, p in enumerate(photos):
        x = start_x + i * (photo_size[0] + spacing)
        if os.path.exists(p):
            img = Image.open(p).convert("RGB").resize(photo_size)
            card.paste(img, (x, y))
        else:
            draw.rectangle([x, y, x + photo_size[0], y + photo_size[1]], outline="black", width=3)
            draw.text((x + 60, y + 100), "Missing", fill="red", font=small_font)

    y += 260

    # Message
    thanks_text = (
        "Respected Dean, Organizer, and Resource Person,\n\n"
        "We sincerely thank you for organizing and delivering a wonderful\n"
        "and highly informative AI Workshop.\n\n"
        "Your valuable insights and guidance motivated us to explore AI\n"
        "applications in academics, research, and industry.\n\n"
        "We truly appreciate your great support and efforts."
    )
    draw.multiline_text((80, y), thanks_text, fill="black", font=text_font, spacing=10)
    y += 350

    # Expectations
    draw.text((80, y), "Participants' Expectations:", fill="darkgreen", font=title_font)
    y += 40

    expectations = (
        "1. More hands-on sessions using AI tools\n"
        "2. Practical training on ML and Deep Learning\n"
        "3. Real-time project demonstrations\n"
        "4. More examples on AI applications in research\n"
        "5. More time for interactive Q&A sessions"
    )
    draw.multiline_text((100, y), expectations, fill="black", font=small_font, spacing=8)

    # Footer
    footer = "With Regards,\nWorkshop Participants"
    draw.multiline_text((700, 1100), footer, fill="darkred", font=small_font, spacing=6)

    # IMPORTANT: Save and return file path (best for HuggingFace)
    output_path = "generated_card.png"
    card.save(output_path)

    return output_path


with gr.Blocks() as demo:
    gr.Markdown("<h1 style='text-align:center;'>AI Workshop Thanksgiving Card Generator</h1>")
    gr.Markdown("Click the button below to generate the greeting card.")

    btn = gr.Button("Generate Thanksgiving Card")

    output_img = gr.Image(label="Generated Greeting Card")

    btn.click(fn=create_card, inputs=[], outputs=output_img)

demo.launch()
