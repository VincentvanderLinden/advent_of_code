with open('q06.in') as file: 
    input = file.read()
# Create a list of the characters in the datastream
datastream = [char for char in input]


# Function to get markers
def get_marker(datastream, no_of_unique_chars):
    for i in (range(0, len(datastream))):
        # Create sets and check if the length == no_of_unique_chars
        if len(set(datastream[i:i+no_of_unique_chars])) == no_of_unique_chars:
            # Answer is i + no_of_unique_chars, as it indicates the step that found the marker
            marker = i + no_of_unique_chars
            break
    return(marker)

answer1 = get_marker(datastream, 4)
answer2 = get_marker(datastream, 14)

print(f"answer1: {answer1}")
print(f"answer1: {answer2}")
