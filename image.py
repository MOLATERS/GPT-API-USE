import requests
import json

url = "https://api.openai.com/v1/images/generations"

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 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"
}
dict = {"small":"256x256","medium":"512x512","large":"1024x1024"}

requirments = input("what is your requirments?\n")
Size = input("what size?\n")
if Size not in ["small","medium","large"]:
    Size = "medium"
num = int(input("how many pictures do you want?\n"))
if num < 1 or num > 10:
    num = 1

size = dict[Size]

data = {
    "prompt": f"{requirments}",
    "n":num,
    "size":f"{size}"
}

context = requests.post(url,headers=headers,data=json.dumps(data))

images = []

for item in context.json().get("data"):
    images.append(item.get("url"))

# print(images)    

index = 0

for image in images:
    with open(f"./image/generated_image_{index}.jpg","wb") as f:
        f.write(requests.get(image).content)
        print("file generated")
    index += 1