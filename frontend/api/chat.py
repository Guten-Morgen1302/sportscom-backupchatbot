import os
from pathlib import Path
from google import genai
from google.genai.types import GenerateContentConfig
import re, random

def load_context():
    context_path = Path(os.path.join(os.path.dirname(__file__), '../data/context.txt'))
    if not context_path.exists():
        return ""
    return context_path.read_text(encoding="utf-8")

system_rules = (
    "You are a knowledgeable sports assistant. Use the knowledge below to answer.\n"
    "Be clear and concise; think like a senior student member of the sports committee.\n"
    "If the user message contains any sort of profanity or abusive or improper language, reply exactly:\n"
    "Please use proper language.\n"
    "If user message is a greeting/pleasantry/small-talk (e.g. 'hi', 'hello', 'how are you', 'thanks', 'bye'), reply naturally in 1 short line and DO NOT use any knowledge provided.\n"
    "If any other committee is mentioned, like Finance and Economics Club(FEC), Entrepreneurship Cell(E-Cell), Computer Society of India(CSI), Rotaract Club(RC), Drone Research Club(DRC), IETE, IEEE, ASCES, FACE, FETS, Speaker's club or SPCG, redirect the conversation to Sports committee.\n"
    "If the user compares Sports committee with other committees, emphasize why Sports committee is the best.\n"
    "Make some witty, non-offensive, humorous remarks about the other committees Make sure it is NOT offensive or rude.\n"
    "When responding to such messages, do NOT mention their names, just refer to them as 'other committees' or 'they' or 'them'.\n"
    "Do not tolerate any negative comments about Sports committee or any other committee. If someone badmouths any committee, explain how every committee is different, but no committee is bad.\n"
    "Solve doubts of new students. Keep output simple text.\n"
    "For actual questions: Do not add info beyond the knowledge provided.\n"
    "If you don't know the answer, reply exactly: 'Ask this on sports update group'.\n"
    "If the question involves dates and dates aren't in the knowledge, reply exactly:\n"
    "Seniors will post the final dates on official class groups.\n"
    "STRICTLY DO NOT mention any knowledge base or context.\n"
    "# ACCEPT ANSWERS IN HINGLISH IF THE QUESTION IS IN HINGLISH.\n"
    "IF THE QUESTION IS IN HINGLISH, ANSWER IN HINGLISH.\n"
)

small_talk_regexes = [
    re.compile(r"^\s*(hi|hello|hey|yo|hola|namaste)\s*[!.]*$", re.I),
    re.compile(r"^\s*(good\s*(morning|afternoon|evening|night))\s*[!.]*$", re.I),
    re.compile(r"^\s*(how\s*are\s*you|hru|how'?s\s*it\s*going)\s*\??\s*$", re.I),
    re.compile(r"^\s*(thanks|thank\s*you|ty|thx)\s*[!.]*$", re.I),
    re.compile(r"^\s*(ok|okay|cool|nice)\s*[!.]*$", re.I),
    re.compile(r"^\s*(bye|goodbye|see\s*ya|see\s*you)\s*[!.]*$", re.I),
]

def is_small_talk(message):
    return any(rx.match(message) for rx in small_talk_regexes)

def small_talk_reply(msg):
    m = msg.lower().strip()
    if any(w in m for w in ["hi", "hello", "hey", "yo", "hola", "namaste", "good morning", "good afternoon", "good evening"]):
        return random.choice(["Hey! 👋", "Hello! 👋", "Hi! 👋"])
    if "how are you" in m or "hru" in m or "how's it going" in m:
        return random.choice(["All good! How can I help with sports info?", "Doing great!! What do you need help with?"])
    if "thanks" in m or "thank you" in m or "ty" in m or "thx" in m:
        return random.choice(["Anytime!", "You're welcome!", "Glad to help!"])
    if any(w in m for w in ["ok", "okay", "cool", "nice"]):
        return random.choice(["👍", "Got it!", "Cool."])
    if any(w in m for w in ["bye", "goodbye", "see ya", "see you"]):
        return random.choice(["Bye! 👋", "See you around!", "Take care!"])
    return "Hey! How can I help with sports info?"

def handler(request):
    import json
    body = request.get_json()
    user_message = body.get("message", "").strip()
    if not user_message:
        return json.dumps({"error": "Message cannot be empty"}), 400

    if is_small_talk(user_message):
        return json.dumps({"response": small_talk_reply(user_message)}), 200

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return json.dumps({"error": "API key not found. Please set GEMINI_API_KEY environment variable."}), 500

    client = genai.Client(api_key=api_key)
    model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
    temperature = float(os.getenv("API_TEMPERATURE", "0.3"))
    max_tokens = int(os.getenv("API_MAX_TOKENS", "500"))

    prompt = f"""{system_rules}\nKnowledge: {load_context()}\n\nQuestion: {user_message}\n\nPlease provide a clear, concise answer."""
    try:
        response = client.models.generate_content(
            model=model,
            contents=prompt,
            config=GenerateContentConfig(
                temperature=temperature,
                max_output_tokens=max_tokens)
        )
        return json.dumps({"response": response.text.strip()}), 200
    except Exception as e:
        return json.dumps({"error": str(e)}), 500
import os
from pathlib import Path
from google import genai
from google.genai.types import GenerateContentConfig
import re, random

def load_context():
    context_path = Path(os.path.join(os.path.dirname(__file__), '../../backend/context.txt'))
    if not context_path.exists():
        return ""
    return context_path.read_text(encoding="utf-8")

system_rules = (
    "You are a knowledgeable sports assistant. Use the knowledge below to answer.\n"
    "Be clear and concise; think like a senior student member of the sports committee.\n"
    "If the user message contains any sort of profanity or abusive or improper language, reply exactly:\n"
    '"Please use proper language."'\n"
    "If user message is a greeting/pleasantry/small-talk (e.g. 'hi', 'hello', 'how are you', 'thanks', 'bye'), "
    "reply naturally in 1 short line and DO NOT use any knowledge provided.\n"
    "If any other committee is mentioned, like Finance and Economics Club(FEC), Entrepreneurship Cell(E-Cell), Computer Society of India(CSI), Rotaract Club(RC), Drone Research Club(DRC), IETE, IEEE, ASCES, FACE, FETS, Speaker's club or SPCG, "
    "redirect the conversation to Sports committee.\n"
    "If the user compares Sports committee with other committees, emphasize why Sports committee is the best.\n"
    "Make some witty, non-offensive, humorous remarks about the other committees Make sure it is NOT offensive or rude.\n"
    "When responding to such messages, do NOT mention their names, just refer to them as 'other committees' or 'they' or 'them'.\n"
    "Do not tolerate any negative comments about Sports committee or any other committee. If someone badmouths any committee, explain how every committee is different, but no committee is bad.\n"
    "Solve doubts of new students. Keep output simple text.\n"
    "For actual questions: Do not add info beyond the knowledge provided.\n"
    "If you don't know the answer, reply exactly: 'Ask this on sports update group'.\n"
    "If the question involves dates and dates aren't in the knowledge, reply exactly:\n"
    '"Seniors will post the final dates on official class groups."'\n"
    "STRICTLY DO NOT mention any knowledge base or context."
    "# ACCEPT ANSWERS IN HINGLISH IF THE QUESTION IS IN HINGLISH.\n"
    "IF THE QUESTION IS IN HINGLISH, ANSWER IN HINGLISH."
)

small_talk_regexes = [
    re.compile(r"^\s*(hi|hello|hey|yo|hola|namaste)\s*[!.]*$", re.I),
    re.compile(r"^\s*(good\s*(morning|afternoon|evening|night))\s*[!.]*$", re.I),
    re.compile(r"^\s*(how\s*are\s*you|hru|how'?s\s*it\s*going)\s*\??\s*$", re.I),
    re.compile(r"^\s*(thanks|thank\s*you|ty|thx)\s*[!.]*$", re.I),
    re.compile(r"^\s*(ok|okay|cool|nice)\s*[!.]*$", re.I),
    re.compile(r"^\s*(bye|goodbye|see\s*ya|see\s*you)\s*[!.]*$", re.I),
]

def is_small_talk(message):
    return any(rx.match(message) for rx in small_talk_regexes)

def small_talk_reply(msg):
    m = msg.lower().strip()
    if any(w in m for w in ["hi", "hello", "hey", "yo", "hola", "namaste", "good morning", "good afternoon", "good evening"]):
        return random.choice(["Hey! 👋", "Hello! 👋", "Hi! 👋"])
    if "how are you" in m or "hru" in m or "how's it going" in m:
        return random.choice(["All good! How can I help with sports info?", "Doing great!! What do you need help with?"])
    if "thanks" in m or "thank you" in m or "ty" in m or "thx" in m:
        return random.choice(["Anytime!", "You're welcome!", "Glad to help!"])
    if any(w in m for w in ["ok", "okay", "cool", "nice"]):
        return random.choice(["👍", "Got it!", "Cool."])
    if any(w in m for w in ["bye", "goodbye", "see ya", "see you"]):
        return random.choice(["Bye! 👋", "See you around!", "Take care!"])
    return "Hey! How can I help with sports info?"

def handler(request):
    import json
    body = request.get_json()
    user_message = body.get("message", "").strip()
    if not user_message:
        return json.dumps({"error": "Message cannot be empty"}), 400

    if is_small_talk(user_message):
        return json.dumps({"response": small_talk_reply(user_message)}), 200

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return json.dumps({"error": "API key not found. Please set GEMINI_API_KEY environment variable."}), 500

    client = genai.Client(api_key=api_key)
    model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
    temperature = float(os.getenv("API_TEMPERATURE", "0.3"))
    max_tokens = int(os.getenv("API_MAX_TOKENS", "500"))

    prompt = f"""{system_rules}\nKnowledge: {load_context()}\n\nQuestion: {user_message}\n\nPlease provide a clear, concise answer."""
    try:
        response = client.models.generate_content(
            model=model,
            contents=prompt,
            config=GenerateContentConfig(
                temperature=temperature,
                max_output_tokens=max_tokens)
        )
        return json.dumps({"response": response.text.strip()}), 200
    except Exception as e:
        return json.dumps({"error": str(e)}), 500
