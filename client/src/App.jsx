import React, {useState} from 'react';
import './css/App.css'
import Index from './components/Index';
import Create_board from './components/board';
import Config from './components/Config';
import MusicControls from './components/MusicControls';

function App() {
    const [viewComponent, setViewComponent] = useState('index')
    const [id] = useState(Math.floor(Math.random() * 101));

    const handleViewChange = (view) => {
      setViewComponent(view);
    };

    const views = {
      index: Index,
      config: Config,
      game: Create_board,

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
      </>
    );
  }

export default App;





