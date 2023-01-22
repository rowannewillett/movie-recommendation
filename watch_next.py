"""

Let us build a system that will tell you what to watch next based on the word
vector similarity of the description of movies.
● Create a file called watch_next.py
● Read in the movies.txt file. Each separate line is a description of a different movie.
● Your task is to create a function to return which movies a user would watch
next if they have watched Planet Hulk with the description “Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.”
● The function should take in the description as a parameter and return the title of the most similar movie.
● Host your solution on a Git host such as GitLab or GitHub.
○ Remember to exclude any venv or virtualenv files from your repo.
● Add the link for your remote Git repo to your semantic_similarity.txt file.

"""
# Import spacy library and load the nlp model
import spacy

nlp = spacy.load('en_core_web_md')

# Open the movies.txt file for reading the content, and save as list to the movies_content variable.
# Clean the data using a for loop so it only checks the similarity of the description (not Movie X, or escape characters).
read_file = open('movies.txt', 'r')
movies_content = read_file.readlines()

cleaned_movies_content = []

for line in movies_content:
    split_line = line.split(" ")
    split_line.remove("Movie")
    del split_line[0]
    split_line[-1] = split_line[-1].replace('\n', '')
    split_line[0] = split_line[0].replace(':', '')
    cleaned_description = ' '.join(split_line)
    cleaned_movies_content.append(cleaned_description)

current_movie = "Planet Hulk"
current_movie_description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."


def recommend_next_movie(movie_description):
    # Function to Compare current movie description with descriptions of other movies,
    # and then recommend the movie wit the highest semantic similarity score (SpaCy).

    movie_description_model = nlp(movie_description)

    print(f"\nCurrent Movie: {current_movie}\n")
    print(f"==== Film Similarity Scores ====\n")

    highest_score = 0
    highest_description = ''

    for description in cleaned_movies_content:
        similarity = nlp(description).similarity(movie_description_model)
        print(f"Film Description:\n{description}\n      Similarity Score: {similarity}\n")
        if similarity > highest_score:
            highest_score = similarity
            highest_description = description

    print("==== OUR RECOMMENDATION ====\n")

    for line in movies_content:
        if highest_description in line:
            print(f"Our recommendation is: \n      {line}")


# Call function

recommend_next_movie(current_movie_description)
