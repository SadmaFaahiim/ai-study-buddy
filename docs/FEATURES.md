# Feature Documentation: AI Learning Buddy

This document details the core functionalities and interactive features implemented in the **AI Learning Buddy**.

---

## 1. Concept Explainer (`💡 Explain Concept`)
* **Purpose:** Provides a beginner-friendly overview of any topic entered by the user.
* **Prompt Mechanics:** Employs the `Explain Concept` template.
* **Layout Design:** 
  - Renders inside a card.
  - Summarizes the topic in plain language.
  - Highlights 3-4 key sub-points with bold headings.
  - Utilizes bullet points to prevent cognitive overload.

---

## 2. Real-Life Analogy Maker (`🍎 Real-Life Example`)
* **Purpose:** Bridges abstract theory with everyday practical intuition.
* **Prompt Mechanics:** Instructs the AI to build a relatable scenario (e.g., "Imagine you are...").
* **Layout Design:**
  - Standardizes the response with clear scenario-driven milestones.
  - Helps students contextualize complex concepts like SQL joins or regressions.

---

## 3. Interactive Quiz Engine (`📝 Take Interactive Quiz`)
* **Purpose:** Active recall testing tool that operates both online (dynamic via Gemini) and offline (pre-set sample data).
* **Key Mechanisms:**
  - **Dynamic Generation:** Prompts Gemini to return a raw JSON array representing 5 multiple-choice questions (MCQs) with options A, B, C, and D.
  - **Schema Validation:** The application parses the response, verifies that exactly 5 questions are returned, and checks that all fields are intact.
  - **Offline Fallback:** If the user has no API key or network access, they can click "Load Pre-set Sample Quiz", which loads a validated quiz on **SQL Joins** from `data/sample_quiz.json` locally.
  - **Stateful Forms:** Streamlit handles form submissions. Upon submission, it renders:
    1. A color-coded results section showing correct/incorrect choices.
    2. Dynamic feedback generated for each question explaining the answer logic.
    3. An overall scoreboard showing the final score (e.g. `4 / 5`) with a summary card.

---

## 4. Stateful Conversation Buddy (`💬 Ask Anything`)
* **Purpose:** Supports open-ended tutoring where students can ask follow-up questions.
* **Conversation History:**
  - Maintains state inside the Streamlit session state variable (`st.session_state.chat_history`).
  - Passes the history to Gemini to maintain context.
  - Formatted like a standard modern chat interface with user and assistant message avatars.

---

## 5. Student Corner (`🎓 Student Corner`)
* **Purpose:** Built specifically to satisfy the assignment submission guidelines.
* **Components Displayed:**
  - **AI Buddy Persona Description:** Shows the persona description and system prompt.
  - **Prompt Templates:** Displays the python structures and literal text of the 5 reusable templates.
  - **Sample Learning Conversation:** Displays the transcript showing the tutor in action.
  - **5-Question Quiz + Answers:** Shows the questions, options, correct answers, and explanations.
  - **Reflection on AI Limitations:** Displays the 350-word reflection essay.
* **Benefit:** Simplifies evaluation for instructors grading the assignment.
