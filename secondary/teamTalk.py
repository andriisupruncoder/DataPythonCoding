import teamtalk
from tkinter import *

class TeamTalkBot:
    def __init__(self, server, username, password, channel):
        self.server = server
        self.username = username
        self.password = password
        self.channel = channel
        self.client = teamtalk.TeamTalkClient(server, username, password)

    def connect(self):
        self.client.connect()
        self.client.joinChannel(self.channel)

    def send_message(self, message):
        self.client.sendChannelMessage(self.channel, message)

    def open_dialog_box(self):
        root = Tk()
        root.title("TeamTalk Bot")

        label = Label(root, text="Enter message to send:")
        label.pack()

        entry = Entry(root)
        entry.pack()

        def send_message():
            message = entry.get()
            self.send_message(message)
            root.destroy()

        button = Button(root, text="Send", command=send_message)
        button.pack()

        root.mainloop()

if __name__ == "__main__":
    server = "localhost"
    username = "bot"
    password = "password"
    channel = "1"

    bot = TeamTalkBot(server, username, password, channel)
    bot.connect()
    bot.open_dialog_box()