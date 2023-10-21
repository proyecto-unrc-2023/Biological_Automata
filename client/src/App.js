import React, {useState, useEffect} from 'react';
import './css/App.css';
import Create_board from './components/board';
import Config from './components/Config';
import aud from './images/music.mp3'

function App() {
    const [startGame, setStartGame] = useState(false)
    const [sound, setSound] = useState(0)

    const handleStartGame = (bool) => {
      setStartGame(bool);
      setSound(1);
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
  const sonido = cargarSonido(aud);
  const reproducir = function() {
    if (!startGame && sound === 0) {
      try {
        sonido.play();
      } catch (error) {
        
      }
    }
  };



    return (
      <>
      
      <div className="App" onMouseMove={reproducir}>
        {startGame ? (
          <Create_board handleStartGame={handleStartGame} />
        ) : (
          <Config handleStartGame={handleStartGame} />
        )}

      </div>
      </>
    );
  }

export default App;
