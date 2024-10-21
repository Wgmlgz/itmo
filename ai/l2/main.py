import re
from pyswip import Prolog

# Initialize Prolog and consult the knowledge base
prolog = Prolog()
prolog.consult('../l1/db.pl')

def parse_user_input(user_input):
    """
    Parses the user's input and dynamically constructs Prolog query components based on regex matching.
    """
    query_parts = []
    # Define patterns to recognize different types of preferences
    patterns = {
        r'i like tech weapons': 'uses_tech_weapon(X)',
        r'i like smart weapons': 'uses_smart_weapon(X)',
        r'i prefer allies in (.+)': lambda match: f'ally(X, _), located_in(X, {match.group(1)})',
        r'i prefer dangerous characters': 'dangerous(X)',
        r'i prefer characters in (.+)': lambda match: f'is_in(X, {match.group(1)})',
        r'i want friends of (.+)': lambda match: f'friend_of(X, {match.group(1)})',
        r'i want enemies of (.+)': lambda match: f'enemy_of(X, {match.group(1)})',
    }

    # Split input by 'and'
    phrases = user_input.lower().split('and')
    for phrase in phrases:
        phrase = phrase.strip()
        for pattern, response in patterns.items():
            match = re.match(pattern, phrase)
            if match:
                if callable(response):
                    query_parts.append(response(match))
                else:
                    query_parts.append(response)
                break  # Match only the first applicable pattern

    return query_parts

def construct_query(query_parts):
    """
    Constructs the final Prolog query from the list of query components.
    """
    if not query_parts:
        return None
    else:
        query = ', '.join(query_parts)
        query = query + '.'
        return query

def get_recommendations(query):
    """
    Executes the Prolog query and returns a list of recommendations.
    """
    results = []
    prolog_query = query[:-1]  # Remove the final dot for the Prolog query
    for sol in prolog.query(prolog_query):
        results.append(sol['X'])
    return results

def main():
    print("Welcome to the Cyberpunk 2077 recommendation system!")
    print("Please enter your preferences. For example:")
    print(" - I like tech weapons and prefer characters in Badlands")
    print(" - I prefer dangerous characters")
    print(" - I want enimies of Arasaka and I like smart weapons")
    print(" - I want enemies of Arasaka")
    print("Please enter your preferences:")
    user_input = input()
    query_parts = parse_user_input(user_input)
    if not query_parts:
        print("Sorry, I didn't understand your preferences.")
        return
    query = construct_query(query_parts)
    recommendations = get_recommendations(query)
    if recommendations:
        print("\nBased on your preferences, we recommend the following character:")
        for character in recommendations:
            print(f"- {character.replace('_', ' ').title()}")
    else:
        print("Sorry, no characters match your preferences.")

if __name__ == '__main__':
    main()
