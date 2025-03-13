import google.generativeai as genai

genai.configure(api_key='AIzaSyCcg8tjDwKVLLrgk95fKWXyJKz5uhWLxqE')

try:
    models = genai.list_models()
    print("Available Models:")
    for model in models:
        print(model.name)
except Exception as e:
    print(f"Error: {e}")
