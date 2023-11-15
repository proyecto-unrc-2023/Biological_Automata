import React, { useEffect, useState } from 'react';
import Cell from './Cell';
import '../css/board.css';
import html2canvas from 'html2canvas';
import cap from '../images/Captura.png';

function Create_board({onViewChange, id}) {
  const [board, setBoard] = useState([]);
  const [boardData, setBoardData] = useState(null);
  const [gameData, setGameData] = useState(null);
  const [stopGame, setStopGame] = useState(true);
  const [speed, setSpeed] = useState(1);


  //funcion para refrescar la data del game
  const fetchRefreshData = () => {
    fetch(`http://localhost:5000/game/refreshgame/${id}`)
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
    const url = `http://localhost:5000/game/stopgame/${id}`;
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
      newBoard.push(<tr key={i} className="grid-row" children={row} />);
    }

    setBoard(newBoard);
  };

  const captureScreen = async () => {
    try {
       const node = document.getElementById('capture');
       const canvas = await html2canvas(node);
       const imgData = canvas.toDataURL('image/png');

       const link = document.createElement('a');
       link.href = imgData;
       link.download = 'Tablero.png';
       link.click();

    } catch (err) {
       console.error('Error al capturar la pantalla:', err);
    }
   };

  const togglePause = () => {
    setStopGame(!stopGame)
    document.getElementById('pause').classList.toggle('pause');
  };

  useEffect(() => {
    if(stopGame){
      const refreshInterval = setInterval(refreshGame, 1000/speed);

      return () => {
        clearInterval(refreshInterval);
      };
    }
  }, [gameData, stopGame, speed]);

  return (
    <>
    <div>
    </div>
    <div className="grid">

      <div id='controls-v'>
        <label>Velocidad: </label>
        <input
          type="range" //que aparezca como deslizar
          min="0.5"
          max="5"
          step="0.1"
          value={speed}
          onChange={(e) => setSpeed(parseFloat(e.target.value))} //toma el valor seleccionado y lo transforma en float
        />
      </div>

      <div id='capture'>
        <table><tbody>{board}</tbody></table>
      </div>

      <div id="controls">
        <button className="button stop-button" onClick={() => {
          onViewChange('index'); handleStop_Game();}}>
        </button>

        <button className="button pause-button" id='pause' onClick={() => {
          togglePause();}}>
        </button>
      </div>

    </div>

    <div id='captura'>
        <img src={cap} alt='captura-pantalla' onClick={captureScreen}></img>
    </div>
  </>
  );
}

export default Create_board;
