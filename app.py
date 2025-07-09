import streamlit as st
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity
import urllib.parse

# --- Page Configuration ---
st.set_page_config(
    page_title="Bollywood Vibe Generator",
    page_icon="🎵",
    layout="wide"
)

# --- Data Loading and Caching ---
@st.cache_data
def load_data(file_path):
    """Load, clean, and process the song dataset."""
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip().str.lower()
    # Drop rows where essential information like name or artist is missing
    df.dropna(subset=['name', 'artist'], inplace=True)
    df.drop_duplicates(subset=['name', 'artist'], inplace=True)
    return df

@st.cache_data
def process_data(df):
    """Select features, scale them, and create a unique identifier for each song."""
    feature_cols = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness',
                    'instrumentalness', 'liveness', 'valence', 'tempo']
    
    # Fill any missing numerical features with the median value
    for col in feature_cols:
        if col in df.columns:
            df[col].fillna(df[col].median(), inplace=True)

    scaler = MinMaxScaler()
    df_features = scaler.fit_transform(df[feature_cols])
    df['song_id'] = df['name'] + " - " + df['artist']
    return df, df_features

# --- Core Recommendation Logic ---
def get_recommendations(df, df_features, selected_songs, n_recommendations=9):
    """Generate recommendations based on selected songs."""
    if not selected_songs:
        return pd.DataFrame()

    selected_indices = df[df['song_id'].isin(selected_songs)].index
    if len(selected_indices) == 0:
        return pd.DataFrame()

    vibe_vector = df_features[selected_indices].mean(axis=0).reshape(1, -1)
    cosine_sim = cosine_similarity(vibe_vector, df_features)
    
    sim_scores = list(enumerate(cosine_sim[0]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    recommendation_indices = [i[0] for i in sim_scores if i[0] not in selected_indices]
    
    return df.iloc[recommendation_indices[:n_recommendations]]

# --- Main Application UI ---
st.title("🎵 Bollywood Vibe Generator")
st.markdown("Select a few of your favorite Bollywood songs, and we'll generate a playlist that matches your vibe!")

DATASET_PATH = 'bollywood_songs_curated.csv'

try:
    songs_df = load_data(DATASET_PATH)
    songs_df, features = process_data(songs_df)

    st.header("1. Select Your Vibe")
    selected_songs = st.multiselect(
        'Choose songs you like:',
        options=sorted(songs_df['song_id'].unique()),
        placeholder="Search for songs..."
    )

    if len(selected_songs) > 10:
        st.warning("For best results, choose 3-5 core songs to define your vibe.")

    if st.button("Generate Recommendations", type="primary", use_container_width=True):
        if len(selected_songs) > 0:
            st.header("2. Your Recommended Playlist")
            
            with st.spinner('Generating your custom vibe...'):
                recommended_playlist = get_recommendations(songs_df, features, selected_songs)
            
            if not recommended_playlist.empty:
                cols = st.columns(3)
                for i, song_row in enumerate(recommended_playlist.iterrows()):
                    index, song = song_row
                    with cols[i % 3]:
                        with st.container(border=True):
                            # Use the corrected parameter for the image
                            st.image(f"https://picsum.photos/seed/{urllib.parse.quote(song['name'])}/400", use_container_width=True)
                            st.markdown(f"**{song['name']}**")
                            st.markdown(f"*{song['artist']}*")
                            
                            # --- CORRECTED: Only show Album if it exists ---
                            if 'album' in song and pd.notna(song['album']):
                                st.caption(f"Album: {song['album']}")
                
                st.markdown("---")
                
                st.header("3. Your Playlist available on YouTube Music and Spotify")
                
                query_string = " ".join(recommended_playlist['name'] + " " + recommended_playlist['artist'])
                encoded_query = urllib.parse.quote_plus(query_string)
                
                youtube_music_url = f"https://music.youtube.com/search?q={encoded_query}"
                spotify_url = f"https://open.spotify.com/search/{encoded_query}"
                
                col1, col2 = st.columns(2)
                with col1:
                    st.link_button("Search on YouTube Music 🚀", youtube_music_url, use_container_width=True)
                with col2:
                    st.link_button("Search on Spotify 🟢", spotify_url, use_container_width=True)

            else:
                st.warning("Could not generate recommendations. Please try other songs.")
        else:
            st.warning("Please select at least one song to get recommendations.")

except FileNotFoundError:
    st.error(f"Error: The dataset file '{DATASET_PATH}' was not found.")
except Exception as e:
    st.error(f"An error occurred: {e}.")