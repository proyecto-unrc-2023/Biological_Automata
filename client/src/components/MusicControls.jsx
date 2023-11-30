import React, { useState, useEffect } from 'react';
import '../css/MusicControls.css'; // Importa el archivo CSS

const cargarSonido = function (fuente) {
  const sonido = document.createElement("audio");
  sonido.src = fuente;
  sonido.setAttribute("preload", "auto");
  sonido.setAttribute("loop", "true");
  sonido.style.display = "none";
  document.body.appendChild(sonido);
  return sonido;
};

const MusicControls = () => {
  const [playlist, setPlaylist] = useState([]);
  const amount_song = 11;
  const [currentSongIndex, setCurrentSongIndex] = useState(0);
  const [isPlaying, setIsPlaying] = useState(false);
  const [audio] = useState(cargarSonido(playlist[currentSongIndex]));

  useEffect(() => {
    const tempPlaylist = [];
    for (let i = 0; i <= amount_song; i++) {
      tempPlaylist.push(`./music/music${i}.mp3`);
    }
    setPlaylist(tempPlaylist);
  }, [amount_song]);

  useEffect(() => {
    audio.src = playlist[currentSongIndex];
    audio.load(); // Carga explícita para reiniciar la carga de la canción
    audio.addEventListener('loadedmetadata', () => {
      if (isPlaying) {
        audio.play();
      }
    });
  }, [currentSongIndex, isPlaying, audio, playlist]);

  const play = () => {
    setIsPlaying(true);
  };

  const pause = () => {
    setIsPlaying(false);
  };

  const previous = () => {
    if (currentSongIndex > 0) {
      setCurrentSongIndex(currentSongIndex - 1);
    }else {
      setCurrentSongIndex(playlist.length - 1); // Vuelve al ultimo si estás en la primera canción
    }
  };
  
  const next = () => {
    if (currentSongIndex < playlist.length - 1) {
      setCurrentSongIndex(currentSongIndex + 1); // Avanza al siguiente índice
    } else {
      setCurrentSongIndex(0); // Vuelve al inicio si estás en la última canción
    }
  };
  
  return (
    <div className="music-controls-container">
      <audio ref={audio} />
      <button onClick={previous} className="button-music previous-music">
      </button>
      {isPlaying ? (
        <button onClick={pause} className="button-music pause-music">
        </button>
      ) : (
        <button onClick={play} className="button-music play-music">
        </button>
      )}
      <button onClick={next} className="button-music next-button">
      </button>

    </div>
  );
};

export default MusicControls;