from slacker import Slacker

slack = Slacker('<xoxb-2321419546114-2318745410245-BCblO7rMxP4SHPeYT7cX9bEB>')

# Send a message to #general channel
slack.chat.post_message('#stock', 'Hello fellow slackers!')

