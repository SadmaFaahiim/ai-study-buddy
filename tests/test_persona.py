from src.core.persona import AIPersona, PromptTemplates

def test_persona_description_exists():
    """Verify that the AI Tutor persona is populated and descriptive."""
    assert len(AIPersona.NAME) > 0
    assert len(AIPersona.DESCRIPTION) > 0
    assert len(AIPersona.SYSTEM_INSTRUCTION) > 0
    assert "tutor" in AIPersona.DESCRIPTION.lower()

def test_explain_concept_prompt():
    """Verify the concept explanation template contains the target topic."""
    topic = "Recursion"
    prompt = PromptTemplates.get_explain_concept_prompt(topic)
    assert topic in prompt
    assert "simple language" in prompt.lower()

def test_real_life_example_prompt():
    """Verify the real-world analogy template contains the target topic."""
    topic = "Photosynthesis"
    prompt = PromptTemplates.get_real_life_example_prompt(topic)
    assert topic in prompt
    assert "real-life example" in prompt.lower()

def test_generate_quiz_prompt():
    """Verify the quiz prompt contains the target topic and requests JSON format."""
    topic = "SQL Joins"
    prompt = PromptTemplates.get_generate_quiz_prompt(topic)
    assert topic in prompt
    assert "JSON" in prompt
    assert "5-question" in prompt.lower()

def test_feedback_prompt():
    """Verify the answer evaluation prompt formats the feedback variables correctly."""
    question = "What is 2+2?"
    options = "A: 3, B: 4, C: 5"
    correct = "B"
    user_ans = "B"
    explanation = "Addition of two twos."
    
    prompt = PromptTemplates.get_feedback_prompt(question, options, correct, user_ans, explanation)
    assert question in prompt
    assert correct in prompt
    assert user_ans in prompt
    assert "evaluate" in prompt.lower()
