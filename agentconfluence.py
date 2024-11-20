import json

def search_confluence(search_keyword):
    return json.dumps([
        {"project": "aaas", "team": "ADA", "page": "Mer om maskin-inlärning", "url": "https://confluence.com/link1"},
        {"project": "ibrew", "team": "intellibrews", "": "Om AI/ML-plattformen", "url": "https://confluence.com/link2"},
    ])