from PIL import Image
import json
import requests


# using pillow library to photo edit
im = Image.open("frog.jpg")
im.rotate(45).show()

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

# determine which users has the most completed tasks
todos_by_user = {}

# increment thru todos of all users
for todo in todos:
    if todo["completed"]:
        try:
            # Increment the existing user's count
            todos_by_user[todo["userId"]] += 1
        except KeyError:
            # This user has not been seen, set count to 1
            todos_by_user[todo["userId"]] = 1

# sort list by number completed
top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)

# max number complete:
max_complete = top_users[0][1]

# create list of users with max number of completions:
users = []
for user, num_complete in top_users:
    if num_complete < max_complete:
        break
    users.append(str(user))

max_users = " and ".join(users)
print(max_users)

s = "s" if len(users) > 1 else ""
print(f"user{s} {max_users} completed {max_complete} TODOs")

# filter out the complete todos of this new list:

def keep(todo):
    is_complete = todo["completed"]
    has_max_count = str(todo["userId"]) in users
    return is_complete and has_max_count

with open("filtered_data_file.json", "w") as data_file:
    filtered_todos = list(filter(keep, todos))
    json.dump(filtered_todos, data_file, indent=2)
    

