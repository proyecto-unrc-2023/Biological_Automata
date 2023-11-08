import React, {useState} from 'react';
import Create_board from './components/board';
import Config from './components/Config';
import MusicControls from './components/MusicControls';
//import aud from './music/music.mp3'

function App() {
    const [startGame, setStartGame] = useState(false)
    const [id] = useState(Math.floor(Math.random() * 101));
    const [soundPlaying, setSoundPlaying] = useState(false);

    const handleStartGame = (bool) => {
      setStartGame(bool);
    };

    const cargarSonido = function (fuente) {
      const sonido = document.createElement("audio");
      sonido.src = fuente;
      sonido.setAttribute("preload", "auto");
      sonido.setAttribute("controls", "none");
      sonido.setAttribute("loop", "true");
      sonido.style.display = "none"; // <-- oculto
      document.body.appendChild(sonido);
      return sonido;
  };

  // const play = document.querySelector("#btnReproducir");
  // const [sonido] = useState(cargarSonido(aud));
  const [sonido] = useState(cargarSonido("/music/music.mp3"));

  const reproducir = function() {
    if (!soundPlaying) {
      try {
        sonido.play();
        setSoundPlaying(true);
      } catch (error) {
      }
    } else if (soundPlaying) {
      try {
        sonido.pause();
        setSoundPlaying(false);
      } catch (error) {
      }
    }
  };

    return (
      <>
      <MusicControls />
      <div className="App">
        {startGame ? (
          <Create_board handleStartGame={handleStartGame} id={id} />
        ) : (
          <Config handleStartGame={handleStartGame} id={id}/>
        )}
      </div>

      <div>
        <button className ="button sonido" onClick={reproducir}>
          {soundPlaying ? 'Pausar' : 'Reproducir'}
        </button>
      </div>
  
      </>
    );
  }

export default App;





