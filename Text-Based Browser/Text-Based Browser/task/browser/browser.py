# import sys
# import os
# import requests
# from bs4 import BeautifulSoup
#
#
# path = ""
# stack = []
# sites_amount = 0
#
#
# def check_arguments():
#     global path
#     args = sys.argv
#     if len(args) > 1:
#         try:
#             os.mkdir(args[1])
#             path = args[1] + "/"
#             # os.chdir(args[1])
#         except FileExistsError:
#             path = args[1] + "/"
#             # os.chdir(args[1])
#
#
# def check_site(sites):
#     # print(sites)
#     dot_id = 0
#     global path
#     if "." in sites:
#         for i in range(len(sites)):
#             if sites[i] == ".":
#                 dot_id = i
#         url = sites[0:dot_id]
#     else:
#         url = sites
#     file_name_path = path + url.lstrip("https://")  # + ".txt"
#     file_name = url.lstrip("https://")
#     # print(file_name)
#     if sites in stack:
#         file = open(path + file_name, "r")
#         print(file.read())
#         file.close()
#     else:
#         if not ("." in sites):
#             print("Error: Incorrect URL")
#         else:
#             if not ("https://" in sites):
#                 sites = "https://" + sites
#             send_request(sites, file_name_path, file_name)
#
#
# def send_request(url, file_name, file_name_2):
#     global sites_amount
#     # print(url)
#     tags = {'[document]', 'head', 'script', 'style', 'body', 'html', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'title', 'table', 'div', 'li', 'form',}
#     file = open(file_name, "w")
#     file2 = open(file_name + "_windows", "w")
#     stack.append(file_name_2)
#     r = requests.get(url)
#     soup = BeautifulSoup(r.text, 'html.parser')
#     soup.prettify()
#     html = soup.find_all('p')
#     text = ""
#     for lines in range(len(html)):
#         print(soup.find_all('p')[lines].get_text())
#         text += soup.find_all('p')[lines].get_text() + "\n"
#     file.write(text)
#     file2.write(text)
#     sites_amount += 1
#     # print(stack)
#     file2.close()
#     file.close()
#
#
# check_arguments()
# while True:
#     site = input()
#     if site == "exit":
#         break
#     elif site == "back":
#         if sites_amount == 1:
#             check_site(str(stack[sites_amount - 1]))
#         elif sites_amount > 1:
#             check_site(str(stack[sites_amount - 2]))
#         continue
#     check_site(site)


from sys import argv
from os import mkdir
import requests
from bs4 import BeautifulSoup


def make_dir(dir_name):
    try:
        mkdir(dir_name)
    except FileExistsError:
        print(f"Directory {dir_name} already exists")


def get_tab(dir_name, tab_name):
    try:
        with open(f'./{dir_name}/{tab_name}', 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "Error: Incorrect URL"


def save_tab(dir_name, tab_name, tab_text):
    with open(f"./{dir_name}/{tab_name}", 'w') as f:
        f.write(tab_text)


def get_html(url):
    if not url.startswith('https://'):
        url = 'https://' + url
    r = requests.get(url, )
    return r.content if r else "Failed"


def parse_html(html_file):
    buf = ''
    tags = ['p', 'a', 'ul', 'ol', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'title']
    soup = BeautifulSoup(html_file, 'html.parser')
    for t in soup.find_all(tags):
        buf = buf + t.get_text() + '\n'
    return buf


directory_ = argv[1]
make_dir(directory_)
while True:
    user_input = input()
    if user_input == 'exit':
        break
    if '.' not in user_input:
        print(get_tab(directory_, user_input))
        continue

    html_ = get_html(user_input)
    if html_ == "Failed":
        print("Error: Incorrect URL")
        continue
    file_ = parse_html(html_)
    print(file_)
    save_tab(directory_, user_input.split('.')[0], file_)
