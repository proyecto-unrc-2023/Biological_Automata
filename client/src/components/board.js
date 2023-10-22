import React, { useEffect, useState } from 'react';

function Create_board({handleStartGame }) {
  const [rows, setRows] = useState(0);
  const [columns, setColumns] = useState(0);
  const [board, setBoard] = useState([]);
  const [spawn_b, setSpawn_b] = useState(null);
  const [spawn_o, setSpawn_o] = useState(null);
  const [boardData, setBoardData] = useState(null);
  const [gameData, setGameData] = useState(null);
  const [stop, setStop] = useState(false);


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
    const { spawn_bacterium, spawn_other } = gameData.games;

    setRows(_rows);
    setColumns(_columns);
    setSpawn_b(spawn_bacterium);
    setSpawn_o(spawn_other);
    setBoardData(gameData.games._board._board);
    generateBoard(_rows, _columns);
  };


  useEffect(() => {
    const refreshInterval = setInterval(refreshGame, 200);

    return () => {
      clearInterval(refreshInterval);
    };
  }, [gameData, stop]);


  const generateBoard = (_rows, _columns) => {
    if (!boardData) {
      return; //esto hace que no salga un error cuando no se hizo el refresh XD
    }

    const newBoard = [];
    for (let i = 0; i < _rows; i++) {
      const row = [];

      for (let j = 0; j < _columns; j++) {
        const cell = boardData[i][j];
        const antibiotics = cell._antibiotics;
        const cantBacteriophage = cell._cant_bacteriophage;
        const bacterias = cell.bacterias;
        const cantBact = gameData.games._cant_bacterium
        const cantOther = gameData.games._cant_other

        let cellClass = "cell"; // Clase predeterminada

        if (antibiotics !== 0) {
          cellClass = "antibiotic";
        } else if (Array.isArray(bacterias) && bacterias.length > 0) {
          if (bacterias.includes("f")) {
            cellClass = "bacteriumStrong";
          } else if (bacterias.includes("b")) {
            cellClass = "bacterium";
          } else if (bacterias.includes("d")) {
            cellClass = "bacteriumWeak";
          } else {
            cellClass = "bacteriumInfected";
          }
        } else if (cantBacteriophage !== 0) {
          cellClass = "bacteriophage";
        } else if (spawn_b && spawn_b[0] === i && spawn_b[1] === j && cantBact == 0) {
          cellClass = "spawnBacterium";
        } else if (spawn_b && spawn_b[0] === i && spawn_b[1] === j && cantBact > 0) {
          cellClass = "spawnBacteriumActive";
        } else if (spawn_o && spawn_o[0] === i && spawn_o[1] === j && cantOther == 0) {
          cellClass = "spawnOther";
        } else if (spawn_o && spawn_o[0] === i && spawn_o[1] === j && cantOther > 0) {
          cellClass = "spawnOtherActive";
        }

        row.push(
          <td key={`${i}-${j}`} id={`${i}-${j}`} className={cellClass}></td>
        );
      }

      newBoard.push(
        <div key={i} className="grid-row">
          {row}
        </div>
      );
    }

    setBoard(newBoard);
  };

  if (gameData === null) {
    return <div>Cargando...</div>;
  }

  // Frenar el Juego Con el Boton STOP
  const handleStop_Game = () => {
      const url = `http://localhost:5000/game/stop`;
      fetch(url, {
        method: 'POST',
      })
        .then(response => {
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
        })
        .catch(error => {
          console.error('Hubo un error al terminar el juego', error);
        });
  };

  return (
    <>
    <div>
    </div>
    <div className="grid">
      {board}
      <button onClick={() => {
        handleStartGame(false); setStop(true); handleStop_Game();}}>
        STOP
      </button>
    </div>
    <div>

    </div>
  </>
  );
}

export default Create_board;
