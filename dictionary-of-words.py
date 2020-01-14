word_definitions = {
    "tired": "what I feel today",
    "run": "what I want to do",
    "nervous": "how I feel about learning",
}

word_definitions["rollercoaster"] = "what this program feels like"
word_definitions["preemptive nostalgia"] ="what I feel watching cohort 33's demo day"

# print(word_definitions["run"] + " and " + word_definitions["preemptive nostalgia"])

for word in word_definitions:
    # print(word)
    print(f'The definition of {word} is {word_definitions[word]}.')