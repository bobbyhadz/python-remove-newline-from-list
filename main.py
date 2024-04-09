# Remove newline characters from a List in Python

my_list = ['bobby\n', 'hadz\r\n', '\ncom\r\n']

# ✅ Remove leading and trailing newline characters from list
new_list = [item.strip() for item in my_list]
print(new_list)  # 👉️ ['bobby', 'hadz', 'com']

# ---------------------------------------------

# ✅ Remove ALL newline characters from list
new_list = [
    item.replace('\r', '').replace('\n', '')
    for item in my_list
]
print(new_list)  # 👉️ ['bobby', 'hadz', 'com']