import ollama

prompt_text = (
    "The image displays a parking violation notice attached to the driver's side of a vehicle's windshield. "
    "The notice is printed with various pieces of information typically found on such documents, which includes:\n"
    "\n"
    "- A header at the top that reads 'CITATION NO:' followed by a number '918065' and 'Violation Date:' followed by dates '2/17 9:43 PM.'\n"
    "- Below this header is the name of an individual and their address.\n"
    "- There are details provided about the vehicle, such as the make, model, color, and license plate number.\n"
    "- The notice lists the parking violation, stating 'Violation' followed by a description of what was done wrong: 'No Permit.'\n"
    "- The amount due for the violation is '$140,' indicating that the recipient must pay this sum to resolve the issue.\n"
    "- At the bottom, there are instructions for paying the fine, which include 'PAY IN PERSON' and an address for a nearby court or payment facility.\n"
    "\n"
    "The notice appears to be from the Chautauqua County Court, as indicated by the logo at the top left corner of the paper. "
    "The image style is a straightforward photograph with no filters or artistic manipulations, focusing on the contents of the document."
    "What should I do in this kind of situation? What is my duty?"
)

response_text = ollama.generate(
    model='gemma3:4b',
    prompt=prompt_text
)
print("Text Response:")
print(response_text['response'])