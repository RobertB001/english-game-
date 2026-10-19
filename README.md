# English Game-

A simple console game in Python that helps you practice English words by speaking.

## About

The game shows you a word in Polish, and you have to say its English translation out loud. The program records your voice, recognizes what you said, and checks if your answer is correct.

## How to play

1. Choose a difficulty level: easy, medium or hard.
2. A Polish word appears on the screen.
3. Press Enter and say the word in English.
4. A correct answer gives you points, a wrong one costs you a life.
5. The game ends when you lose all 3 lives or finish all the words.


## Requirements

- Python 3.8+
- Microphone
- Internet connection

## Installation

Before running the game, you need to install the required libraries. Without them, the game will not work. Run this command in your terminal:


pip install sounddevice scipy SpeechRecognition googletrans==4.0.0rc1

- `sounddevice` records sound from the microphone
- `scipy` saves the recording as a .wav file
- `SpeechRecognition` turns your voice into text
- `googletrans` translates words from Polish to English (version 4.0.0rc1 is required, newer versions will not work with this code)

