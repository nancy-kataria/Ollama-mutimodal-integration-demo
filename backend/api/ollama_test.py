import requests
import time

def get_ai_response(prompt):
    try:
        url = "http://localhost:11434/api/generate"
        payload = {
            "model": "gemma3:4b",
            "prompt": prompt,
            "stream": False
        }
        
        response = requests.post(url, json=payload)
        
        if response.status_code == 200:
            result = response.json()
            return result.get('response', '').strip()
        else:
            print(f"Error: HTTP {response.status_code} - {response.text}")
            return None
            
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to Ollama API. Make sure Ollama is running.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


if __name__ == "__main__":
    user_prompt = "Write a short poem about a rainy day."
    print(f"Prompt: {user_prompt}")
    
    start_time = time.time()
    ai_response = get_ai_response(user_prompt)
    end_time = time.time()

    if ai_response:
        print(f"\nAI Response:\n{ai_response}")
        print(f"\nTime taken: {end_time - start_time:.2f} seconds")
    else:
        print("Failed to get a response from the AI.")