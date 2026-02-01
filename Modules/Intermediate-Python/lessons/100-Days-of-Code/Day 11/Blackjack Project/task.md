## Choose your difficulty

- **Normal 😎**: Use all hints below to complete the project.
- **Hard 🤔**: Use only **Hints 1, 2, 3** to complete the project.
- **Extra Hard 😭**: Use only **Hints 1 & 2** to complete the project.
- **Expert 🤯**: Use only **Hint 1** to complete the project.

---

## Our Blackjack Game House Rules

- The deck is unlimited in size.
- There are no jokers.
- The Jack/Queen/King all count as 10.
- The Ace can count as 11 or 1.
- Use the following list as the deck of cards:

```python
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
```

---

## Tasks / Hints

### **HINT 1** — Play Blackjack online and review the completed demo
<!-- TODO: HINT 1 -->

- [Play Blackjack (Washington Post)](https://games.washingtonpost.com/games/blackjack/)
- [Completed Blackjack Demo](https://appbrewery.github.io/python-day11-demo/)

---

### **HINT 2** — Read requirements and create a flowchart
<!-- TODO: HINT 2 -->

- [Blackjack Program Requirements](http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF)

Create your own flowchart for the program.

---

### **HINT 3** — Review provided flowchart
<!-- TODO: HINT 3 -->

- [Download Provided Flowchart (PDF)](https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt)

---

### **HINT 4** — Implement `deal_card()`
<!-- TODO: HINT 4 -->

Create a function that returns a random card.

```python
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
```

---

### **HINT 5** — Deal initial cards
<!-- TODO: HINT 5 -->

Deal two cards to both user and computer.

```python
user_cards = []
computer_cards = []
```

---

### **HINT 6** — Implement `calculate_score()`
<!-- TODO: HINT 6 -->

Create a `calculate_score()` function that:
- takes a list of cards as input
- returns the total using `sum()`

---

### **HINT 7** — Handle blackjack
<!-- TODO: HINT 7 -->

If the hand is a blackjack (Ace + 10), return `0`.

---

### **HINT 8** — Handle Ace adjustment
<!-- TODO: HINT 8 -->

If the score exceeds 21:
- replace `11` with `1`

Reference:
- [Python List Methods](https://developers.google.com/edu/python/lists#list-methods)

---

### **HINT 9** — End game conditions
<!-- TODO: HINT 9 -->

End the game if:
- user or computer has blackjack (`0`)
- user score exceeds 21

---

### **HINT 10** — User draw decision
<!-- TODO: HINT 10 -->

Ask the user if they want another card:
- Yes → deal a card
- No → end turn

---

### **HINT 11** — Recalculate score
<!-- TODO: HINT 11 -->

Recalculate scores after each draw until the game ends.

---

### **HINT 12** — Computer drawing logic
<!-- TODO: HINT 12 -->

Computer keeps drawing cards while score is below 17.

---

### **HINT 13** — Implement `compare()`
<!-- TODO: HINT 13 -->

Create `compare(user_score, computer_score)` to determine the winner.

---

### **HINT 14** — Restart game
<!-- TODO: HINT 14 -->

Ask the user if they want to restart:
- clear console
- restart game
- show logo from `art.py`
