import React, {useState, useEffect} from 'react';
import './css/config.css';
import Create_board from './components/board';
import Config from './components/Config';

function App() {
    const [gameData, setGameData] = useState(null);
    const [startGame, setStartGame] = useState(false)
    useEffect(() => {
      fetch('http://localhost:5000/game/game')
        .then((response) => response.json())
        .then((data) => {
          setGameData(data);
        })
        .catch((error) => {
          console.error('Error no se agarró el JSON', error);
        });
    }, [startGame]);

    if (gameData === null) {
      return <div>NO CARGO</div>;
    }

    const handleStartGame = (bool) => {
      setStartGame(bool);
    };

    return (
      <>
      <div className="App">
        {startGame ? (
          <Create_board gameData={gameData} handleStartGame={handleStartGame} />
        ) : (
          <Config handleStartGame={handleStartGame} />
        )}

      </div>
      </>
    );
  }

export default App;
