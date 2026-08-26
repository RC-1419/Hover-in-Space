# 🚀 Hover in Space

> A simple and engaging space arcade game built with **Python and Pygame**, designed as a fun stress-buster where you navigate a spaceship through incoming meteors and try to achieve the highest possible score.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Pygame](https://img.shields.io/badge/Pygame-Game%20Development-green)
![Status](https://img.shields.io/badge/Status-Complete-success)

---

## 🎮 About the Game

**Hover in Space** is a lightweight 2D arcade game developed using Python and Pygame.

The objective is simple: **control your spaceship, avoid incoming meteors, and survive as long as possible to achieve a high score.**

The game features multiple meteors moving at different speeds and positions, making the gameplay progressively challenging. Your best scores are stored locally so you can keep trying to beat your previous record.

---

## ✨ Features

* 🚀 Spaceship-based 2D gameplay
* ☄️ Multiple incoming meteor obstacles
* 🎮 Keyboard-based player movement
* 🏆 Real-time score tracking
* 📈 Best-score persistence using a local score file
* 🎵 Background music
* 💥 Collision detection
* 🌌 Space-themed background
* ▶️ Simple start screen
* 🛑 Game-over screen
* ⚙️ Configurable game settings

---

## 🕹️ Controls

| Key | Action     |
| --- | ---------- |
| `↑` | Move Up    |
| `↓` | Move Down  |
| `←` | Move Left  |
| `→` | Move Right |

Avoid the meteors and survive as long as possible!

---

## 🛠️ Tech Stack

* **Python**
* **Pygame**

The game uses Pygame for:

* Game window and rendering
* Keyboard input handling
* Sprite/image loading
* Collision detection
* Background music
* Game loop and frame-rate control

---

## 📂 Project Structure

```text
Hover-in-Space/
│
├── images/
│   ├── space.jpg
│   ├── spaceship.png
│   └── meteor.png
│
├── main.py
├── player.py
├── meteors.py
├── settings.py
├── scores.txt
├── game_background_music.mp3
└── README.md
```

### File Description

| File                        | Description                                                                |
| --------------------------- | -------------------------------------------------------------------------- |
| `main.py`                   | Main game loop, event handling, scoring, collision detection and game flow |
| `player.py`                 | Handles spaceship creation, rendering and movement                         |
| `meteors.py`                | Handles meteor creation, positioning and rendering                         |
| `settings.py`               | Contains configurable game settings such as screen dimensions              |
| `scores.txt`                | Stores previous scores                                                     |
| `images/`                   | Contains game graphics                                                     |
| `game_background_music.mp3` | Background music used during gameplay                                      |

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/RC-1419/Hover-in-Space.git
```

### 2. Navigate to the project directory

```bash
cd Hover-in-Space
```

### 3. Install Pygame

```bash
pip install pygame
```

Or:

```bash
python -m pip install pygame
```

---

## ▶️ Run the Game

Start the game using:

```bash
python main.py
```

A game window will open with the **PLAY** button.

Click **PLAY** to begin.

Use the arrow keys to control the spaceship and avoid the incoming meteors.

---

## 🏆 Scoring System

Your score increases continuously while you remain in the game.

When the spaceship collides with a meteor:

1. The current score is saved to `scores.txt`.
2. A **GAME OVER** screen is displayed.
3. The game exits.

The highest score stored in `scores.txt` is displayed as your **BEST SCORE** during gameplay.

---

## 🧠 Game Mechanics

The game is built around a continuous game loop.

### Player

The spaceship can move in four directions:

* Up
* Down
* Left
* Right

Movement is controlled using boolean movement states that are updated through keyboard events.

### Meteors

Multiple meteor objects are created and move across the screen at different speeds.

This creates varying obstacle patterns and requires the player to continuously adjust the spaceship's position.

### Collision Detection

Pygame's rectangle collision detection is used to determine whether the spaceship has collided with a meteor.

```python
player_obj.rect.colliderect(meteor_obj.rect)
```

When a collision occurs, the current score is saved and the game ends.

---

## 🎯 Objective

The goal is to:

> **Survive as long as possible, avoid every meteor, and beat your best score.**

Can you reach a new high score? 🚀

---

## 🔮 Future Improvements

Possible improvements for future versions include:

* [ ] Progressive difficulty
* [ ] Increasing meteor speed over time
* [ ] Power-ups and special abilities
* [ ] Multiple spaceship options
* [ ] Sound effects
* [ ] Pause/resume functionality
* [ ] Restart button after game over
* [ ] Main menu
* [ ] Multiple difficulty levels
* [ ] Improved score and leaderboard system
* [ ] High-score UI
* [ ] Additional levels and environments

---

## 🤝 Contributing

Contributions and suggestions are welcome.

If you would like to improve the game:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Commit your changes
5. Open a Pull Request

---

## 📜 License

This project is intended for educational and personal use.

If you plan to distribute or modify the project, please check the licensing requirements for any third-party assets used in the game.

---

## 👨‍💻 Author

**RC-1419**

GitHub:
https://github.com/RC-1419

---

⭐ If you enjoyed the project, consider giving the repository a star!
