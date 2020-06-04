from discord.ext import commands
from difflib import SequenceMatcher
import random

from token import load_token

SERVER_TOKEN = '551153505734361098'
SERVER_NAME = 'FoxtrotDefense Multigaming'


class Bot(commands.Bot):

    def __init__(self, command_prefix="!"):
        super(Bot, self).__init__(command_prefix)
        self.voice_client = None

        self.dicks_being_sucked = []

        self.possible_messages = {
            "do nogi": self.do_nogi,
            "zapraszam bota do testu": self.do_nogi,
            "noga": self.do_nogi,
            "do budy": self.do_budy,
            "daj glos": self.daj_glos,
            "ssij pale": self.ssij,
            "ssij": self.ssij,
            "ssij kutasa": self.ssij,
            "obciagaj": self.ssij,
            "do miecza": self.ssij
        }

        token = load_token()
        self.run(token)

    # region Events
    async def on_ready(self):
        print(f"Zalogowano bota jako {self}")
        """for guild in self.guilds:
            if guild.name == SERVER_NAME:
                print(*[x.name for x in guild.members])"""

    async def on_message(self, message):
        if message.author == self.user:
            return

        await self.interpret_message(message)

        """if message.content.startswith('Do nogi kundlu'):
            await message.channel.send('Juz biegne Panie!')
            channel = message.author.voice.channel
            self.voice_client = await channel.connect()
        if message.content.startswith('Do budy'):
            await self.voice_client.disconnect()
            await message.channel.send('Wypierdalam juz przepraszam')
        if message.content.startswith('Czemu kurwo mozesz tylko tutaj pisac'):
            await message.channel.send('Nie wiem jestem bezwartosciowym kalem')"""

    # endregion

    # region Commands
    @commands.command(name="zamknij morde")
    async def zamknij_morde(self, ctx):
        print("dostalem rozkaz")

    async def do_nogi(self, message):
        await message.channel.send('Juz biegne Panie!')
        channel = message.author.voice.channel
        self.voice_client = await channel.connect()

    async def do_budy(self, message):
        await self.voice_client.disconnect()
        await message.channel.send('Wypierdalam juz przepraszam')

    async def daj_glos(self, message):
        await message.channel.send('Hau hau hau jestem psem',)

    async def ssij(self, message):
        sucking_messages = [f"O boze {message.author} jaki skurwiel", f"Dobrze {message.author}, wylizac twarog?"]

        if "Zues" not in message.author.name:
            sucking_messages.append(f"Moze nie taki duzy jak mojego taty, ale ok")

        if "Punky" in message.author.name:
            response = "Przystepuje do minety"
        elif "Lernan" in message.author.name:
            response = "Ty to akurat mozesz mi zassac"
        elif "Adik" in message.author.name:
            response = "Adis, Tobie zawsze"
        else:
            response = random.choice(sucking_messages)

        await message.channel.send(response)

    # endregion

    async def interpret_message(self, message):

        print(f'Received message "{message.content}"')

        best_match = None
        best_match_ratio = 0
        for possible_message in self.possible_messages:
            possible_ratio = SequenceMatcher(None, possible_message, message.content).ratio()
            # print(f'Matching ratio calculated for "{possible_message}" = {possible_ratio}')
            if possible_ratio > best_match_ratio:
                best_match = possible_message
                best_match_ratio = possible_ratio

        print(f'Best match found - "{best_match}"')

        minimal_ratio = 0.4

        if best_match_ratio > minimal_ratio:
            function = self.possible_messages[best_match]
            await function(message)

        else:
            print(f"Matching command (with ratio above minimal {minimal_ratio}) not found")