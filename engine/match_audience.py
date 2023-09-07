# helpers/match_audience.py
from .fetch_audiences import fetch_custom_audiences
from .text_processing import preprocess_text, calculate_similarity

def find_best_match(processed_input, custom_audiences):
    best_match = 'None'
    max_similarity = 0

    for audience in custom_audiences:
        similarity = calculate_similarity(processed_input, preprocess_text(audience))
        if similarity > max_similarity:
            max_similarity = similarity
            best_match = audience

    return best_match