import React, { useState } from 'react';
import ant from '../../images/pill.gif';
import selec from '../../images/seleccion.gif';
import vir from '../../images/bacteriophague.png';

function SetterGameMode({ onViewChange, handleNextStep, gameMode, setGameMode }) {
  const [modeOne, setmodeOne] = useState(false);
  const [modeTwo, setmodeTwo] = useState(false);

  // GameMode Antibiotics
  const toggleModeAntibiotic = () => {
    setGameMode(1);
    document.getElementById('modA').classList.toggle('modAa');
    var selec = document.getElementById('selec');
    if (selec.style.display === 'block') {
      setGameMode(null);
      selec.style.display = 'none';
    } else {
      selec.style.display = 'block';
    }

    setmodeOne(!modeOne);
    if (modeTwo) {
      document.getElementById('modV').classList.toggle('modVa');
      document.getElementById('selec2').style.display = 'none';
      setmodeTwo(!modeTwo);
    }
  };

  // GameMode Bacteriopague
  const toggleModeBacteriophague = () => {
    setGameMode(2);
    document.getElementById('modV').classList.toggle('modVa');
    var selec = document.getElementById('selec2');
    if (selec.style.display === 'block') {
      setGameMode(null);
      selec.style.display = 'none';
    } else {
      selec.style.display = 'block';
    }
    setmodeTwo(!modeTwo);
    if (modeOne) {
      document.getElementById('modA').classList.toggle('modAa');
      document.getElementById('selec').style.display = 'none';
      setmodeOne(!modeOne);
    }
  };

  const isNextButtonVisible = () => {
    return gameMode !== null;
  };

  return (
    <>
      <div className='sss'>
          <p>Modo de Juego</p>
          <div id='mode'>
            <button onClick={toggleModeAntibiotic} id='modA'>
              <p className='description'>Antibiotico</p>
              <img src={ant} alt='Antibiotic' id='ant'></img>
              <img src={selec} alt='seleccion' id='selec'></img>
            </button>
            <button onClick={toggleModeBacteriophague} id='modV'>
              <p className='description'>Bacteriofago</p>
              <img src={vir} alt='vir' id='vir'></img>
              <img src={selec} alt='seleccion' id='selec2'></img>
            </button>
          </div>
      </div>
      <button id='buttons-flush' onClick={() => onViewChange('index')}>
          Anterior
        </button>

      <button
          id='buttons-flush'
          className='siguiente'
          onClick={() => handleNextStep(gameMode)}
          disabled={!isNextButtonVisible()}
        >
          Siguiente
        </button>

    </>
  );
}

export default SetterGameMode;
