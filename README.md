# AI Assistant Telegram Bot

This repository contains the code for an AI-driven Telegram bot that uses the Aiogram framework. The bot is capable of generating responses, managing user limits, handling chat history, and more. 

## Features

- **AI-Powered Responses**: Uses Google's generative AI (Gemini) to generate responses.
- **User Limit Management**: Manages daily usage limits for users.
- **Chat History Management**: Saves and retrieves chat histories.
- **User Profile Management**: Allows users to create and update profiles.
- **Broadcast Messages**: Sends messages to all users or groups.
- **Invoice Handling**: Processes payments to extend user limits.
- **FSM (Finite State Machine)**: Manages states for various user interactions.
- **Callback Queries**: Handles various callback queries for user interactions.

## Installation

To set up the bot, follow these steps:

1. **Clone the repository**:
   ```sh
   git clone https://github.com/chelipika/ai_asistant_tg.git
   cd ai_asistant_tg
   ```

2. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

3. **Set up configuration**:
   - Create a `config.py` file with the following variables:
     ```python
     GEMINI_API_KEY = 'your_gemini_api_key'
     TOKEN = 'your_telegram_bot_token'
     CHANNEL_ID = 'your_channel_id'
     CHANNEL_LINK = 'your_channel_link'
     ```

4. **Run the bot**:
   ```sh
   python main.py
   ```

## Usage

### Commands

- `/start`: Start the bot and greet the user.
- `/reg`: Register a new user profile.
- `/history`: Show the user's chat history.
- `/end`: Clear the user's chat history.
- `/new`: Start a new chat session.
- `/fund`: Extend user limits with a payment.
- `/send_to_all_users`: Send a message to all users.
- `/send_to_all_groups`: Send a message to all groups.

### Callback Queries

- `subchek`: Check subscription status.
- `history_callback`: Show chat history as a message.
- `send_as_file_history`: Send chat history as a file.
- `fundup`: Initiate a payment to extend limits.
- `back`: Go back to the main menu.
- `profile`: Show or create user profile.
- `show_users_profliee`: Show user profile.
- `create_update_profile`: Create or update user profile.

### State Management

The bot uses FSM to manage different states for user interactions:

- **Registration (`Reg` StatesGroup)**:
  - `name`, `Experience`, `Approach`, `Mission`, `Commitment`, `CallToAction`, `ai_name`
  
- **Advertisement Messages (`AdvMsg` StatesGroup)**:
  - `img`, `audio`, `txt`, `inline_link_name`, `inline_link_link`
  
- **Group Messages (`GroupMsg` StatesGroup)**:
  - `img`, `audio`, `txt`, `inline_link_name`, `inline_link_link`
  
- **General (`Gen` StatesGroup)**:
  - `wait`

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

For any questions or support, please contact [chelipika](https://github.com/chelipika).

---

By following the above instructions, you should be able to set up and run your AI Assistant Telegram bot, as well as understand its capabilities and usage.
