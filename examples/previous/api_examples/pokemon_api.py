import requests


# This function will give you information about a Pokémon
# Check out https://pokeapi.co/ for details on how it works

# This function takes in a Pokémon name and returns the details
def get_pokemon_details(pokemon_name="Pikachu"):

    # Construct this URL based on the documentation in PokeApi
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"

    # Send request to PokeAPI

    # Remember when we learned about the requests Library?
    # Well the responses can also be JSONs which contain useful data for us to review
    response = requests.get(url)

    # If the request is not successful (Anything other than 200
    if response.status_code != 200:
        print(f"Error: Data not found for '{pokemon_name}' - Status {response.status_code})")
        return

    # Convert the data in to json
    data = response.json()

    # Print the data so you can see the format of the data we are working with

    # You can print just the keys to know what data you have to work with
    # print(data.keys())
    #
    # or the entire JSON Response
    # pretty_json = json.dumps(data, indent=4) # This makes the JSON neater to read
    # print(pretty_json)


    # Extract relevant details
    name = data['name'].capitalize()
    types = [t['type']['name'].capitalize() for t in data['types']]
    image = data['sprites']['front_default']
    weight = data.get('weight', "No weight available")

    # Display results
    print("Here is information about your Pokémon:")
    print(f"\nPokémon: {name}")
    print(f"Types: {', '.join(types)}")
    print(f"Image Url: {image}")
    print(f"Weight: {weight}")

# Example usage
if __name__ == "__main__":
    pokemon = input("Enter a Pokémon name: ")
    if not pokemon:
        pokemon = "Pikachu"
    get_pokemon_details(pokemon)