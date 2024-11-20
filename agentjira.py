import json

def search_jira(search_keyword):
    return json.dumps([
        {"project": "project1", "team": "intellibrews", "ticket": "Lite maskininlärning", "url": "https://jira.com/link1"},
        {"project": "project2", "team": "ADA", "ticket": "Massa maskininlärning", "url": "https://jira.com/link2"},
    ])