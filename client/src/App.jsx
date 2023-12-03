import React, {useState} from 'react';
import './css/App.css'
import Index from './components/Index';
import Register from './components/Register';
import Login from './components/Login';
import Config from './components/Config';
import Create_Game from './components/GameBoard';
import MusicControls from './components/MusicControls';

function App() {
    const [selectComponent, setSelectComponent] = useState('index')
    const [id, setId] = useState(null);

    const handleComponentChange = (view) => {
      setSelectComponent(view);
    };

    const components = {
      index: Index,
      register: Register,
      login: Login,
      config: Config,
      game: Create_Game,

    };
    
    const CurrentComponent = components[selectComponent];
    
    return (
      <>
      <div>
        <MusicControls selectComponent={selectComponent}/>
        <CurrentComponent componentChange={handleComponentChange} id = {id} setId = {setId} />
      </div>
      </>
    );
  }

export default App;





