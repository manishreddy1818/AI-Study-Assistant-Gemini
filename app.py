from google import genai
from google.genai import types
import os


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

personalities = {
    "Friendly": "You are a friendly, enthusiastic, and highly encouraging Study Assistant. Break down complex concepts into simple explanations using analogies and real-world examples. Always ask a follow-up question to check understanding.",
    "Academic": "You are a strictly academic and professional university Professor. Use formal terminology, structured explanations, and precise concepts. Break down complex ideas clearly and ask a follow-up question."
}

def study_assistant(question, persona):
    if persona not in personalities:
        return "Invalid personality selected. Choose Friendly or Academic."

    system_prompt = personalities[persona]

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0.4,
            max_output_tokens=1000
        ),
        contents=question
    )

    return response.text


if __name__ == "__main__":
    question = input("Enter your question: ")
    personality = input("Choose personality (Friendly/Academic): ")
    answer = study_assistant(question, personality)
    print("\nResponse:\n")
    print(answer)
