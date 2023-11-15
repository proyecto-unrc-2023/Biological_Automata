import React, { useState } from 'react';
import SetterGameMode from './Config/SetGameMode';
import SetterSpawn from './Config/SetterSpawn';
import '../css/config.css';

function Config({ onViewChange, id }) {
  const [step, setStep] = useState(1);

  const [spawnBacterium, setSpawnBacterium] = useState(null);
  const [spawnOther, setSpawnOther] = useState(null);

  // Valores predeterminados y valores editables
  const [cantBact, setCantBact] = useState(10);
  const [frecBact, setFrecBact] = useState(2);
  const [cantOther, setCantOther] = useState(20);
  const [frecOther, setFrecOther] = useState(2);
  const [gameMode, setGameMode] = useState(null);

  const handleNextStep = () => {
    if (step === 1) {
      setStep(2);
    } else if (step === 2) {
      // Validar spawns y otros parámetros aquí antes de avanzar al siguiente paso
      setStep(3);
    } else if (step === 3) {
      handleSaveConfig();
    }
  };

  const handleAntStep = () => {
    if (step === 2) {
      setStep(1);
    } else if (step === 3) {
      // Validar spawns y otros parámetros aquí antes de avanzar al siguiente paso
      setStep(2);
    }
  };

  const handleSaveConfig = () => {
    if (
      spawnBacterium &&
      spawnOther &&
      gameMode !== null &&
      isValidNumbers(cantBact, cantOther, frecBact, frecOther)
    ) {
      const data = {
        xBacterium: spawnBacterium.split('-').map(Number)[0],
        yBacterium: spawnBacterium.split('-').map(Number)[1],
        xOther: spawnOther.split('-').map(Number)[0],
        yOther: spawnOther.split('-').map(Number)[1],
        cantBact: cantBact,
        cantOther: cantOther,
        frecBact: frecBact,
        frecOther: frecOther,
        gameMode: gameMode,
        id: id,
      };

      fetch(`http://localhost:5000/game/saveConfig`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          onViewChange('game');
        })
        .catch((error) => {
          console.error('Hubo un error al enviar los datos', error);
        });
    } else {
      console.error('Error: No se ha proporcionado spawns o modo de juego');
    }
  };

  const isValidNumbers = (...numbers) => {
    return numbers.every((num) => !isNaN(num) && num >= 0);
  };

  return (
    <>
      {step === 1 && (
        <SetterGameMode
          onViewChange={onViewChange}
          handleNextStep={handleNextStep}
          gameMode={gameMode}
          setGameMode={setGameMode}
        />
      )}

      {step === 2 && (
        <SetterSpawn
          onViewChange={onViewChange}
          handleNextStep={handleNextStep}
          handleAntStep={handleAntStep}
          spawnBacterium={spawnBacterium}
          setSpawnBacterium={setSpawnBacterium}
          spawnOther={spawnOther}
          setSpawnOther={setSpawnOther}
        />
      )}

      {step === 3 && (
        <div id='params'>
          <label>
            Cantidad de Bacterias:
            <input
              type='number'
              value={cantBact}
              onChange={(e) => setCantBact(parseInt(e.target.value))}
              min='0'
            />
          </label>
          <label>
            Frecuencia de Bacterias:
            <input
              type='number'
              value={frecBact}
              onChange={(e) => setFrecBact(parseInt(e.target.value))}
              min='1'
            />
          </label>
          <label>
            Cantidad de Other:
            <input
              type='number'
              value={cantOther}
              onChange={(e) => setCantOther(parseInt(e.target.value))}
              min='0'
            />
          </label>
          <label>
            Frecuencia de Other:
            <input
              type='number'
              value={frecOther}
              onChange={(e) => setFrecOther(parseInt(e.target.value))}
              min='1'
            />
          </label>
          <button className='buttonInit' onClick={handleNextStep}>
            PLAY
          </button>
          <button className='buttonInit' onClick={handleAntStep}>
            {' '}
            Anterior{' '}
          </button>
          <button className='buttonInit' onClick={() => onViewChange('index')}>
            Inicio
        </button>
        </div>
      )}
    </>
  );
}

export default Config;
