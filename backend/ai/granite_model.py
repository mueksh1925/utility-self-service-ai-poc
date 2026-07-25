from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="ibm-granite/granite-3.3-2b-instruct"
)

def generate_answer(prompt: str) -> str:
    result = generator(
        prompt,
        max_new_tokens=150,
        do_sample=False,
        return_full_text=False
    )

    return result[0]["generated_text"].strip()