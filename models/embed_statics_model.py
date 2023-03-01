import discord

from services.environment_service import EnvService

BOT_NAME = EnvService.get_custom_bot_name()


class EmbedStatics:
    def __init__(self):
        pass

    @staticmethod
    def get_invalid_api_response_embed(e):
        embed = discord.Embed(
            title="The API returned an invalid response",
            description=f"**{e.status}: {e.message}**",
            color=discord.Color.red(),
        )
        return embed

    @staticmethod
    def get_invalid_value_embed(e):
        embed = discord.Embed(
            title="Invalid value",
            description=f"**{str(e)}**",
            color=discord.Color.red(),
        )
        return embed

    @staticmethod
    def get_general_error_embed(e):
        embed = discord.Embed(
            title="An error occurred",
            description=f"**{str(e)}**",
            color=discord.Color.red(),
        )
        return embed

    @staticmethod
    def generate_end_embed():
        embed = discord.Embed(
            title="Conversation Ended",
            description=f"This conversation has ended. You can start a new one with `/gpt converse`",
            color=0x808080,
        )
        return embed

    @staticmethod
    def generate_conversation_embed(conversation_threads, thread, opener, overrides):
        # Generate a nice looking embed for the above text
        embed = discord.Embed(
            title="Conversation started",
            description=f"Conversation started with {BOT_NAME}",
            color=0x808080,
        )
        embed.add_field(
            name="Model",
            value=f"The model used is **{conversation_threads[thread.id].model}**",
        )
        embed.add_field(
            name="Overrides",
            value=f"**temp={overrides['temperature']}**, **top_p={overrides['top_p']}**"
            f", **freq. penalty={overrides['frequency_penalty']}**, **pres. penalty={overrides['presence_penalty']}**\n",
        )
        embed.add_field(
            name="End the conversation",
            value="End the conversation by saying `end`, or clicking the red 'End Conversation' button\n\n",
            inline=False,
        )
        embed.add_field(
            name="Ignoring Messages",
            value="If you want GPT3 to ignore your messages, start your messages with `~`\n\n",
            inline=False,
        )
        return embed

    @staticmethod
    def generate_opener_embed(opener):
        embed = discord.Embed(
            title="Opening Prompt",
            description=f"{opener}",
            color=0x808080,
        )
        return embed

    @staticmethod
    def get_index_set_success_embed(price="Unknown"):
        embed = discord.Embed(
            title="Index Added",
            description=f"This index can now be queried and loaded with `/index query` and `/index load`\n\n||Total cost: {round(float(price), 6)}||",
            color=discord.Color.green(),
        )
        # thumbnail of https://i.imgur.com/7JF0oGD.png
        embed.set_thumbnail(url="https://i.imgur.com/7JF0oGD.png")
        return embed

    @staticmethod
    def get_index_set_failure_embed(message):
        embed = discord.Embed(
            title="Index Add",
            description=f"Index add failed. {message}",
            color=discord.Color.red(),
        )
        # thumbnail of https://i.imgur.com/VLJ32x7.png
        embed.set_thumbnail(url="https://i.imgur.com/VLJ32x7.png")
        return embed

    @staticmethod
    def get_index_load_success_embed(name=None):
        embed = discord.Embed(
            title="Index Loaded" if not name else f"Index {name} loaded",
            color=discord.Color.green(),
        )
        # thumbnail of https://i.imgur.com/7JF0oGD.png
        embed.set_thumbnail(url="https://i.imgur.com/7JF0oGD.png")
        return embed

    @staticmethod
    def get_index_load_failure_embed(message):
        embed = discord.Embed(
            title="Index load",
            description=f"Index load failed. {message}",
            color=discord.Color.red(),
        )
        # thumbnail of https://i.imgur.com/VLJ32x7.png
        embed.set_thumbnail(url="https://i.imgur.com/VLJ32x7.png")
        return embed

    @staticmethod
    def get_index_query_failure_embed(message):
        embed = discord.Embed(
            title="Index query",
            description=f"Index query failed. {message}",
            color=discord.Color.red(),
        )
        # thumbnail of https://i.imgur.com/VLJ32x7.png
        embed.set_thumbnail(url="https://i.imgur.com/VLJ32x7.png")
        return embed

    @staticmethod
    def get_index_compose_success_embed(price="Unknown"):
        embed = discord.Embed(
            title="Indexes Composed",
            description=f"Indexes composed successfully, you can query and load this index with `/index query` and `/index load`\n\n||Total cost: {round(float(price), 6)}||",
            color=discord.Color.green(),
        )
        # thumbnail of https://i.imgur.com/7JF0oGD.png
        embed.set_thumbnail(url="https://i.imgur.com/7JF0oGD.png")
        return embed

    @staticmethod
    def get_index_compose_failure_embed(message):
        embed = discord.Embed(
            title="Index Compose",
            description=f"Index compose failed. {message}",
            color=discord.Color.red(),
        )
        # thumbnail of https://i.imgur.com/VLJ32x7.png
        embed.set_thumbnail(url="https://i.imgur.com/VLJ32x7.png")
        return embed

    @staticmethod
    def get_index_compose_progress_embed():
        embed = discord.Embed(
            title="Index Compose",
            description=f"Your index composition is running, this may take a while.",
            color=discord.Color.blurple(),
        )
        # thumbnail of https://i.imgur.com/VLJ32x7.png
        embed.set_thumbnail(url="https://i.imgur.com/txHhNzL.png")
        return embed

    @staticmethod
    def get_index_rename_success_embed(original, renamed):
        embed = discord.Embed(
            title=f"Index Rename",
            description=f"Index {original} renamed to {renamed}",
            color=discord.Color.green(),
        )
        # thumbnail of https://i.imgur.com/7JF0oGD.png
        embed.set_thumbnail(url="https://i.imgur.com/7JF0oGD.png")
        return embed

    @staticmethod
    def get_index_rename_failure_embed(original, renamed, message):
        embed = discord.Embed(
            title="Index Rename",
            description=f"Index rename from {original} to {renamed} failed. {message}",
            color=discord.Color.red(),
        )
        # thumbnail of https://i.imgur.com/VLJ32x7.png
        embed.set_thumbnail(url="https://i.imgur.com/VLJ32x7.png")
        return embed

    @staticmethod
    def get_edit_command_output_embed(response_text):
        embed = discord.Embed(
            title="GPT3 Edits",
            description=f"{response_text}",
            color=discord.Color.light_grey(),
        )
        return embed

    @staticmethod
    def get_search_failure_embed(message):
        embed = discord.Embed(
            title="AI-Assisted Search",
            description=f"An error occured while performing search: {message}",
            color=discord.Color.red(),
        )
        # thumbnail of https://i.imgur.com/VLJ32x7.png
        embed.set_thumbnail(url="https://i.imgur.com/VLJ32x7.png")
        return embed

    @staticmethod
    def get_search_redo_progress_embed():
        embed = discord.Embed(
            title="AI-Assisted Search",
            description=f"Your original search request is being redone. This may take a while.",
            color=discord.Color.blurple(),
        )
        # thumbnail of https://i.imgur.com/VLJ32x7.png
        embed.set_thumbnail(url="https://i.imgur.com/txHhNzL.png")
        return embed

    @staticmethod
    def get_conversation_shared_embed(url):
        embed = discord.Embed(
            title="Conversation Shared",
            description=f"You can access your shared conversation at: {url}",
            color=discord.Color.blurple(),
        )
        # thumbnail of https://i.imgur.com/VLJ32x7.png
        embed.set_thumbnail(url="https://i.imgur.com/8OIZc1A.png")
        return embed

    @staticmethod
    def get_conversation_share_failed_embed(message):
        embed = discord.Embed(
            title="Conversation Sharing",
            description=f"Conversation sharing failed: " + message,
            color=discord.Color.red(),
        )
        # thumbnail of https://i.imgur.com/VLJ32x7.png
        embed.set_thumbnail(url="https://i.imgur.com/VLJ32x7.png")
        return embed

    @staticmethod
    def build_index_progress_embed():
        embed = discord.Embed(
            title="Index Service",
            description="Indexing...",
            color=discord.Color.blurple(),
        )
        embed.set_thumbnail(url="https://i.imgur.com/txHhNzL.png")
        return embed

    @staticmethod
    def build_index_query_progress_embed(query):
        embed = discord.Embed(
            title="Index Service",
            description=f"Query:\n`{query}`\nQuerying...",
            color=discord.Color.blurple(),
        )
        embed.set_thumbnail(url="https://i.imgur.com/txHhNzL.png")
        return embed

    @staticmethod
    def build_index_query_success_embed(query, price="Unknown"):
        embed = discord.Embed(
            title="Index Service",
            description=f"Query:\n`{query}`\nThe index query was successful.\n\n||Total cost: {round(float(price), 6)}||",
            color=discord.Color.green(),
        )
        # thumbnail of https://i.imgur.com/7JF0oGD.png
        embed.set_thumbnail(url="https://i.imgur.com/7JF0oGD.png")
        return embed
