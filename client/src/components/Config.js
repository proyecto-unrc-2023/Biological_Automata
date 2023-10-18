import React, { useEffect, useState } from 'react';

function Config ({handleStartGame}) {
  const rows =20;
  const columns = 30;
  const [board, setBoard] = useState([]);
  const [bacteriumMode, setBacteriumMode] = useState(false);
  const [otherMode, setOtherMode] = useState(false);
  const [spawnBacterium, setSpawnBacterium] = useState(null);
  const [spawnOther, setSpawnOther] = useState(null);

  // Valores predeterminados y valores editables
  const [cantBact, setCantBact] = useState(10);
  const [frecBact, setFrecBact] = useState(2);
  const [cantOther, setCantOther] = useState(20);
  const [frecOther, setFrecOther] = useState(2);
  const [gameMode, setGameMode] = useState(null);


  useEffect(() => {
    generateBoard(rows, columns);
  }, [bacteriumMode, otherMode]);

  // Función para generar el board
  const generateBoard = (_rows, _columns) => {
    const newBoard = [];
    for (let i = 0; i < _rows; i++) {
      const row = [];
      for (let j = 0; j < _columns; j++) {
          row.push(<td key={`${i}-${j}`} id={`${i}-${j}`} className="cell" onClick={handleClick}></td>);
      }
      newBoard.push(<div key={i} className="grid-row">{row}</div>);
    }
    setBoard(newBoard);
  };

  const handleClick = (event) => {
    if (bacteriumMode) {
      if (spawnBacterium === event.target.id) {
        // Si haces clic nuevamente en la misma celda en modo "Bacterium," deselecciona la celda.
        event.target.className = 'cell';
        setSpawnBacterium(null);
      } else {
        if (spawnBacterium) {
          console.log("Ya se tiene un spawn bacterium en: " + spawnBacterium);
        } else {
          const cellId = event.target.id;
          const isOccupied = isCellOccupied(cellId);
          if (!isOccupied) {
            const currentClass = event.target.className;
            event.target.className = currentClass === 'spawnBacterium' ? 'cell' : 'spawnBacterium';
            setSpawnBacterium(event.target.id);
            setBacteriumMode(!bacteriumMode);
          }
        }
      }
    }

    if (otherMode) {
      if (spawnOther === event.target.id) {
        //si hago click en la misma celda que ya puse antes el spawn se elimina
        event.target.className = 'cell';
        setSpawnOther(null);
      } else {
        if (spawnOther) {
          console.log("Ya se tiene un spawn other en la celda " + spawnOther);
        } else {
          const cellId = event.target.id;
          const isOccupied = isCellOccupied(cellId);

          if (!isOccupied) {
            const currentClass = event.target.className;
            event.target.className = currentClass === 'spawnOther' ? 'cell' : 'spawnOther';
            setSpawnOther(event.target.id);
            setOtherMode(!otherMode);
          }
        }
      }
    }
  };

  const isCellOccupied = (cellId) => {
    // Esto verifica si la celda ya tiene la clase spawnOther o spawnBacterium.
    // Esto evita volver a ocuparla.
    const cell = document.getElementById(cellId);
    return cell.className === 'spawnBacterium' || cell.className === 'spawnOther';
  };

  //Elegir Spawn Bacteria
  const toggleSpawnBacterium = () => {
    if (bacteriumMode) {
      setBacteriumMode(false);
    } else {
      setOtherMode(false);
      setBacteriumMode(!bacteriumMode);
    }
  };

  //Elegir Spawn Other
  const toggleSpawnOther = () => {
    if (otherMode) {
      setOtherMode(false);
    } else {
      setBacteriumMode(false);
      setOtherMode(!otherMode);
    };
  };

  //GameMode Antibiotics
  const toggleModeAntibiotic = () => {
    setGameMode(1);
  };

  //GameMode Bacteriopague
  const toggleModeBacteriophague = () => {
    setGameMode(2);
  };

  const handleSaveConfig = () => {
    if (spawnBacterium && spawnOther && gameMode !== null) {
      const [xBacterium, yBacterium] = spawnBacterium.split('-').map(Number);
      const [xOther, yOther] = spawnOther.split('-').map(Number);
      const url = `http://localhost:5000/game/config/${xBacterium}/${yBacterium}/${xOther}/${yOther}/${cantBact}/${cantOther}/${frecBact}/${frecOther}/${gameMode}`;
      fetch(url, {
        method: 'POST',
      })
        .then(response => {
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          handleStartGame(true)
        })
        .catch(error => {
          console.error('Hubo un error al enviar los datos', error);
        });
    } else {
      console.error('Error: No se ha proporcionado spawns o modo de juego');
    }
  };

  return (
    <div className="grid">
      <button onClick={toggleSpawnBacterium}>
        Elegir Spawn bacterium {bacteriumMode ? "Activado" : "Desactivado"}
      </button>

      <button onClick={toggleSpawnOther}>
        Elegir Spawn Other {otherMode ? "Activado" : "Desactivado"}
      </button>

      <button onClick={toggleModeAntibiotic}>
        Elegir Modo Antibiotic {gameMode === 1 ? "Activado" : "Desactivado"}
      </button>

      <button onClick={toggleModeBacteriophague}>
        Elegir Modo Bacteriophage {gameMode === 2 ? "Activado" : "Desactivado"}
      </button>

      {board}

      <div>
        <label>
          Cantidad de Bacterias:
          <input
            type="number"
            value={cantBact}
            onChange={(e) => setCantBact(parseInt(e.target.value))}
          />
        </label>
      </div>
      <div>
        <label>
          Frecuencia de Bacterias:
          <input
            type="number"
            value={frecBact}
            onChange={(e) => setFrecBact(parseInt(e.target.value))}
          />
        </label>
      </div>
      <div>
        <label>
          Cantidad de Other:
          <input
            type="number"
            value={cantOther}
            onChange={(e) => setCantOther(parseInt(e.target.value))}
          />
        </label>
      </div>
      <div>
        <label>
          Frecuencia de Other:
          <input
            type="number"
            value={frecOther}
            onChange={(e) => setFrecOther(parseInt(e.target.value))}
          />
        </label>
      </div>
      <button onClick={handleSaveConfig}>Guardar Configuracion</button>
    </div>
  );
}

export default Config;

