import streamlit as st
import requests

# 🔑 Your API Key
API_KEY = "aaa919944e404eef93423b23da72ee92"

st.set_page_config(page_title="Grimoire", layout="centered")

st.title("🧙 Grimoire")
st.write("Find recipes using your ingredients")

ingredients = st.text_input("Enter ingredients (comma separated):")

if st.button("Find Recipes"):

    if ingredients.strip() == "":
        st.warning("Please enter ingredients")
    else:
        url = "https://api.spoonacular.com/recipes/findByIngredients"

        params = {
            "ingredients": ingredients,
            "number": 6,
            "apiKey": API_KEY
        }

        response = requests.get(url, params=params)
        data = response.json()

        if "status" in data:
            st.error("API limit reached or invalid key ❌")
        elif len(data) == 0:
            st.error("No recipes found 😢")
        else:
            st.subheader("🍽 Recipes")

            for recipe in data:
                st.image(recipe["image"])
                st.write(f"**{recipe['title']}**")