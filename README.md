# BookBot 📖🤖

**BookBot** is a command-line utility written in Python that automates the analysis of entire books. It parses `.txt` files to count total words, track individual character frequencies, and output a structured analysis report directly to your terminal. 

This repository represents my very first project built while completing the backend engineering curriculum on [Boot.dev](https://www.boot.dev).

---

## 🚀 Features

* **Total Word Counting**: Quickly calculates exactly how many words are contained in any text file.
* **Character Frequency Breakdown**: Counts how many times every character appears (case-insensitive) to provide an analytical footprint of the text.
* **Automated Data Sorting**: Automatically filters out non-alphabetical characters and sorts letters by highest-to-lowest frequency.
* **Clean Terminal Reports**: Outputs clean, reader-friendly analytical summaries for any book provided.

---

## 🛠️ Tech Stack

* **Language:** Python 3.x (100%)
* **Environment:** Command Line Interface (CLI)

---

## 📁 Repository Structure

```text
bookbot/
│
├── books/                 # Folder containing your .txt books (e.g., frankenstein.txt)
├── main.py                # Main application entry point & report orchestrator
├── stats.py               # Core analysis logic (counting functions, sorting logic)
├── .gitignore             # Standard git exclusions (e.g., __pycache__/)
└── README.md              # Project documentation
```

---

## 📦 Getting Started

### Prerequisites
Make sure you have [Python 3](https://python.org) installed on your machine. You can verify this by running:
```bash
python3 --version
```

### Installation
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com
   ```
2. Navigate into the project directory:
   ```bash
   cd bookbot
   ```
3. Create a `books/` directory to store your text files:
   ```bash
   mkdir books
   ```
4. Place a plain text file (such as Mary Shelley's *Frankenstein* from [Project Gutenberg](https://gutenberg.org)) inside the `books/` folder and name it `frankenstein.txt`.

---

## 💻 Usage

To run BookBot and analyze your file, execute the `main.py` script from your root directory:

```bash
python3 main.py
```

### Example Output
When executed, BookBot will output a structured report resembling the following format:

```text
--- Begin report of books/frankenstein.txt ---
77986 words found in the document

The 'e' character was found 46043 times
The 't' character was found 30365 times
The 'a' character was found 26743 times
...
The 'z' character was found 243 times
--- End report ---
```

---

## 🧑‍💻 Contributing

As this is a foundational project for my [Boot.dev](https://www.boot.dev) portfolio, contributions are not actively being accepted, but feel free to fork the repository to experiment with your own text analysis features!
