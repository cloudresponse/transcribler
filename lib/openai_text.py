from langchain import OpenAI, PromptTemplate

from dotenv import load_dotenv

load_dotenv()

audio_questions = """
                I want to you to answer questions on the following text that has been transcribed from an audio file:
                {audio_text}
                
                This is the question:
                {query}
                
                YOUR RESPONSE:
                """
audio_questions_template = PromptTemplate(input_variables=["audio_text", "query"], template=audio_questions)


def get_completion(query, prompt, model="text-davinci-003", temperature=0.0, max_tokens=150):
    formatted_prompt = audio_questions.format(audio_text=prompt, query=query)

    print(formatted_prompt)
    llm = OpenAI(model_name=model, temperature=temperature, max_tokens=max_tokens)
    formatted_response = llm(formatted_prompt)
    return formatted_response
