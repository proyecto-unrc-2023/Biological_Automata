import React, { useState, useEffect, useRef } from 'react';
import '../css/MusicControls.css'; // Importa el archivo CSS

const MusicControls = ({ selectComponent }) => {
  const [playlist, setPlaylist] = useState([]);
  const amount_song = 11;
  const [currentSongIndex, setCurrentSongIndex] = useState(0);
  const [isPlaying, setIsPlaying] = useState(false);
  const audioRef = useRef(null);
  const [isActionInProgress, setIsActionInProgress] = useState(false);

  useEffect(() => {
    const tempPlaylist = [];
    for (let i = 0; i <= amount_song; i++) {
      tempPlaylist.push(`./music/music${i}.mp3`);
    }
    setPlaylist(tempPlaylist);
  }, [amount_song]);

  useEffect(() => {
    if (audioRef.current){
      audioRef.current.src = playlist[currentSongIndex];
      audioRef.current.loop = true;
      if (isPlaying) {
        audioRef.current.play();
      }
    }
  }, [currentSongIndex, playlist, isPlaying]);

  const performActionWithDelay = (actionFunction) => {
    if (!isActionInProgress) {
      setIsActionInProgress(true);
      actionFunction();
      setTimeout(() => {
        setIsActionInProgress(false);
      }, 1000); // Espera 1 segundo antes de habilitar la acción nuevamente
    }
  };

  const play = () => {
    setIsPlaying(true);
  };

  const pause = () => {
    setIsPlaying(false);
  };

  const previous = () => {
    performActionWithDelay(() => {
      if (currentSongIndex > 0) {
        setCurrentSongIndex(currentSongIndex - 1);
      } else {
        setCurrentSongIndex(playlist.length - 1);
      }
    });
  };
  
  const next = () => {
    performActionWithDelay(() => {
      if (currentSongIndex < playlist.length - 1) {
        setCurrentSongIndex(currentSongIndex + 1);
      } else {
        setCurrentSongIndex(0);
      }
    });
  };
  
  return (
    <div className={`music-controls-container ${selectComponent === 'game' ? 'visible' : 'hidden'}`}>
      <audio ref={audioRef} />
      <button onClick={previous} className="button-music previous-music"></button>
      {isPlaying ? (
        <button onClick={pause} className="button-music pause-music"></button>
      ) : (
        <button onClick={play} className="button-music play-music"></button>
      )}
      <button onClick={next} className="button-music next-button"></button>
    </div>
  );
};

export default MusicControls;