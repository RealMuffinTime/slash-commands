# Here you can specify bot ids and tokens
accounts = [
    ["<botid>", "Bot <discordbottoken>"],  # bot 1
    ["<anotherbotid>", "Bot <anotherdiscordbottoken>"]  # bot 2 or more
]

# Here you can set ids for specific guilds to update commands for these
guilds = ["<guildid>"]

# Here in this list you can define the commands you want to upload/update
post_list = [
    {"name": "<command name 1>", "description": "<command description 1>", "type": 1},  # command 1
    {"name": "<command name 2>", "description": "<command description 2>", "type": 1}  # command 2 or more
]

# Here you can specify ids you got from get commands to delete commands
delete_list = ["<commandid>"]
