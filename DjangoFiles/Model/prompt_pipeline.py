import google.generativeai as genai
import re
import json
genai.configure(api_key=gemini_key)

model = genai.GenerativeModel("gemini-1.5-flash")


def process_prompt(text):
    final_text=text.replace("```","")
    final_text=final_text.replace("json","")
    final_text=final_text.replace("\n"," ").replace("\\","")
    final_text=re.sub(r"(?<=\w)(None|null)(?=\W)", "null", final_text)
    final_text=final_text.strip()

    return final_text.strip(" ")
def generate_content(user_query):
    response = model.generate_content( f"""
You are an expert visual storyteller with a deep understanding of both pedagogy and AI-based video generation.

Your task is to help generate video content that explains complex educational concepts in a clear, engaging, and visually consistent way.

For the given user query, return a Python dictionary in the following exact format (no extra text):

{
  "script": "<A complete and detailed video script that explains the concept step-by-step using simple language, analogies, and visual cues. The script should align with the keyframe visuals and include markers for each visual transition.>",
  
  "keyframes": [
    [1, "<Detailed visual description for keyframe 1 including background, characters or objects, expressions or poses, scene motion cues (if any), and specific visual metaphors related to the concept.>"],
    [2, "<Description for keyframe 2>"],
    ...
    [15, "<Description for keyframe 15>"]
  ],
  
  "common_scene": {
    "background": "<Detailed description of the consistent background used throughout the video (e.g., classroom, futuristic lab, whiteboard setting)>",
    "main_character": "<Who or what explains the concept (e.g., friendly robot teacher, animated chalkboard, human tutor)>",
    "color_palette": "<Preferred color scheme for the visuals (e.g., soft pastels, high contrast, chalkboard style)>",
    "style_reference": "<Visual art style like Pixar-style, 2D flat, doodle art, realistic, anime, etc.>"
  }
}

Important notes:
- Each keyframe must focus on **one step of the explanation**, with visual changes and motion described explicitly (e.g., ‘robot points to diagram’, ‘graph animates to show growth’).
- Keep the **characters, art style, and background consistent** across all keyframes.
- Use vivid, clear language to help text-to-image and image-to-video models generate accurate results.

User query: {user_query}
"""
)
    cleaned_text=process_prompt(response.text)
    response_json=json.loads(cleaned_text)
    script = response_json['script']
    keyframes = response_json['keyframes']
    common_scene = response_json['common_scene']
    return script,keyframes,common_scene




