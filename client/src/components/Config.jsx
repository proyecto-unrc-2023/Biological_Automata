import React, { useState } from 'react';
import SetterGameMode from './Config/SetGameMode';
import SetterSpawn from './Config/SetterSpawn';
import '../css/config.css';
import Tooltip from './Tooltip';

function Config({ componentChange, setId, id}) {
  const [step, setStep] = useState(1);

  const [spawnBacterium, setSpawnBacterium] = useState(null);
  const [spawnOther, setSpawnOther] = useState(null);
  const [showMore, setShowMore] = useState(false);

  // Valores predeterminados y valores editables
  const [cantBact, setCantBact] = useState(10);
  const [frecBact, setFrecBact] = useState(2);
  const [cantOther, setCantOther] = useState(20);
  const [frecOther, setFrecOther] = useState(2);
  const [gameMode, setGameMode] = useState(null);
  const [movesReproduction, setMovesReproduction] = useState(10);
  const [movesRecovery, setMovesRecovery] = useState(6);
  const [powerAntibiotic, setPowerAntibiotic] = useState(3);
  const [movesExplotion, setMovesExplotion] = useState(4);
  const [virusAfterExplotion, setVirusAfterExplotion] = useState(4);
  const [initialPowerInfection, setInitialPowerInfection] = useState(4);
  const [mutationProbability, setMutationProbability] = useState(0.1);
  const [cantOverpopulation, setCantOverpopulation] = useState(4);

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
      const xBacterium = spawnBacterium.split('-').map(Number)[0];
      const yBacterium = spawnBacterium.split('-').map(Number)[1];
      const xOther = spawnOther.split('-').map(Number)[0];
      const yOther = spawnOther.split('-').map(Number)[1];

      fetch(`http://localhost:5000/game/newgame`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          xBacterium,
          yBacterium,
          xOther,
          yOther,
          cantBact,
          cantOther,
          frecBact,
          frecOther,
          gameMode,
          id,
          movesReproduction,
          movesRecovery,
          powerAntibiotic,
          movesExplotion,
          virusAfterExplotion,
          initialPowerInfection,
          mutationProbability,
          cantOverpopulation,
        }),
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          return response.json();
        })
        .then((data) => {
          if(data.id === id) {
            componentChange('game');
          }
        })
        .catch((error) => {
          console.error('Hubo un error al enviar los datos', error);
        });
    }
  };


  const isValidNumbers = (...numbers) => {
    return numbers.every((num) => !isNaN(num) && num >= 0);
  };

  return (
    <>
      <div className='config-conteiner'>
        <div className='background'>
          {step === 1 && (
            <SetterGameMode
              componentChange={componentChange}
              handleNextStep={handleNextStep}
              gameMode={gameMode}
              setGameMode={setGameMode}
            />
          )}

          {step === 2 && (
            <SetterSpawn
              componentChange={componentChange}
              handleNextStep={handleNextStep}
              handleAntStep={handleAntStep}
              spawnBacterium={spawnBacterium}
              setSpawnBacterium={setSpawnBacterium}
              spawnOther={spawnOther}
              setSpawnOther={setSpawnOther}
              gameMode={gameMode}
            />
          )}

          {step === 3 && (
          <div id='config'>
            <button className='buttonHome' onClick={() => componentChange('index')}>
            </button>
            <div id='params' className='params'>
              <label>
               <Tooltip text="Cantidad de bacterias que saldrán del spawn">
                Cantidad de Bacterias:
                <input
                  type='number'
                  value={cantBact}
                  onChange={(e) => setCantBact(parseInt(e.target.value))}
                  min='0'
                />
                </Tooltip>
              </label>
              <label>
              <Tooltip text="Cantidad de pasos que pasan entre cada spawneo de bacterias">
                Frecuencia de Bacterias:
                <input
                  type='number'
                  value={frecBact}
                  onChange={(e) => setFrecBact(parseInt(e.target.value))}
                  min='1'
                />
                </Tooltip>
              </label>
              <label>
                <Tooltip text={`Cantidad de ${gameMode === 1 ? "antibióticos" : "bacteriófagos"} que saldrán del spawn`}>
                  Cantidad de {gameMode === 1 ? "Antibióticos" : "Bacteriófagos"}:
                  <input
                    type='number'
                    value={cantOther}
                    onChange={(e) => setCantOther(parseInt(e.target.value))}
                    min='0'
                  />
                </Tooltip>
              </label>
              <label>
                <Tooltip text={`Cantidad de pasos que pasan entre cada spawneo de ${gameMode === 1 ? "antibióticos" : "bacteriófagos"}`}>
                Frecuencia de {gameMode === 1 ? "Antibióticos" : "Bacteriófagos"}:
                <input
                  type='number'
                  value={frecOther}
                  onChange={(e) => setFrecOther(parseInt(e.target.value))}
                  min='1'
                />
                </Tooltip>
              </label>
              <button className='buttonInit' onClick={handleNextStep}>
                Jugar
              </button>
              <button className='buttonInit' onClick={handleAntStep}>
                {' '}
                Anterior{' '}
              </button>
            </div>

            <div id='advanced-params' className='params'>
              {/* Botón para mostrar/ocultar el segundo grupo */}
              <button className='buttonShowMore' onClick={() => setShowMore(!showMore)}>
                {showMore ? "Ocultar" : "Conf. Avanzada"}
              </button>

              {/* Mostrar el segundo grupo solo si showMore es verdadero */}
              {showMore && (
                <>

                  <label>
                    <Tooltip text="Cantidad de movimientos que necesitan las bacterias para reproducirse">
                    Mov. reproducción:
                    <input
                      type='number'
                      value={movesReproduction}
                      onChange={(e) => setMovesReproduction(parseInt(e.target.value))}
                      min='1'
                    />
                    </Tooltip>
                  </label>
                  <label>
                  <Tooltip text="Cantidad de bacterias en una celda que produce sobrepoblación">
                    Cant. sobrepoblación:
                    <input
                      type='number'
                      value={cantOverpopulation}
                      onChange={(e) => setCantOverpopulation(parseInt(e.target.value))}
                      min='1'
                    />
                    </Tooltip>
                  </label>
                  {gameMode === 1 && (
                    <>
                      <label>
                        <Tooltip text="Cantidad de movimientos que necesita una bacteria débil para recuperarse">
                        Mov. recuperación:
                        <input
                          type='number'
                          value={movesRecovery}
                          onChange={(e) => setMovesRecovery(parseInt(e.target.value))}
                          min='1'
                        />
                        </Tooltip>
                      </label>
                      <label>
                        <Tooltip text="Poder con el que los antibióticos salen del spawn">
                        Poder antibióticos:
                        <input
                          type='number'
                          value={powerAntibiotic}
                          onChange={(e) => setPowerAntibiotic(parseInt(e.target.value))}
                          min='0'
                        />
                        </Tooltip>
                      </label>
                      <label>
                        <Tooltip text="Probabilidad de mutación cuando una bacteria se reproduce">
                        Probabilidad de mutación:
                        <input
                          type='number'
                          value={mutationProbability}
                          onChange={(e) => setMutationProbability(parseFloat(e.target.value))}
                          max='1'
                          min='0'
                          step='0.05'
                        />
                        </Tooltip>
                      </label>
                    </>
                  )}

                  {gameMode === 2 && (
                    <>
                      <label>
                        <Tooltip text="Cantidad de pasos que necesita una bacteria infectada para explotar">
                        Mov. explosión:
                        <input
                          type='number'
                          value={movesExplotion}
                          onChange={(e) => setMovesExplotion(parseInt(e.target.value))}
                          min='1'
                        />
                        </Tooltip>
                      </label>
                      <label>
                        <Tooltip text="Cantidad de bacteriófagos que salen después de la explosión">
                        Virus después explosión:
                        <input
                          type='number'
                          value={virusAfterExplotion}
                          onChange={(e) => setVirusAfterExplotion(parseInt(e.target.value))}
                          min='1'
                        />
                        </Tooltip>
                      </label>
                      <label>
                        <Tooltip text="Poder de infección con el que comienzan los bacteriófagos">
                        Poder infeccion inicial:
                        <input
                          type='number'
                          value={initialPowerInfection}
                          onChange={(e) => setInitialPowerInfection(parseInt(e.target.value))}
                          min='1'
                        />
                        </Tooltip>
                      </label>
                    </>
                  )}
                </>
              )}
            </div>



          </div>
          )}
        </div>
      </div>
    </>
  );
}

export default Config;
