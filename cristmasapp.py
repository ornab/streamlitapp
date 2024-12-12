import streamlit as st
from datetime import datetime
from gtts import gTTS
from io import BytesIO
from PIL import Image

# Set the page configuration
st.set_page_config(
    page_title="Christmas Countdown App",
    page_icon="🎄",
    layout="centered",
)

# Title and Welcome Message
st.title("🎅 Welcome to the Christmas Countdown! 🎄")
st.write("Let's get ready for the most wonderful time of the year!")

# Calculate days left for Christmas
today = datetime.now()
christmas = datetime(today.year, 12, 25)
if today > christmas:  # If today's date is after Christmas, calculate for next year
    christmas = datetime(today.year + 1, 12, 25)
days_left = (christmas - today).days

# Display days left for Christmas
st.subheader(f"🌟 Only {days_left} days left until Christmas! 🌟")

# Display a Christmas tree image
image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Christmas_tree.svg/2048px-Christmas_tree.svg.png"
image = Image.open(requests.get(image_url, stream=True).raw)
st.image(image, caption="🎄 Christmas Tree 🎄", use_column_width=True)

# Generate and Play Voice Message
message = f"There are only {days_left} days left until Christmas!"
tts = gTTS(message)
audio_file = BytesIO()
tts.write_to_fp(audio_file)
audio_file.seek(0)

# Audio Player
st.audio(audio_file, format="audio/mp3")

