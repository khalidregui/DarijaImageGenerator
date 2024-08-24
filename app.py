from openai import OpenAI
import streamlit as st
from streamlit_carousel import carousel
from api_key import openai_api_key
client = OpenAI(api_key=openai_api_key)


# darija to prompt
def darija_to_prompt(text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"generate a short English prompt from this moroccan darija text ({text}) to give it to a model to generate an image\nmake sure to return just the prompt"}
        ]
    )
    return response.choices[0].message.content




# Initialize your image generation client
single_img=dict(
    title = "",
    text="",
    interval=None,
    img=""
)

def generate_images(image_description, num_images):
    image_gallery=[]
    for i in range (num_images):
        response = client.images.generate(
            model="dall-e-3",
            prompt=image_description,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        image_url = response.data[0].url
        new_image=single_img.copy()
        new_image["title"]=''
        new_image["text"]=''
        new_image["img"]=image_url
        image_gallery.append(new_image)
    return image_gallery



st.set_page_config(
    page_title="RGK-Image-Generation",
    page_icon=":camera:",
    layout="wide"
    )

# craete a title
st.title("RGK Image Generation Tool")

# create a subheader
st.subheader("Powered by RGK")
img_description = st.text_input("Dkhl wasef l sora li bghiti tsayb : ")
num_of_images = st.number_input("khtar ch7la nta3 tsawr bghity tsayb : ", min_value=1, max_value=4, value=1)

# create a button
if st.button("Sawb tswira (tsawr)"):
    img_description = darija_to_prompt(img_description)
    generate_image=generate_images(img_description, num_of_images)
    # st.write("first image")
    # st.image(generate_image)
    carousel(items=generate_image, width=0.8)
    





