import ollama
import time

start_time = time.time()

result = ollama.chat(
    model='llava:7b',  # Fast vision model
    messages=[{
        'role': 'user',
        'content': 'What do you see in the image?',
        'images': ['/Users/nancy/Downloads/candy.JPG']
    }]
)

end_time = time.time()
execution_time = end_time - start_time

print(result['message']['content'])
print(f"\n--- Execution Time: {execution_time:.2f} seconds ---")
