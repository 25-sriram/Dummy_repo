
import spacy
from collections import defaultdict

class RequirementNLPProcessor:

    def __init__(self):
        # Load spaCy English model
        self.nlp = spacy.load("en_core_web_sm")

        # Common technical terms (can expand later)
        self.tech_dictionary = {
            "token", "jwt", "auth", "authentication",
            "module", "login", "validation", "api",
            "database", "service", "endpoint"
        }

    def process_requirement(self, requirement_id, text):

        doc = self.nlp(text)

        action_verbs = []
        components = []
        technical_terms = []
        keywords = []

        # Extract verbs, nouns, and entities
        for token in doc:

            # ACTION VERBS
            if token.pos_ == "VERB":
                action_verbs.append(token.lemma_)

            # COMPONENTS (noun phrases)
            if token.pos_ in ["NOUN", "PROPN"]:
                components.append(token.text)

            # TECHNICAL TERMS
            if token.text.lower() in self.tech_dictionary:
                technical_terms.append(token.text.lower())

            # KEYWORDS
            if token.pos_ in ["NOUN", "PROPN", "ADJ"]:
                keywords.append(token.text.lower())

        result = {
            "id": requirement_id,
            "action_verbs": list(set(action_verbs)),
            "components": list(set(components)),
            "technical_terms": list(set(technical_terms)),
            "keywords": list(set(keywords))
        }

        return result


if __name__ == "__main__":

    processor = RequirementNLPProcessor()

    requirement_text = "Fix login token validation bug in authentication module"

    output = processor.process_requirement(
        "REQ-001",
        requirement_text
    )

    print("\nExtracted Requirement Entities:\n")
    for key, value in output.items():
        print(f"{key}: {value}")
