import React, { useState, useEffect } from 'react';
import spb from '../../images/spb.png'
import spa from '../../images/spa.png'
import '../../css/config.css';

function SetterSpawn({onViewChange, handleNextStep, handleAntStep, setSpawnBacterium, setSpawnOther }) {
  const rows = 12;
  const columns = 17;
  const [bacteriumMode, setBacteriumMode] = useState(false);
  const [otherMode, setOtherMode] = useState(false);
  const [spawnBacterium, SetterSpawnBacterium] = useState(null);
  const [spawnOther, SetterSpawnOther] = useState(null);
  const [board, setBoard] = useState([]);

  // Función para generar el board
  const generateBoard = (_rows, _columns) => {
    const newBoard = [];

    for (let i = 0; i < _rows; i++) {
      const row = [];
      for (let j = 0; j < _columns; j++) {
          row.push(<td key={`${i}-${j}`} id={`${i}-${j}`} className="cell" onClick={handleClick}></td>);
      }

      newBoard.push(<tr key={i} className="grid-row">{row}</tr>);
    }

    setBoard(newBoard);
  };

  const handleClick = (event) => {
    if (bacteriumMode) {
      if (spawnBacterium === event.target.id) {
        // Si haces clic nuevamente en la misma celda en modo "Bacterium," deselecciona la celda.
        event.target.className = 'cell';
        setSpawnBacterium(null);
        SetterSpawnBacterium(null);
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
            SetterSpawnBacterium(event.target.id);
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
        SetterSpawnOther(null);
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
            SetterSpawnOther(event.target.id);
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

  //Elegir Spawn Bacteria
  const toggleSpawnBacterium = () => {
    if (bacteriumMode) {
      setBacteriumMode(false);
      console.log(bacteriumMode);
    } else {
      setOtherMode(false);
      setBacteriumMode(!bacteriumMode);
      setspBact(1);
      document.getElementById('spawnbac').classList.toggle('spawnbacAct');
      if (spOth === 1) {
        document.getElementById('spawnoth').classList.toggle('spawnothAct');
        setspOth(0);
      }
      document.addEventListener('mousemove', (e) => {
        const xPos = e.pageX;
        const yPos = e.pageY;
        let m = document.querySelector('.cursor-bacterium');
        m.style.left = xPos+'px';
        m.style.top = yPos+'px';
      })
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
      document.addEventListener('mousemove', (e) => {
        const xPos = e.pageX;
        const yPos = e.pageY;
        let m = document.querySelector('.cursor-other');
        m.style.left = xPos+'px';
        m.style.top = yPos+'px';
      })
    };
  };

  const isNextButtonVisible = () => {
      return spawnBacterium !== null && spawnOther !== null;
  };

  useEffect(() => {
    generateBoard(rows, columns);
  }, [bacteriumMode, otherMode]);

  return (
    <>
    <button className='buttonHome' onClick={() => onViewChange('index')}>
    </button>
      <div className='sss'>

        <div id='mode-select'>
          <p id='spawn'>Spawn: </p>

          <button onClick={toggleSpawnBacterium} id='spawnbac'>
              <img src={spb} alt='Bacterium Spawn'></img>
          </button>

          <button onClick={toggleSpawnOther} id='spawnoth'>
              <img src={spa} alt='Other Spawn'></img>
          </button>
        </div>


        <div className="grid">
            {{otherMode} && <div className="cursor-other"></div>}
            {{bacteriumMode} && <div className="cursor-bacterium"></div>}
            <table><tbody>{board}</tbody></table>
        </div>
      </div>
      <button id='buttons-flush' onClick={handleAntStep} > Anterior </button>

      <button
          id='buttons-flush'
          className='siguiente'
        onClick={handleNextStep}
        disabled={!isNextButtonVisible()} >
        Siguiente
      </button>
    </>
  );
}

export default SetterSpawn;



