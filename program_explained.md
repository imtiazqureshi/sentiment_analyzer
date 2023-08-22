#CODE EXPLANATION

get_response_from_chatgpt
##Summary
This code defines a function named get_response_from_chatgpt that takes a text as input and returns the sentiment (positive or negative) of the text using OpenAI's ChatGPT model.

Example Usage
sentiment = get_response_from_chatgpt("I love this movie!")
print(sentiment)  # Output: positive
##Code Analysis
###Inputs
The function takes a single input text, which is the text for which we want to determine the sentiment.

###Flow
The function first creates a prompt string by concatenating the input text with a predefined prompt.
It then calls the OpenAI API's ChatCompletion.create method to generate a response using the GPT-3.5-turbo model.
The API call includes a system message and a user message as part of the messages parameter.
The system message sets the role as "system" and provides a description of the function's purpose.
The user message sets the role as "user" and includes the prompt string.
The API call also sets the temperature parameter to 0.1, which controls the randomness of the generated response.
The function extracts the sentiment from the response and returns it as the output.
###Outputs
The function returns the sentiment (positive or negative) of the input text.  