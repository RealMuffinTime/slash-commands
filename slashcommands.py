import importlib
import requests
import settings

version = "1.0.0"


def post_request(url, token, json):
    post = requests.post(url, headers={"Authorization": token}, json=json)
    return post


def get_request(url, token):
    get = requests.get(url, headers={"Authorization": token})
    return get


def delete_request(url, token):
    delete = requests.delete(url, headers={"Authorization": token})
    return delete


def request():
    print(f"Running script version {version}.\n")

    accounts = []
    for account in range(len(settings.accounts)):
        accounts.append(str(account))
    # you need to declare accounts in settings.py
    print(f"Which account? {'/'.join(accounts)}")
    for account in accounts:
        print(f"{account} - {settings.accounts[int(account)][0]}")
    account = input().lower()
    if account in accounts:
        account = settings.accounts[int(account)]
        print(f"Using account {account[0]}.\n")
    else:
        print("Invalid account selection. This request will not execute.\n")

    # 'guild' updates for the specific guild, 'guilds' updates for all guilds
    print("Use one guild or all guilds? guild/guilds")
    url = input().lower()
    if url == "guild":
        guilds = []
        for guild in range(len(settings.guilds)):
            guilds.append(str(guild))
        print(f"Using guild. Which guild do you want to use? {'/'.join(guilds)}")
        for guild in guilds:
            print(f"{guild} - {settings.guilds[int(guild)]}")
        guild = input().lower()
        if guild in guilds:
            url = f"https://discord.com/api/v8/applications/{account[0]}/guilds/{settings.guilds[int(guild)]}/commands"
            print(f"Using guild {settings.guilds[int(guild)]}.\n")
        else:
            print("Invalid guild selection. This request will not execute.\n")
    elif url == "guilds":
        url = f"https://discord.com/api/v8/applications/{account[0]}/commands"
        print("Using all guilds.\n")
    else:
        print("Invalid answer. This request will not execute.\n")

    # select which action you want to do
    print("Which type of request? post/get/delete")
    request_type = input().lower()

    if request_type == "post" or request_type == "p":
        print("Do you really want to post these commands? yes/no")
        for command in settings.post_list:
            print(command)
        post = input().lower()
        if post == "y" or post == "yes":
            for command in settings.post_list:
                try:
                    response = post_request(url, account[1], command).text
                    print(f"Posted {command}." + response)
                except:
                    print(f"Failed posting {command}.")
            print()
        else:
            print("Did not post commands. This request will not execute.\n")

    elif request_type == "get" or request_type == "g":
        try:
            response = get_request(url, account[1]).text.strip("\n")
            print(f"Successfully retrieved information: {response}\n")
        except:
            print(f"Failed retrieving information.\n")

    elif request_type == "delete" or request_type == "d":
        print("Do you really want to delete these commands? yes/no")
        for command in settings.delete_list:
            print(command)
        delete = input().lower()
        if delete == "y" or delete == "yes":
            for command in settings.delete_list:
                try:
                    response = delete_request(url + "/" + command, account[1]).text
                    print(f"Successfully posted {command}." + response)
                except:
                    print(f"Failed deleting {command}.")
            print()
        else:
            print("Did not delete commands. This request will not execute.\n")

    else:
        print("Invalid requests type. This request will not execute.\n")

    print("\nExecute script again? yes/no")
    script = input().lower()
    if script == "y" or script == "yes":
        importlib.reload(settings)
        print("Reloaded settings file.")
        request()


request()
