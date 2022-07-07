import requests
import settings

version = "1.0.0"


guild_url = f"https://discord.com/api/v8/applications/%s/guilds/{settings.guild_id}/commands"
guilds_url = "https://discord.com/api/v8/applications/%s/commands"


temp_id = ""
temp_token = ""
temp_url = ""


def post_request(url, token, json):
    post = requests.post(url, headers={"Authorization": "Bot " + token}, json=json)
    return post


def get_request(url, token):
    get = requests.get(url, headers={"Authorization": "Bot " + token})
    return get


def delete_request(url, token):
    delete = requests.delete(url, headers={"Authorization": "Bot " + token})
    return delete


def request():
    global temp_token
    global temp_url
    global temp_id

    # for usage with a master and dev bot, you need to declare them in settings.py
    print("\nWhich bot version? master/dev")
    bot = input().lower()

    if bot == "master":
        temp_token = settings.master_token
        temp_id = settings.master_id
    elif bot == "dev":
        temp_token = settings.dev_token
        temp_id = settings.dev_id
    else:
        print("Incorrect bot version type")

    # 'guild' updates for the specific guild, 'guilds' updates for all guilds
    print("\nWhich url? guild/guilds")
    url = input().lower()

    if url == "guild":
        temp_url = guild_url
    elif url == "guilds":
        temp_url = guilds_url
    else:
        print("Incorrect url type.")

    print("\nWhich request? post/get/delete")
    request_type = input().lower()

    if request_type == "post":
        for command in settings.command_list:
            print(post_request(temp_url % temp_id, temp_token, command).text)
    elif request_type == "get":
        print(get_request(temp_url % temp_id, temp_token).text)
    elif request_type == "delete":
        print("\nYou want do delete these commands? yes/no")
        if input().lower() == "yes":
            for command in settings.delete_list:
                print(delete_request((temp_url % temp_id) + "/" + command, temp_token).text)
        else:
            print("Did not delete commands.")
    else:
        print("Incorrect requests type.")

    print("\n --- \n")
    print("Again? y/n")
    i = input().lower()
    if i == "y" or i == "yes":
        request()


request()
