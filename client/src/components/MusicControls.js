import React, { useRef, useState } from 'react';


const cargarSonido = function (fuente) {
  const sonido = document.createElement("audio");
  sonido.src = fuente;
  sonido.setAttribute("preload", "auto");
 // sonido.setAttribute("controls", "none");
  sonido.setAttribute("loop", "true");
  sonido.style.display = "none";
  document.body.appendChild(sonido);
  return sonido;
};

const MusicControls = () => {
  const [playlist, setPlaylist] = useState([
    './music/Gravity_falls.mp3',
    './music/music.mp3',
    './music/music1.mp3',
    './music/music2.mp3',
  ]);

  const [currentSongIndex, setCurrentSongIndex] = useState(0);
  const [isPlaying, setIsPlaying] = useState(false);
  const [isLooping, setIsLooping] = useState(false);

  const [audio] = useState(cargarSonido(playlist[currentSongIndex]));

//  const audio = useRef(null);

  const play = () => {
    audio.play();
    setIsPlaying(true);
  };

  const pause = () => {
    audio.pause();
    setIsPlaying(false);
  };

  const previous = () => {
    audio.pause();
    if (currentSongIndex > 0) {
      setCurrentSongIndex(currentSongIndex - 1);
    }else {
      setCurrentSongIndex(playlist.length - 1); // Vuelve al ultimo si estás en la primera canción
    }
    audio.src = playlist[currentSongIndex];
    audio.play();
    console.log('Canción anterior:', currentSongIndex);
    console.log('playlist[currentSongIndex]:', playlist[currentSongIndex]);
  };
  
  const next = () => {
    audio.pause(); // Pausa la canción actual
    if (currentSongIndex < playlist.length - 1) {
      setCurrentSongIndex(currentSongIndex + 1); // Avanza al siguiente índice
    } else {
      setCurrentSongIndex(0); // Vuelve al inicio si estás en la última canción
    }
    audio.src = playlist[currentSongIndex]; // Actualiza la fuente del audio
    audio.play(); // Reproduce la nueva canción
    console.log('Canción posterior:', currentSongIndex);
    console.log('playlist[currentSongIndex]:', playlist[currentSongIndex]);
  };

  const toggleLoop = () => {
    setIsLooping(!isLooping);
    audio.loop = !isLooping;
  };

  return (
    <div>
      <audio ref={audio} src={playlist[currentSongIndex]} />
      <button onClick={previous}>Anterior</button>
      {isPlaying ? (
        <button onClick={pause}>Pausar</button>
      ) : (
        <button onClick={play}>Reproducir</button>
      )}
      <button onClick={next}>Siguiente</button>
      <button onClick={toggleLoop}>
        Loop {isLooping ? 'Activado' : 'Desactivado'}
      </button>
    </div>
  );
};

export default MusicControls;
