from transformers import pipeline

print("Loading Granite model...")

generator = pipeline(
    "text-generation",
    model="ibm-granite/granite-3.3-2b-instruct"
)

print("Model loaded successfully!")

result = generator(
    "Hello! Introduce yourself.",
    max_new_tokens=50,
    return_full_text=False
)

print(result)