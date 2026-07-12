import json
import re
from typing import List, Dict, Any, Optional
from src.logger import logger

def extract_json_from_text(text: str) -> Optional[List[Dict[str, Any]]]:
    """
    Extracts a JSON list from a text block, handling common LLM formatting behaviors
    such as wrapping JSON in markdown blocks (e.g., ```json ... ```).
    
    Args:
        text: Raw text string potentially containing JSON.
        
    Returns:
        A list of dictionaries if successful, otherwise None.
    """
    if not text:
        return None
        
    # Clean the input text first
    cleaned = text.strip()
    
    # Check for markdown code block markers
    markdown_match = re.search(r'```(?:json)?\s*([\s\S]*?)\s*```', cleaned)
    if markdown_match:
        cleaned = markdown_match.group(1).strip()
        
    # Find matching brackets to extract just the list/object
    list_match = re.search(r'\[\s*\{[\s\S]*\}\s*\]', cleaned)
    if list_match:
        cleaned = list_match.group(0)

    try:
        data = json.loads(cleaned)
        if isinstance(data, list):
            return data
        elif isinstance(data, dict):
            # Wrap single object in a list for consistency
            return [data]
        return None
    except json.JSONDecodeError as e:
        logger.error(f"JSON parsing error: {str(e)}\nRaw block analyzed: {cleaned[:200]}...")
        return None

def validate_quiz_schema(quiz_list: List[Dict[str, Any]]) -> bool:
    """
    Validates that the parsed quiz list conforms strictly to our schema.
    Schema requires:
    - Exactly 5 questions
    - Each question must contain: 'id', 'question', 'options', 'correct_answer', 'explanation'
    - 'options' must be a dictionary with keys 'A', 'B', 'C', 'D'
    - 'correct_answer' must be one of 'A', 'B', 'C', 'D'
    
    Args:
        quiz_list: A list of parsed dictionaries.
        
    Returns:
        True if the schema is correct, False otherwise.
    """
    if not quiz_list or len(quiz_list) != 5:
        logger.warning(f"Quiz validation failed: expected 5 items, got {len(quiz_list) if quiz_list else 0}")
        return False
        
    required_keys = {"id", "question", "options", "correct_answer", "explanation"}
    valid_answers = {"A", "B", "C", "D"}
    
    for idx, item in enumerate(quiz_list):
        # Check all keys are present
        if not required_keys.issubset(item.keys()):
            missing = required_keys - item.keys()
            logger.warning(f"Quiz item {idx} is missing keys: {missing}")
            return False
            
        # Validate options structure
        options = item["options"]
        if not isinstance(options, dict) or not set(options.keys()) == valid_answers:
            logger.warning(f"Quiz item {idx} options are invalid. Expected keys A, B, C, D. Got: {options}")
            return False
            
        # Validate correct answer label
        ans = str(item["correct_answer"]).strip().upper()
        if ans not in valid_answers:
            logger.warning(f"Quiz item {idx} correct_answer '{ans}' is invalid.")
            return False
            
        # Standardize correct answer to uppercase
        item["correct_answer"] = ans

    return True
