import React, { useEffect, useState } from 'react';

function Create_board({handleStartGame }) {
  const [rows, setRows] = useState(0);
  const [columns, setColumns] = useState(0);
  const [board, setBoard] = useState([]);
  const [spawn_b, setSpawn_b] = useState(null);
  const [spawn_o, setSpawn_o] = useState(null);
  const [boardData, setBoardData] = useState(null);
  const [gameData, setGameData] = useState(null);

  useEffect(() => {
    fetch('http://localhost:5000/game/refresh')
      .then((response) => response.json())
      .then((data) => {
        setGameData(data);
      })
      .catch((error) => {
        console.error('Error no se agarró el JSON', error);
      });


      if (gameData === null) {
        return;
      }

      const { _rows, _columns } = gameData.games._board;
      const { spawn_bacterium, spawn_other } = gameData.games;

      setRows(_rows);
      setColumns(_columns);
      setSpawn_b(spawn_bacterium);
      setSpawn_o(spawn_other);

      // Llamamos a la función para generar el grid con los datos del JSON
      generateBoard(rows, columns);
      setBoardData(gameData.games._board._board); // Asignar la estructura de datos a gameData



  }, [gameData]);




  if (boardData != null){
    const primeraCelda = boardData[0][0];
    const antibiotics = primeraCelda._antibiotics;
    const cantBacteriophage = primeraCelda._cant_bacteriophage;
    const bacterias = primeraCelda.bacterias;
  }

  // Función para generar el board
  const generateBoard = (_rows, _columns) => {
    const newBoard = [];
    for (let i = 0; i < _rows; i++) {
      const row = [];
      for (let j = 0; j < _columns; j++) {
        const cell = boardData[i][j];
        const antibiotics = cell._antibiotics;
        const cantBacteriophage = cell._cant_bacteriophage;
        const bacterias = cell.bacterias;
        if (antibiotics !== 0) {
          row.push(<td key={`${i}-${j}`} id={`${i}-${j}`} className="antibiotic"></td>);
        } else {
          if (Array.isArray(bacterias) && bacterias.length !== 0) {
            row.push(<td key={`${i}-${j}`} id={`${i}-${j}`} className="bacterium"></td>);
          } else {
            if (spawn_b && spawn_b[0] === i && spawn_b[1] === j) {
              row.push(<td key={`${i}-${j}`} id={`${i}-${j}`} className="spawnBacterium"></td>);
            } else if (spawn_o && spawn_o[0] === i && spawn_o[1] === j) {
              row.push(<td key={`${i}-${j}`} id={`${i}-${j}`} className="spawnOther"></td>);
            } else {
              row.push(<td key={`${i}-${j}`} id={`${i}-${j}`} className="cell"></td>);
            }
          }
        }
      }
      newBoard.push(<div key={i} className="grid-row">{row}</div>);
    }
    setBoard(newBoard);
  };

  if (gameData === null) {
    return <div>NO CARGO</div>;
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
    <div className="grid">
      {board}
      <button onClick={() => {
      handleStartGame(false); handleStop_Game();}}>
        STOP
      </button>
    </div>
  );
}

export default Create_board;
