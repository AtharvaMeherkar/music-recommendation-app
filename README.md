# 🎵 AI Vibe Generator 🎶

### An Intelligent Music Recommendation Engine with Python & Streamlit

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/scikit--learn-1.x-F89939?style=for-the-badge&logo=scikit-learn&logoColor=white)

</div>

> This project is an intelligent music discovery application that creates custom Bollywood playlists based on the "vibe" of songs you love. It uses a **content-based filtering** model, analyzing the core musical features of songs—such as danceability, energy, and valence—to provide highly relevant and personalized recommendations.

---

## 🚀 Live Demo & Preview

**Interact with the live application here:**

### **[PROJECT LIVE](https://vibe-generator.streamlit.app/)**


## 📋 Table of Contents
- [✨ Key Features](#-key-features)
- [🧠 How It Works: The Recommendation Engine](#-how-it-works-the-recommendation-engine)
- [🛠️ Tech Stack & Architecture](#️-tech-stack--architecture)
- [📁 Project Structure](#-project-structure)
- [⚙️ Getting Started](#️-getting-started)
- [💡 Future Improvements](#-future-improvements)
- [📞 Contact](#-contact)

---

## ✨ Key Features

-   **Vibe-Based Recommendations:** Go beyond single-song suggestions. Select multiple tracks to create a "vibe vector," and the AI generates a playlist matching that unique mood.
-   **Content-Based Filtering:** The core recommendation logic uses **Cosine Similarity** on scaled musical features (e.g., danceability, energy, valence) to mathematically find songs with a similar audio DNA.
-   **Interactive & Attractive UI:** Built with Streamlit for a clean, fast, and user-friendly experience. Recommendations are displayed in modern, stylish cards with placeholder album art.
-   **Export to Music Platforms:** Generated playlists can be instantly searched for on **YouTube Music** or **Spotify** with a single click, bridging the gap between discovery and listening.
-   **Robust Data Handling:** The app uses Pandas for efficient data loading and preprocessing, including cleaning column names and handling missing data to prevent errors.
-   **Optimized Performance:** Leverages Streamlit's caching (`@st.cache_data`) to load and process the dataset only once, ensuring the app is fast and responsive on subsequent visits.

---

## 🧠 How It Works: The Recommendation Engine

This application doesn't just guess; it uses a mathematical approach to "understand" the music.

**`[Song Selections]` ➔ `[Feature Extraction]` ➔ `[Vibe Vector Creation]` ➔ `[Cosine Similarity]` ➔ `[Ranked Playlist]`**

1.  **Feature Extraction:** For every song in the dataset, we extract its core musical features provided by Spotify (e.g., `danceability`, `energy`, `acousticness`). These features are scaled to a common range (0 to 1) using `MinMaxScaler` so that no single feature can unfairly dominate the results.

2.  **Vibe Vector Creation:** When you select your songs, the application finds their corresponding feature sets and calculates the **average vector**. This new vector represents the mathematical "center" of your chosen vibe.

3.  **Cosine Similarity:** The recommendation engine then calculates the cosine similarity—a measure of similarity between two non-zero vectors—between your unique "vibe vector" and every other song in the dataset. A score closer to 1 means the songs are very similar in their musical features.

4.  **Ranked Playlist:** The app sorts all songs by their similarity score in descending order, filters out the songs you already selected, and presents the top 9 results as your new playlist.

---

## 🛠️ Tech Stack & Architecture

| Technology | Role |
| :--- | :--- |
| **Python** | The core programming language for all application logic. |
| **Streamlit** | The framework used to build and serve the entire interactive web application and UI components. |
| **Pandas** | The backbone for all data operations: loading the CSV, data manipulation, and aggregation. |
| **Scikit-learn** | Used for scaling the musical features (`MinMaxScaler`) and calculating the similarity score (`cosine_similarity`). |

---

## 📁 Project Structure

The project is organized with a clean and scalable structure:

```
vibe-generator-app/
├── venv/                 # Virtual environment folder
├── app.py                # Main Streamlit application script
├── spotify_songs.csv     # The dataset containing song information
└── requirements.txt      # List of Python dependencies for deployment
```

---

## ⚙️ Getting Started

To get this project running on your local machine, please follow these steps.

### 1. Prerequisites
-   Python 3.8 or higher
-   `pip` and `venv` installed

### 2. Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/AtharvaMeherkar/vibe-generator-app.git](https://github.com/AtharvaMeherkar/vibe-generator-app.git)
    cd vibe-generator-app
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    ```bash
    # On Windows:
    .\venv\Scripts\activate
    
    # On macOS/Linux:
    source venv/bin/activate
    ```

4.  **Install the dependencies:**
    ```bash
    pip install streamlit pandas scikit-learn
    ```

### 3. Run the Application

Launch the Streamlit web server with this command:
```bash
streamlit run app.py
```
The application will automatically open in a new tab in your web browser!

---

## 💡 Future Improvements

-   **Genre & Mood Filtering:** Add filters to allow users to refine recommendations by genre or desired mood (e.g., "Happy," "Chill").
-   **"Explain the Vibe" Chart:** Implement a Radar Chart to visualize the audio profile of the user's selected vibe.
-   **User Accounts:** Add user accounts to save favorite vibe selections and generated playlists.

---

## 📞 Contact

Your Name - `atharvameherkar123@gmail.com`

Project Link: [AtharvaMeherkar](https://github.com/AtharvaMeherkar/vibe-generator-app)
