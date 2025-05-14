# Word Guessing Game

A Wordle-like word guessing game built with Python and Streamlit. Guess the five-letter word within six attempts!

## Demo

The game can be played online at: [Link will be available after Streamlit deployment]

## Features

- Random selection from a list of 5-letter words
- Visual feedback with colored tiles (green, yellow, gray)
- Six attempts to guess the word
- Input validation
- Win/lose conditions
- Simple and intuitive UI
- New game functionality

## How to Play

1. Guess the 5-letter word within 6 attempts
2. After each guess, you'll get feedback:
   - 🟩 Green: Correct letter in the correct position
   - 🟨 Yellow: Correct letter in the wrong position
   - ⬛ Gray: Letter not in the word
3. All guesses must be valid 5-letter words

## Setup Instructions

### Local Setup

1. Clone this repository:
   ```
   git clone https://github.com/[your-username]/word-guessing-game.git
   cd word-guessing-game
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Run the game:
   ```
   streamlit run word_guessing_game.py
   ```

4. Open your browser and navigate to `http://localhost:8501`

### Streamlit Cloud Deployment

This application can also be deployed to Streamlit Cloud:

1. Fork this repository to your GitHub account
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Sign in with your GitHub account
4. Create a new app, selecting this repository and the main file `word_guessing_game.py`
5. Your app will be deployed and available at a public URL

## Technology Stack

- Python 3.x
- Streamlit for the web interface

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgements

- Built as a learning project for web-based game development using Python
- Inspired by the popular word game Wordle

