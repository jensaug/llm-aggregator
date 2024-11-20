from agentjira import search_jira
from agentgit import search_git
from agentconfluence import search_confluence
from llm import get_completion

def find_search_keyword(user_input):
    userContent = "Lista i fallande ordning de viktigaste nyckelorden (max 3 stycken) i följande fråga: " + user_input
    #completion = get_completion(userContent)
    completion = "maskininlärning, team"
    print("Nyckelord i frågeställning:\n", completion)
    return completion

def aggregate_response(user_input, api_responses):
    llm_input = "Du skall besvara en fråga genom att sammaställa information från ett antal informationsystem."
    llm_input = "\nSkicka om möjligt alltid med länk i sammanställningen."
    llm_input = "\nFrågan som skall besvaras är: " + user_input
    llm_input += "\n\nSvaret skall vara baserat på information från följande informationssystem: " + " | ".join(api_responses)
    completion = get_completion(llm_input)
    #print("Svar:", completion)
    return completion

def agent_orchestrator(user_input):
    print("Orkestrerar agenter som svarar på frågor om: ", user_input)
    api_responses = []
    search_keyword = find_search_keyword(user_input)
    if search_keyword:
        api_responses.append("Söksvar från ärendesystemet JIRA: " + search_jira(search_keyword))
        api_responses.append("Söksvar från källkodssystemet Git: " + search_git(search_keyword))
        api_responses.append("Söksvar från informationssystemet Confluence: " + search_confluence(search_keyword))        
    else:
        pass
    return aggregate_response(user_input, api_responses)

def main():
    print("Välkommen till Aggregatorn. Vad vill du veta? \nSkriv 'exit' att avsluta.")
    while True:
        #user_input = input("[User Prompt]: ")
        user_input = "Vilka team jobbar med maskininlärning"
        if user_input.lower() == 'exit':
            break
        response = agent_orchestrator(user_input)
        print(f"[Agent]: {response}")
        break

if __name__ == "__main__":
    main()