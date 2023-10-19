import React, {useState, useEffect} from 'react';
import './css/App.css';
import Create_board from './components/board';
import Config from './components/Config';

function App() {
    const [startGame, setStartGame] = useState(false)

    const handleStartGame = (bool) => {
      setStartGame(bool);
    };

    return (
      <>
      <div className="App">
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
