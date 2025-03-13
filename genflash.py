# # # # # # import streamlit as st
# # # # # # import os
# # # # # # import json
# # # # # # import google.generativeai as genai  # Gemini AI SDK

# # # # # # # Set API Key directly (replace with your actual API key)
# # # # # # API_KEY = "AIzaSyCcg8tjDwKVLLrgk95fKWXyJKz5uhWLxqE"  # Make sure to replace this!
# # # # # # genai.configure(api_key=API_KEY)

# # # # # # # List all available models to check which one exists
# # # # # # models = genai.list_models()
# # # # # # available_models = [model.name for model in models]
# # # # # # st.write("Available Models:", available_models)  # Debugging: Shows available models in Streamlit

# # # # # # # Use the correct model name (adjust based on available models)
# # # # # # MODEL_NAME = "gemini-1.0-pro"  # Default
# # # # # # if "models/gemini-1.5-pro" in available_models:
# # # # # #     MODEL_NAME = "gemini-1.5-pro"

# # # # # # st.title(":rainbow[Flashcard Maker]")

# # # # # # message = st.text_area("Enter your text to generate flashcards", height=200)

# # # # # # def generate_flashcards(text):
# # # # # #     """Generates flashcards using Gemini API."""
# # # # # #     PROMPT_TEMPLATE = f"""
# # # # # #     You are an AI that creates concise one-liner flashcards based on a given text. 
# # # # # #     Generate exactly 5 flashcards in the following JSON format:
    
# # # # # #     {{
# # # # # #       "flashcards": [
# # # # # #         {{"question": "What is ...?", "answer": "Definition of ..."}},
# # # # # #         {{"question": "How does ... work?", "answer": "It works by ..."}},
# # # # # #         {{"question": "Why is ... important?", "answer": "Because ..."}},
# # # # # #         {{"question": "What are the benefits of ...?", "answer": "The benefits are ..."}},
# # # # # #         {{"question": "Explain ... briefly.", "answer": "It means ..."}}
# # # # # #       ]
# # # # # #     }}
    
# # # # # #     Text: {text}
# # # # # #     """

# # # # # #     model = genai.GenerativeModel(MODEL_NAME)  # Uses the correct model
# # # # # #     response = model.generate_content(PROMPT_TEMPLATE)

# # # # # #     try:
# # # # # #         extracted_response = response.text.strip()  # Extract text response
# # # # # #         parsed_response = json.loads(extracted_response)
# # # # # #         return parsed_response.get("flashcards", [])
# # # # # #     except json.JSONDecodeError:
# # # # # #         st.error("Failed to generate valid flashcards. Please try again.")
# # # # # #         return []

# # # # # # if st.button("Generate Flashcards"):
# # # # # #     if message.strip():
# # # # # #         flashcards = generate_flashcards(message)
        
# # # # # #         if flashcards:
# # # # # #             st.session_state["flashcards"] = flashcards  # Store flashcards in session
# # # # # #             st.success("Flashcards generated! See below.")

# # # # # # if "flashcards" in st.session_state:
# # # # # #     st.subheader("Your Flashcards:")
# # # # # #     for flashcard in st.session_state["flashcards"]:
# # # # # #         st.write(f"**Q:** {flashcard['question']}")
# # # # # #         st.write(f"**A:** {flashcard['answer']}")
# # # # # #         st.markdown("---")

# # # # # #     flashcards_text = "\n\n".join(
# # # # # #         f"Q: {fc['question']}\nA: {fc['answer']}" for fc in st.session_state["flashcards"]
# # # # # #     )

# # # # # #     st.download_button(
# # # # # #         label="Download Flashcards",
# # # # # #         data=flashcards_text,
# # # # # #         file_name="flashcards.txt",
# # # # # #         type="primary",
# # # # # #     )
# # # import streamlit as st
# # # import os
# # # import json
# # # from dotenv import load_dotenv
# # # import google.generativeai as genai  # Gemini AI SDK

# # # # ✅ Load environment variables
# # # load_dotenv()
# # # API_KEY = os.getenv("GEMINI_API_KEY")

# # # if not API_KEY:
# # #     st.error("❌ API Key not found! Check your .env file or manually set it.")
# # #     st.stop()  # Stop execution if API key is missing

# # # # ✅ Configure Gemini API
# # # genai.configure(api_key=API_KEY)

# # # # ✅ Check available models
# # # available_models = [model.name for model in genai.list_models()]
# # # if "models/gemini-1.5-pro" in available_models:
# # #     MODEL_NAME = "gemini-1.5-pro"
# # # elif "models/gemini-pro" in available_models:
# # #     MODEL_NAME = "gemini-pro"
# # # else:
# # #     st.error("❌ No valid Gemini model found! Check your API key.")
# # #     st.stop()

# # # st.title(":rainbow[Flashcard Maker]")

# # # message = st.text_area("Enter your text to generate flashcards", height=200)

# # # def generate_flashcards(text):
# # #     """Generates flashcards using Gemini API."""
# # #     PROMPT_TEMPLATE = f"""
# # #     You are an AI that creates concise one-liner flashcards based on a given text. 
# # #     Generate exactly 5 flashcards in **VALID JSON FORMAT** like this:

# # #     ```
# # #     {{
# # #       "flashcards": [
# # #         {{"question": "What is ...?", "answer": "Definition of ..."}},
# # #         {{"question": "How does ... work?", "answer": "It works by ..."}},
# # #         {{"question": "Why is ... important?", "answer": "Because ..."}},
# # #         {{"question": "What are the benefits of ...?", "answer": "The benefits are ..."}},
# # #         {{"question": "Explain ... briefly.", "answer": "It means ..."}}
# # #       ]
# # #     }}
# # #     ```

# # #     Text: {text}
# # #     """

# # #     model = genai.GenerativeModel(MODEL_NAME)
    
# # #     try:
# # #         response = model.generate_content(PROMPT_TEMPLATE)
# # #         st.write("✅ **RAW RESPONSE:**", response.text)  # Debugging
        
# # #         extracted_response = response.text.strip()  # Extract text response
# # #         parsed_response = json.loads(extracted_response)
        
# # #         return parsed_response.get("flashcards", [])
# # #     except json.JSONDecodeError:
# # #         st.error("❌ Failed to generate valid flashcards. Please try again.")
# # #         return []

# # # if st.button("Generate Flashcards"):
# # #     if message.strip():
# # #         flashcards = generate_flashcards(message)
        
# # #         if flashcards:
# # #             st.session_state["flashcards"] = flashcards  # Store flashcards in session
# # #             st.success("✅ Flashcards generated! See below.")

# # # if "flashcards" in st.session_state:
# # #     st.subheader("📌 Your Flashcards:")
# # #     for flashcard in st.session_state["flashcards"]:
# # #         st.write(f"**Q:** {flashcard['question']}")
# # #         st.write(f"**A:** {flashcard['answer']}")
# # #         st.markdown("---")

# # #     flashcards_text = "\n\n".join(
# # #         f"Q: {fc['question']}\nA: {fc['answer']}" for fc in st.session_state["flashcards"]
# # #     )

# # #     st.download_button(
# # #         label="📥 Download Flashcards",
# # #         data=flashcards_text,
# # #         file_name="flashcards.txt",
# # #         type="primary",
# # #     )
# # # # import streamlit as st
# # # # import os
# # # # import json
# # # # from dotenv import load_dotenv
# # # # import google.generativeai as genai  # Gemini AI SDK

# # # # # ✅ Load environment variables
# # # # load_dotenv()
# # # # API_KEY = os.getenv("GEMINI_API_KEY")

# # # # if not API_KEY:
# # # #     st.error("❌ API Key not found! Check your .env file or manually set it.")
# # # #     st.stop()

# # # # # ✅ Configure Gemini API
# # # # genai.configure(api_key=API_KEY)

# # # # # ✅ Select available model
# # # # try:
# # # #     available_models = [model.name for model in genai.list_models()]
# # # #     if "gemini-1.5-pro" in available_models:
# # # #         MODEL_NAME = "gemini-1.5-pro"
# # # #     elif "gemini-pro" in available_models:
# # # #         MODEL_NAME = "gemini-pro"
# # # #     else:
# # # #         st.error("❌ No valid Gemini model found! Check your API key.")
# # # #         st.stop()
# # # # except Exception as e:
# # # #     st.error(f"❌ Error fetching models: {e}")
# # # #     st.stop()

# # # # st.title(":rainbow[Flashcard Maker]")

# # # # message = st.text_area("Enter your text to generate flashcards", height=200)

# # # # def generate_flashcards(text):
# # # #     """Generates flashcards using Gemini API."""
# # # #     PROMPT_TEMPLATE = f"""
# # # #     You are an AI that creates flashcards in **VALID JSON FORMAT**. 

# # # #     **Example Output:**
# # # #     ```
# # # #     {{
# # # #       "flashcards": [
# # # #         {{"question": "What is Python?", "answer": "Python is a programming language."}},
# # # #         {{"question": "How does AI work?", "answer": "AI works by learning patterns from data."}},
# # # #         {{"question": "Why use functions?", "answer": "Functions improve code reusability."}},
# # # #         {{"question": "What is a loop?", "answer": "A loop is used to repeat a block of code."}},
# # # #         {{"question": "Explain recursion?", "answer": "Recursion is a function calling itself."}}
# # # #       ]
# # # #     }}
# # # #     ```

# # # #     **Now generate 5 flashcards for this text:**
# # # #     ```
# # # #     {text}
# # # #     ```
# # # #     """

# # # #     model = genai.GenerativeModel(MODEL_NAME)

# # # #     try:
# # # #         response = model.generate_content(PROMPT_TEMPLATE)
# # # #         extracted_response = response.text.strip()  
        
# # # #         # ✅ Try parsing JSON safely
# # # #         extracted_json = extracted_response[
# # # #             extracted_response.find("{") : extracted_response.rfind("}") + 1
# # # #         ]
# # # #         parsed_response = json.loads(extracted_json)

# # # #         return parsed_response.get("flashcards", [])
# # # #     except json.JSONDecodeError:
# # # #         st.error("❌ Failed to generate valid flashcards. Please try again.")
# # # #         st.write("📌 **Debugging Response:**", response.text)  # Debugging output
# # # #         return []
# # # #     except Exception as e:
# # # #         st.error(f"❌ Error: {e}")
# # # #         return []

# # # # if st.button("Generate Flashcards"):
# # # #     if message.strip():
# # # #         flashcards = generate_flashcards(message)
        
# # # #         if flashcards:
# # # #             st.session_state["flashcards"] = flashcards  # Store flashcards in session
# # # #             st.success("✅ Flashcards generated! See below.")

# # # # if "flashcards" in st.session_state:
# # # #     st.subheader("📌 Your Flashcards:")
# # # #     for flashcard in st.session_state["flashcards"]:
# # # #         st.write(f"**Q:** {flashcard['question']}")
# # # #         st.write(f"**A:** {flashcard['answer']}")
# # # #         st.markdown("---")

# # # #     flashcards_text = "\n\n".join(
# # # #         f"Q: {fc['question']}\nA: {fc['answer']}" for fc in st.session_state["flashcards"]
# # # #     )

# # # #     st.download_button(
# # # #         label="📥 Download Flashcards",
# # # #         data=flashcards


# # # # import streamlit as st
# # # # import os
# # # # import json
# # # # from dotenv import load_dotenv
# # # # import google.generativeai as genai  # Gemini AI SDK

# # # # # ✅ Load environment variables
# # # # load_dotenv()
# # # # API_KEY = os.getenv("GEMINI_API_KEY")

# # # # if not API_KEY:
# # # #     st.error("❌ API Key not found! Check your .env file or manually set it.")
# # # #     st.stop()

# # # # # ✅ Configure Gemini API
# # # # genai.configure(api_key=API_KEY)

# # # # # ✅ Select available model
# # # # try:
# # # #     available_models = [model.name for model in genai.list_models()]
# # # #     if "gemini-1.5-pro" in available_models:
# # # #         MODEL_NAME = "gemini-1.5-pro"
# # # #     elif "gemini-pro" in available_models:
# # # #         MODEL_NAME = "gemini-pro"
# # # #     else:
# # # #         st.error("❌ No valid Gemini model found! Check your API key.")
# # # #         st.stop()
# # # # except Exception as e:
# # # #     st.error(f"❌ Error fetching models: {e}")
# # # #     st.stop()

# # # # st.title(":rainbow[Flashcard Maker]")

# # # # message = st.text_area("Enter your text to generate flashcards", height=200)

# # # # def generate_flashcards(text):
# # # #     """Generates flashcards using Gemini API."""
# # # #     PROMPT_TEMPLATE = f"""
# # # #     You are an AI that creates flashcards in **VALID JSON FORMAT**. 

# # # #     **Example Output:**
# # # #     ```
# # # #     {{
# # # #       "flashcards": [
# # # #         {{"question": "What is Python?", "answer": "Python is a programming language."}},
# # # #         {{"question": "How does AI work?", "answer": "AI works by learning patterns from data."}},
# # # #         {{"question": "Why use functions?", "answer": "Functions improve code reusability."}},
# # # #         {{"question": "What is a loop?", "answer": "A loop is used to repeat a block of code."}},
# # # #         {{"question": "Explain recursion?", "answer": "Recursion is a function calling itself."}}
# # # #       ]
# # # #     }}
# # # #     ```

# # # #     **Now generate 5 flashcards for this text:**
# # # #     ```
# # # #     {text}
# # # #     ```
# # # #     """

# # # #     model = genai.GenerativeModel(MODEL_NAME)

# # # #     try:
# # # #         response = model.generate_content(PROMPT_TEMPLATE)
# # # #         extracted_response = response.text.strip()  
        
# # # #         # ✅ Try parsing JSON safely
# # # #         extracted_json = extracted_response[
# # # #             extracted_response.find("{") : extracted_response.rfind("}") + 1
# # # #         ]
# # # #         parsed_response = json.loads(extracted_json)

# # # #         return parsed_response.get("flashcards", [])
# # # #     except json.JSONDecodeError:
# # # #         st.error("❌ Failed to generate valid flashcards. Please try again.")
# # # #         st.write("📌 **Debugging Response:**", response.text)  # Debugging output
# # # #         return []
# # # #     except Exception as e:
# # # #         st.error(f"❌ Error: {e}")
# # # #         return []

# # # # if st.button("Generate Flashcards"):
# # # #     if message.strip():
# # # #         flashcards = generate_flashcards(message)
        
# # # #         if flashcards:
# # # #             st.session_state["flashcards"] = flashcards  # Store flashcards in session
# # # #             st.success("✅ Flashcards generated! See below.")

# # # # if "flashcards" in st.session_state:
# # # #     st.subheader("📌 Your Flashcards:")
# # # #     for flashcard in st.session_state["flashcards"]:
# # # #         st.write(f"**Q:** {flashcard['question']}")
# # # #         st.write(f"**A:** {flashcard['answer']}")
# # # #         st.markdown("---")

# # # #     flashcards_text = "\n\n".join(
# # # #         f"Q: {fc['question']}\nA: {fc['answer']}" for fc in st.session_state["flashcards"]
# # # #     )

# # # #     st.download_button(
# # # #         label="📥 Download Flashcards",
# # # #         data=flashcards_text,
# # # #         file_name="flashcards.txt",
# # # #         type="primary",
# # # #     )
# # # # import os
# # # # from dotenv import load_dotenv

# # # # load_dotenv()
# # # # print("API Key:", os.getenv("GEMINI_API_KEY"))
# # # # import google.generativeai as genai
# # # # from dotenv import load_dotenv
# # # # import os

# # # # load_dotenv()
# # # # genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# # # # try:
# # # #     models = [model.name for model in genai.list_models()]
# # # #     print("Available Models:", models)
# # # # except Exception as e:
# # # #     print("Error Fetching Models:", e)
# # import streamlit as st
# # import os
# # import json
# # from dotenv import load_dotenv
# # import google.generativeai as genai

# # # Load environment variables
# # load_dotenv()
# # genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# # st.title(":rainbow[Flashcard Maker]")

# # message = st.text_area("Enter your text to generate flashcards", height=200)

# # def generate_flashcards(text):
# #     """Generates flashcards using Gemini API."""
# #     PROMPT_TEMPLATE = f"""
# #     You are an AI that creates concise one-liner flashcards based on a given text. 
# #     Generate exactly 5 flashcards in the following JSON format:
    
# #     {{
# #       "flashcards": [
# #         {{"question": "What is ...?", "answer": "Definition of ..."}},
# #         {{"question": "How does ... work?", "answer": "It works by ..."}},
# #         {{"question": "Why is ... important?", "answer": "Because ..."}},
# #         {{"question": "What are the benefits of ...?", "answer": "The benefits are ..."}},
# #         {{"question": "Explain ... briefly.", "answer": "It means ..."}}
# #       ]
# #     }}
    
# #     Text: {text}
# #     """

# #     model = genai.GenerativeModel("gemini-1.5-pro")
# #     response = model.generate_content(PROMPT_TEMPLATE)

# #     try:
# #         extracted_response = response.text.strip()  # Extract text response
# #         parsed_response = json.loads(extracted_response)
        
# #         # ✅ Check if "flashcards" exist in response
# #         if "flashcards" in parsed_response:
# #             return parsed_response["flashcards"]
# #         else:
# #             st.error("No flashcards generated. Try again!")
# #             return []
# #     except json.JSONDecodeError:
# #         st.error("Failed to generate valid flashcards. Please try again.")
# #         return []

# # # ✅ Flashcard Generation Button
# # if st.button("Generate Flashcards"):
# #     if message.strip():
# #         flashcards = generate_flashcards(message)
        
# #         if flashcards:
# #             st.session_state["flashcards"] = flashcards  # Store flashcards in session
# #             st.success("✅ Flashcards generated successfully!")

# # # ✅ Show Flashcards if available
# # if "flashcards" in st.session_state:
# #     st.subheader("📚 Your Flashcards:")
# #     for i, flashcard in enumerate(st.session_state["flashcards"], start=1):
# #         st.markdown(f"### 🃏 Flashcard {i}")
# #         st.write(f"**Q:** {flashcard['question']}")
# #         st.write(f"**A:** {flashcard['answer']}")
# #         st.markdown("---")

# #     # ✅ Download Option
# #     flashcards_text = "\n\n".join(
# #         f"Q: {fc['question']}\nA: {fc['answer']}" for fc in st.session_state["flashcards"]
# #     )
# # #
# #     st.download_button(
# #         label="📥 Download Flashcards",
# #         data=flashcards_text,
# #         file_name="flashcards.txt",
# #         type="primary",
# #     )
# import streamlit as st
# import os
# import json
# from dotenv import load_dotenv
# import google.generativeai as genai  # Gemini AI SDK

# # Load environment variables
# load_dotenv()
# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# st.title("📚 AI-Powered Flashcard Maker")

# # User Input
# message = st.text_area("Enter your text to generate flashcards:", height=200)

# def generate_flashcards(text):
#     """Generates flashcards using Gemini AI"""
#     PROMPT_TEMPLATE = f"""
#     You are an AI that generates concise, one-liner flashcards from the given text.
#     Generate exactly 5 flashcards in JSON format like this:
    
#     {{
#       "flashcards": [
#         {{"question": "What is ...?", "answer": "Definition of ..."}},
#         {{"question": "How does ... work?", "answer": "It works by ..."}},
#         {{"question": "Why is ... important?", "answer": "Because ..."}},
#         {{"question": "What are the benefits of ...?", "answer": "The benefits are ..."}},
#         {{"question": "Explain ... briefly.", "answer": "It means ..."}}
#       ]
#     }}
    
#     Text: {text}
#     """

#     try:
#         model = genai.GenerativeModel("gemini-1.5-pro")
#         response = model.generate_content(PROMPT_TEMPLATE)
#         extracted_response = response.text.strip()  # Extract response text
#         parsed_response = json.loads(extracted_response)  # Parse JSON
#         return parsed_response.get("flashcards", [])
    
#     except json.JSONDecodeError:
#         st.error("❌ Failed to generate valid flashcards. Please try again.")
#         return []

# if st.button("Generate Flashcards"):
#     if message.strip():
#         flashcards = generate_flashcards(message)
        
#         if flashcards:
#             st.session_state["flashcards"] = flashcards  # Store flashcards in session
#             st.success("✅ Flashcards generated successfully!")

# if "flashcards" in st.session_state:
#     st.subheader("🃏 Your AI-Generated Flashcards:")
#     for flashcard in st.session_state["flashcards"]:
#         st.write(f"**Q:** {flashcard['question']}")
#         st.write(f"**A:** {flashcard['answer']}")
#         st.markdown("---")

#     flashcards_text = "\n\n".join(
#         f"Q: {fc['question']}\nA: {fc['answer']}" for fc in st.session_state["flashcards"]
#     )

#     st.download_button(
#         label="⬇️ Download Flashcards",
#         data=flashcards_text,
#         file_name="flashcards.txt",
#         type="primary",
#     )
import streamlit as st
import os
import json
from dotenv import load_dotenv
import google.generativeai as genai  # Gemini AI SDK

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

st.title("📚 AI-Powered Flashcard Maker")

# User Input
message = st.text_area("Enter your text to generate flashcards:", height=200)

def generate_flashcards(text):
    """Generates flashcards using Gemini AI"""
    PROMPT_TEMPLATE = f"""
    You are an AI that extracts key concepts and creates concise, one-liner flashcards.
    Generate exactly 5 flashcards in JSON format:
    
    {{"flashcards": [
        {{"question": "What is ...?", "answer": "..."}},
        {{"question": "How does ... work?", "answer": "..."}},
        {{"question": "Why is ... important?", "answer": "..."}},
        {{"question": "What are the benefits of ...?", "answer": "..."}},
        {{"question": "Explain ... briefly.", "answer": "..."}}
    ]}}
    
    Text: {text}
    """

    try:
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(PROMPT_TEMPLATE)
        
        # Ensure response is valid
        if response and hasattr(response, "text"):
            raw_response = response.text.strip()

            # Extract JSON portion only
            json_start = raw_response.find("{")
            json_end = raw_response.rfind("}")
            if json_start != -1 and json_end != -1:
                json_data = raw_response[json_start : json_end + 1]
                parsed_response = json.loads(json_data)  # Parse JSON

                return parsed_response.get("flashcards", [])

        st.error("❌ API response was not in expected format.")
        return []
    
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
        return []

if st.button("Generate Flashcards"):
    if message.strip():
        flashcards = generate_flashcards(message)
        
        if flashcards:
            st.session_state["flashcards"] = flashcards  # Store flashcards in session
            st.success("✅ Flashcards generated successfully!")

if "flashcards" in st.session_state:
    st.subheader("🃏 Your AI-Generated Flashcards:")
    for flashcard in st.session_state["flashcards"]:
        st.write(f"**Q:** {flashcard['question']}")
        st.write(f"**A:** {flashcard['answer']}")
        st.markdown("---")

    flashcards_text = "\n\n".join(
        f"Q: {fc['question']}\nA: {fc['answer']}" for fc in st.session_state["flashcards"]
    )

    st.download_button(
        label="⬇️ Download Flashcards",
        data=flashcards_text,
        file_name="flashcards.txt",
        type="primary",
    )
