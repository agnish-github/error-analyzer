from error_catcher import install_global_hook
from ai_helper import ask_chatgpt

def handle_error(error_info):
    print("Error captured! Analyzing with AI Agent...")
    response = ask_chatgpt(error_info)
    print("\n--- AI Response ---\n")
    print(response)

def main():
    install_global_hook(handle_error)

    # Example faulty code to trigger
    print("Running test...")
    1 / 0  # Trigger ZeroDivisionError

if __name__ == "__main__":
    main()
