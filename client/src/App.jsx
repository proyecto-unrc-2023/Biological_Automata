import React, {useState} from 'react';
import './css/App.css'
import Index from './components/Index';
import Register from './components/Register';
import Login from './components/Login';
import Config from './components/Config';
import Create_board from './components/board';
import MusicControls from './components/MusicControls';

function App() {
    const [viewComponent, setViewComponent] = useState('index')
    const [id, setId] = useState(null);

    const handleViewChange = (view) => {
      setViewComponent(view);
    };

    const views = {
      index: Index,
      register: Register,
      login: Login,
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
        <CurrentViewComponent onViewChange={handleViewChange} id = {id} setId = {setId} />
      </div>
      </>
    );
  }

export default App;





