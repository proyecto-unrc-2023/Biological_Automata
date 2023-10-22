import React, { useEffect, useState } from 'react';
import spb from '../images/spb.png'
import spa from '../images/spa.png'
import ant from '../images/pill.gif'
import vir from '../images/bacteriophague.png'
import '../css/config.css';


function Config ({handleStartGame}) {
  const rows =15;
  const columns = 20;
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


  const [spBact, setspBact] = useState(0);
  const [spOth, setspOth] = useState(0);
  const [modeOne, setmodeOne] = useState(false);
  const [modeTwo, setmodeTwo] = useState(false);
  //Elegir Spawn Bacteria
  const toggleSpawnBacterium = () => {
    if (bacteriumMode) {
      setBacteriumMode(false);
    } else {
      setOtherMode(false);
      setBacteriumMode(!bacteriumMode);
      setspBact(1);
      document.getElementById('spawnbac').classList.toggle('spawnbacAct');
      if (spOth === 1) {
        document.getElementById('spawnoth').classList.toggle('spawnothAct');
        setspOth(0);
      }
    }
  };
  
  //Elegir Spawn Other
  const toggleSpawnOther = () => {
    if (otherMode) {
      setOtherMode(false);
    } else {
      setBacteriumMode(false);
      setOtherMode(!otherMode);
      setspOth(1);
      document.getElementById('spawnoth').classList.toggle('spawnothAct');
      if (spBact === 1) {
        document.getElementById('spawnbac').classList.toggle('spawnbacAct');
        setspBact(0);
      }
    };
  };

  //GameMode Antibiotics
  const toggleModeAntibiotic = () => {
    setGameMode(1);
    document.getElementById('modA').classList.toggle('modAa');
    setmodeOne(!modeOne);
    if (modeTwo) {
      document.getElementById('modV').classList.toggle('modVa');
      setmodeTwo(!modeTwo);
    }
  };
  
  //GameMode Bacteriopague
  const toggleModeBacteriophague = () => {
    setGameMode(2);
    document.getElementById('modV').classList.toggle('modVa');
    setmodeTwo(!modeTwo);
    if (modeOne) {
      document.getElementById('modA').classList.toggle('modAa');
      setmodeOne(!modeOne);
    }    
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

    <>
    <div class='sss'>

      <p id='spawn'>Spawn</p>

      <button onClick={toggleSpawnBacterium} id='spawnbac'>
        <img src={spb}></img>
      </button>


      <button onClick={toggleSpawnOther} id='spawnoth'>
        <img src={spa}></img>
      </button>

      <div>

        <p>Game mode</p>
            <div id="mode">
              <button onClick={toggleModeAntibiotic} id='modA'>
                <img src={ant}></img>
              </button>

              <button onClick={toggleModeBacteriophague} id='modV'>
                <img src={vir}></img>
                {/* Elegir Modo Bacteriophage {gameMode === 2 ? "Activado" : "Desactivado"} */}
              </button>
            </div>
      </div>
    </div>
    <div className="grid">

      {board}

    </div>

    <div id='params'>
        <label>
          Cantidad de Bacterias:
          <input
            type="number"
            value={cantBact}
            onChange={(e) => setCantBact(parseInt(e.target.value))}
            />
        </label>
        <label>
          Frecuencia de Bacterias:
          <input
            type="number"
            value={frecBact}
            onChange={(e) => setFrecBact(parseInt(e.target.value))}
          />
        </label>
        <label>
          Cantidad de Other:
          <input
            type="number"
            value={cantOther}
            onChange={(e) => setCantOther(parseInt(e.target.value))}
            />
        </label>
        <label>
          Frecuencia de Other:
          <input
            type="number"
            value={frecOther}
            onChange={(e) => setFrecOther(parseInt(e.target.value))}
            />
        </label>
      <button onClick={handleSaveConfig}>Save change</button>
    </div>
    </>
  );
}
export default Config;

