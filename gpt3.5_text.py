import requests
import json
import os

material = input("Name your conversation:\n")
with open (f"./ChatHistory/{material}.md","w",encoding="UTF-8") as S:
    S.write(f"# {material}\n")
    os.system("cls")
    while True:
        requirements = input("USER ")
        S.write("- USER\n"+requirements+ "\n")
        if requirements == "exit":
            break
        # print("hello")
        url = "https://api.openai.com/v1/chat/completions"

        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer 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"
        }

        data = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": f"{requirements}"}],
            "temperature": 0.7
        }

        json_data = json.dumps(data)

        res = requests.post(url, headers=headers, data=json_data)
        content = res.json()
        answer = content.get("choices")[0].get("message").get("content")
        print("GPT  "+answer)
        print("- GPT \n" + answer.encode("UTF-8").decode("UTF-8"),file=S)
    S.close()


# print(res.json()["choices"][0]["text"])   