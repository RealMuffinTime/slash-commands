import requests
import secret_master
import secret_dev

# Here you can set a id for a guild on which you test the bot, you can upload the commands to this specific guild
guild_url = "https://discord.com/api/v8/applications/%s/guilds/<your_guild_id>/commands"
guilds_url = "https://discord.com/api/v8/applications/%s/commands"

# Here in this list you can define the commands you want to upload/update
command_list = [{"name": "a_command_name", "description": "a_command_description"},
                {"name": "a_command_name", "description": "a_command_description"},
                {"name": "a_command_name", "description": "a_command_description"},
                {"name": "a_command_name", "description": "a_command_description"},
                {"name": "a_command_name", "description": "a_command_description"}]

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
    
    # For usage with a master and dev bot, you need to declare them in secret_master.py/secret_dev.py
    print("\nWhich bot version? master/dev")
    bot = input().upper()

    if bot == "MASTER":
        temp_token = secret_master.bot_token
        temp_id = secret_master.bot_id
    elif bot == "DEV":
        temp_token = secret_dev.bot_token
        temp_id = secret_dev.bot_id
    else:
        print("Incorrect token type")

    # 'guild' updates for the specific guild, 'guilds' updates for all guilds
    print("\nWhich url? guild/guilds")
    url = input().upper()

    if url == "GUILD":
        temp_url = guild_url
    elif url == "GUILDS":
        temp_url = guilds_url
    else:
        print("Incorrect url type")
    
    print("\nWhich request type? post/get/delete")
    request_type = input().upper()

    if request_type == "POST":
        for command in command_list:
            print(post_request(temp_url % temp_id, temp_token, command).text)
    elif request_type == "GET":
        print(get_request(temp_url % temp_id, temp_token).text)
    elif request_type == "DELETE":
        print("Which command id?")
        print(delete_request((temp_url % temp_id) + "/" + input(), temp_token).text)
    else:
        print("Incorrect requests type")

    print("\n --- \n")
    print("Again? Y/N")
    i = input().upper()
    if i == "Y" or i == "YES":
        request()


request()
