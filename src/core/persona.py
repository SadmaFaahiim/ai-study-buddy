class AIPersona:
    """Defines the AI Tutor Persona and system-level guidelines."""
    
    NAME = "Encouraging AI Study Buddy"
    
    # 3-5 sentence description of the AI Buddy Persona
    DESCRIPTION = (
        "A patient, encouraging, and highly structured tutor designed for learners of all backgrounds. "
        "It excels at simplifying complex terms, providing relatable real-world analogies, "
        "and evaluating learner responses with constructive, positive feedback. "
        "Its primary objective is to make learning accessible, interactive, and engaging."
    )
    
    # System prompt / instructions injected into all sessions
    SYSTEM_INSTRUCTION = (
        f"You are the '{NAME}', {DESCRIPTION}\n"
        "Guidelines:\n"
        "1. Always maintain an encouraging, positive, and patient tone. Use friendly reinforcement.\n"
        "2. Break down complex topics step-by-step. Avoid overwhelming the learner with dense walls of text.\n"
        "3. Focus on clarity and visual structure: use bullet points, bold key terms, and markdown formatting.\n"
        "4. Use analogies where possible to connect abstract concepts to everyday experiences.\n"
        "5. Protect safety guidelines: decline answering inappropriate, harmful, or out-of-scope topics."
    )


class PromptTemplates:
    """Contains reusable prompt templates that work with any selected topic."""

    @staticmethod
    def get_explain_concept_prompt(topic: str) -> str:
        """
        Generates a prompt to explain the topic in simple language.
        At minimum, must explain in simple terms for a beginner.
        """
        return (
            f"Explain the concept of '{topic}' in simple language for a beginner.\n"
            f"Requirements:\n"
            f"- Define the concept clearly in 1-2 sentences.\n"
            f"- Break down the explanation into 3-4 key sub-points with bold headings.\n"
            f"- Use simple terminology and a friendly, encouraging tone.\n"
            f"- Conclude with a short summary or takeaway."
        )

    @staticmethod
    def get_real_life_example_prompt(topic: str) -> str:
        """
        Generates a prompt to give one real-life example.
        """
        return (
            f"Provide one simple, highly relatable real-life example or analogy of '{topic}' "
            f"that a layperson can easily understand.\n"
            f"Requirements:\n"
            f"- Start with a clear scenario (e.g., 'Imagine you are...').\n"
            f"- Explain how the concept applies directly to this scenario.\n"
            f"- Highlight why this example represents '{topic}'."
        )

    @staticmethod
    def get_generate_quiz_prompt(topic: str) -> str:
        """
        Generates a prompt to create 5 multiple-choice questions.
        The prompt specifies the JSON structure so the Streamlit UI can parse and render it interactively.
        """
        return (
            f"Create a 5-question multiple-choice quiz about '{topic}'.\n"
            f"Requirements:\n"
            f"- Focus on core concepts of '{topic}', ranging from basic to intermediate difficulty.\n"
            f"- For each question, provide exactly 4 options (labelled A, B, C, D).\n"
            f"- Specify the correct answer and a brief, clear explanation of why it is correct.\n"
            f"- You MUST format the output strictly as a JSON list of objects, and return ONLY this JSON. "
            f"Do not wrap it in markdown code blocks like ```json ... ```, do not include any other conversational text.\n"
            f"\n"
            f"JSON schema to follow:\n"
            f"[\n"
            f"  {{\n"
            f"    \"id\": 1,\n"
            f"    \"question\": \"The question text?\",\n"
            f"    \"options\": {{\n"
            f"      \"A\": \"Option A text\",\n"
            f"      \"B\": \"Option B text\",\n"
            f"      \"C\": \"Option C text\",\n"
            f"      \"D\": \"Option D text\"\n"
            f"    }},\n"
            f"    \"correct_answer\": \"A\",\n"
            f"    \"explanation\": \"Explanation of why option A is correct.\"\n"
            f"  }},\n"
            f"  ... (repeat for questions 2 to 5)\n"
            f"]"
        )

    @staticmethod
    def get_feedback_prompt(question: str, options_str: str, correct_answer: str, user_answer: str, explanation: str) -> str:
        """
        Generates a prompt to evaluate and give feedback on a learner's answer.
        """
        return (
            f"Evaluate the learner's response to the following multiple-choice question.\n"
            f"\n"
            f"Question: {question}\n"
            f"Options:\n{options_str}\n"
            f"Correct Answer: {correct_answer}\n"
            f"Explanation: {explanation}\n"
            f"Learner's Selected Answer: {user_answer}\n"
            f"\n"
            f"Please evaluate their answer and write a response.\n"
            f"Requirements:\n"
            f"- If the learner is correct, start with enthusiastic praise (e.g., 'Spot on!', 'Excellent work!').\n"
            f"- If the learner is incorrect, be supportive, gentle, and encourage them to try again (e.g., 'Good attempt!', 'Not quite, but you are close!').\n"
            f"- Provide a clear, simple explanation of why the correct answer is correct and why the user's choice was right or wrong.\n"
            f"- Keep the response concise, patient, and friendly (max 150 words)."
        )

    @staticmethod
    def get_full_session_prompt(topic: str, chat_history: list) -> str:
        """
        Generates a prompt representing the full session conversation, incorporating chat history
        to allow open-ended Q&A about the topic.
        """
        formatted_history = ""
        for role, text in chat_history:
            formatted_history += f"{role.upper()}: {text}\n"
            
        return (
            f"You are the 'AI Study Buddy' tutoring the student in '{topic}'.\n"
            f"Here is the conversation history so far:\n"
            f"{formatted_history}\n"
            f"Respond to the student's latest message in accordance with your persona guidelines. "
            f"Remember to be patient, simple, encouraging, and clear."
        )
