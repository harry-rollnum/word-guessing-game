import streamlit as st
import random
import string

# List of 5-letter words for the game
WORD_LIST = [
    "apple", "beach", "chair", "dance", "eagle", "flame", "ghost", "house", 
    "image", "joint", "knife", "light", "mouse", "nurse", "ocean", "piano", 
    "queen", "river", "stone", "table", "unity", "video", "water", "youth", 
    "zebra", "alien", "blaze", "cloud", "dream", "earth", "fruit", "globe",
    "heart", "ivory", "jolly", "kite", "lemon", "magic", "noble", "olive", 
    "peace", "quiet", "royal", "solar", "tiger", "urban", "voice", "world", 
    "xerox", "yield", "zesty"
]

# Set page configuration
st.set_page_config(
    page_title="Word Guessing Game",
    page_icon="🎮",
    layout="centered"
)

# Title and instructions
st.title("Word Guessing Game 🎮")
st.markdown("""
#### How to play:
1. Guess the 5-letter word within 6 attempts
2. After each guess, you'll get feedback:
   - 🟩 Green: Correct letter in the correct position
   - 🟨 Yellow: Correct letter in the wrong position
   - ⬛ Gray: Letter not in the word
3. All guesses must be valid 5-letter words
""")

# Initialize session state variables if they don't exist
if 'secret_word' not in st.session_state:
    st.session_state.secret_word = random.choice(WORD_LIST)
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'max_attempts' not in st.session_state:
    st.session_state.max_attempts = 6
if 'guesses' not in st.session_state:
    st.session_state.guesses = []
if 'game_over' not in st.session_state:
    st.session_state.game_over = False
if 'win' not in st.session_state:
    st.session_state.win = False

# Function to reset the game
def reset_game():
    st.session_state.secret_word = random.choice(WORD_LIST)
    st.session_state.attempts = 0
    st.session_state.guesses = []
    st.session_state.game_over = False
    st.session_state.win = False

# Function to evaluate the guess
def evaluate_guess(guess):
    result = []
    secret_word = st.session_state.secret_word
    
    # Create a copy of the secret word to track remaining letters
    remaining_letters = list(secret_word)
    
    # First pass: Find exact matches (green)
    for i, letter in enumerate(guess):
        if i < len(secret_word) and letter == secret_word[i]:
            result.append(("🟩", letter))
            remaining_letters[i] = '_'  # Mark as processed
        else:
            result.append(("", letter))  # Placeholder for second pass
            
    # Second pass: Find letters in wrong positions (yellow) or not in word (gray)
    for i, (color, letter) in enumerate(result):
        if color == "":  # Skip already matched letters
            if letter in remaining_letters:
                result[i] = ("🟨", letter)
                remaining_letters[remaining_letters.index(letter)] = '_'  # Mark as processed
            else:
                result[i] = ("⬛", letter)
                
    return result

# Game UI
col1, col2 = st.columns([3, 1])

with col1:
    # Input field for guesses
    guess = st.text_input("Enter your guess (5 letters):", key="guess_input", disabled=st.session_state.game_over)

with col2:
    # Submit button
    if st.button("Submit", disabled=st.session_state.game_over):
        guess = guess.lower().strip()
        
        # Validate guess
        if len(guess) != 5:
            st.error("Your guess must be exactly 5 letters.")
        elif not guess.isalpha():
            st.error("Your guess must contain only letters.")
        else:
            # Process valid guess
            st.session_state.attempts += 1
            evaluated_guess = evaluate_guess(guess)
            st.session_state.guesses.append(evaluated_guess)
            
            # Check win condition
            if guess == st.session_state.secret_word:
                st.session_state.win = True
                st.session_state.game_over = True
            
            # Check lose condition
            if st.session_state.attempts >= st.session_state.max_attempts and not st.session_state.win:
                st.session_state.game_over = True

# Display game status
st.markdown(f"### Attempts: {st.session_state.attempts}/{st.session_state.max_attempts}")

# Display guesses with colored feedback
if st.session_state.guesses:
    st.markdown("### Your Guesses:")
    for guess in st.session_state.guesses:
        guess_display = ""
        for color, letter in guess:
            guess_display += f"{color} {letter.upper()} "
        st.markdown(guess_display)

# Display game result
if st.session_state.game_over:
    if st.session_state.win:
        st.success(f"🎉 Congratulations! You guessed the word: {st.session_state.secret_word.upper()}")
        st.balloons()
    else:
        st.error(f"Game Over! The word was: {st.session_state.secret_word.upper()}")

# New game button
if st.button("New Game"):
    reset_game()

# For debugging (can be removed in production)
if st.checkbox("Show secret word (for testing)"):
    st.write(f"Secret word: {st.session_state.secret_word}")

