import React, { useEffect, useState } from 'react';
import Cell from './Cell';

function Create_board({handleStartGame }) {
  const [board, setBoard] = useState([]);
  const [boardData, setBoardData] = useState(null);
  const [gameData, setGameData] = useState(null);

  const [stopGame, setStopGame] = useState(true);
  const [speed, setSpeed] = useState(1);

  //funcion para refrescar la data del game
  const fetchRefreshData = () => {
    fetch('http://localhost:5000/game/refresh')
      .then((response) => response.json())
      .then((data) => {
        setGameData(data);
      })
      .catch((error) => {
        console.error('Error no se agarró el JSON', error);
      });
  };


  const refreshGame = () => {
    fetchRefreshData();

    if (gameData === null) {
      return "Cargando...";
    }

    const { _rows, _columns } = gameData.games._board;

    setBoardData(gameData.games._board._board);
    generateBoard(_rows, _columns);
  };

    // Frenar el Juego Con el Boton STOP
  const handleStop_Game = () => {
    const url = `http://localhost:5000/game/stop`;
    fetch(url)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
      })
      .catch(error => {
        console.error('Hubo un error al terminar el juego', error);
      });
  };


  useEffect(() => {
    if(stopGame){
      const refreshInterval = setInterval(refreshGame, 1000/speed);

      return () => {
        clearInterval(refreshInterval);
      };
    }
  }, [gameData, stopGame, speed]);


  const generateBoard = (_rows, _columns) => {
    if (!boardData) {
      return; //esto hace que no salga un error cuando no se hizo el refresh XD
    }

    const newBoard = [];
    for (let i = 0; i < _rows; i++) {
      const row = [];

      for (let j = 0; j < _columns; j++) {
        const cellData = boardData[i][j];

        row.push( <Cell i={i} j={j} cellData={cellData} gameData={gameData}/> );  //Componente que crea la celda
      }

      newBoard.push(  <div key={i} className="grid-row"> {row} </div>   );
    }

    setBoard(newBoard);
  };


  const togglePause = () => {
    setStopGame(!stopGame)
  };

  return (
    <>
    <div>
    </div>
    <div className="grid">

      <label>Velocidad: </label>
      <input
        type="range" //que aparezca como deslizar
        min="0.5"
        max="5"
        step="0.1"
        value={speed}
        onChange={(e) => setSpeed(parseFloat(e.target.value))} //toma el valor seleccionado y lo transforma en float
      />

      {board}
      <button onClick={() => {
        handleStartGame(false); handleStop_Game();}}>
        STOP
      </button>

      <button onClick={() => {
        togglePause();}}>
        PAUSA
      </button>

    </div>
    <div>

    </div>
  </>
  );
}

export default Create_board;
