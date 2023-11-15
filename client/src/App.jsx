import React, {useState} from 'react';
import './css/App.css'
import Index from './components/Index';
import Create_board from './components/board';
import Config from './components/Config';
import MusicControls from './components/MusicControls';

//import aud from './music/music.mp3'

function App() {
    const [viewComponent, setViewComponent] = useState('index')
    const [id] = useState(Math.floor(Math.random() * 101));
    const [soundPlaying, setSoundPlaying] = useState(false);

    const handleViewChange = (view) => {
      setViewComponent(view);
    };

    const views = {
      index: Index,
      config: Config,
      game: Create_board,

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

    const CurrentViewComponent = views[viewComponent];

    return (
      <>

      {/* <div className="navbar">
        <a href="#" onClick={() => setViewComponent('index')}>Inicio</a>
        <a href="#" onClick={() => setViewComponent('config')}>Jugar</a>
        <a href="#">Créditos</a>
      </div> */}

      <MusicControls />

      <div>
        <CurrentViewComponent onViewChange={handleViewChange} id = {id} />
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





