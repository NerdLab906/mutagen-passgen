# 🎲 Mutagen PassGen — Custom Seed Password Generator (codename-"Mutagen-Passgen")

A password generator using **custom seed**, **real-time entropy**, and **symbolic masking**. This project includes dynamic mutation logic and builds passwords that adapt to both time and input.

---

### 🔧 Features

- 🧠 **Rebuilder** — Detects and replaces "dumb" seeds with smarter ones  
- 🔥 **Entropy Engine** — Modifies the seed using current minute and second  
- 🧬 **Mutation Formulas** — Lightweight formulas for post-entropy transformation  
- 🎭 **Symbol Styles** — Three visual styles: `classic`, `chaos`, `mystic`  
- ⏱ **Time-based Rare Symbols** — Injects rare ASCII symbols using current time  

---

### 🚀 How to Use

```bash
python main.py --seed 12345678 --style classic
 
--seed: Your custom numeric seed (7–16 digits)
--style: Password style (classic | chaos | mystic)


### 💀 Deleted Concepts (R.I.P.)

These ideas were part of earlier builds but removed for better stability:

❌ Seed Enhancer — Tried to "fix" dumb seeds (Rebuilder replaced it)

❌ Custom Math (LCM, GCD, SUMMING) — Made seed mutations unstable

❌ Tracker — Early entropy draft, very unstable

❌ Old Mutations — Too chaotic and unpredictable

❌ Twister — Never really worked as intended 


### 🧪 Final Notes

This is my first art-code project.
I started it during the early nights of July.
The project broke completely once, but I rebuilt the architecture from scratch, and now it’s stronger.

I'm 16 years old, learning Python without using libraries, just basic built-in tools and json. I may not be the best at programming, but I love it like I love math and philosophy.

Please don't judge harshly — this is a passion project, and I just want to share it with the world 💛