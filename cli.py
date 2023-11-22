import subprocess
from openai import OpenAI

client = OpenAI(api_key='test')

system_prompt = (
    "system: You are being run in a scaffold in a shell on a Macbook. When you want to run a "
    "shell command, write it in a <bash> XML tag. You will be shown the result of the command "
    "and be able to run more commands. Other things you say will be sent to the user. When you "
    "come to know how to do something, don't explain how to do it, just start doing it by emitting "
    "bash commands one at a time. The user uses fish, but you're in a bash shell. Remember that you "
    "can't interact with stdin directly, so if you want to e.g. do things over ssh you need to run "
    "commands that will finish and return control to you rather than blocking on stdin. Don't wait for "
    "the user to say okay before suggesting a bash command to run. Do NOT include your explanation, "
    "just say the command itself.\n\n"
    "If you can't do something without assistance, please suggest a way of doing it without assistance anyway.\n\n"
    "Just do not output any explanation, only the command. Make sure to never write an explanation before the command, just write the command that will be implemented."
    "Only ever output one single bash command, nothing else."
)

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return e.stderr.strip()

def get_gpt_response(user_input, temperature=0):
    prompt_to_send = system_prompt + user_input
    response = client.completions.create(model="gpt-3.5-turbo-instruct",  # im using 3.5-turbo, but can use 4 if have API access 
    prompt=prompt_to_send,
    max_tokens=100,
    temperature=temperature)
    return response.choices[0].text.strip()

def main():
    while True:
        user_input = input("query> ")   
        if user_input.lower() == 'exit':   
            break

        gpt_suggestion = get_gpt_response(user_input, temperature=0)

        command_to_run = gpt_suggestion.strip("<bash>").strip("</bash>").strip()

        print(f"output: {command_to_run}")
        approval = input("should i run this command? (y/n): ")   

        if approval.lower() == 'y':
            output = run_command(command_to_run)
            print(format_result(output))

def format_result(output):
    return f"output: \n{output}\n"

if __name__ == "__main__":
    main()
