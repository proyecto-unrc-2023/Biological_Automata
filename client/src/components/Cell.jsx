import React, { useEffect, useState } from 'react';

function Cell({ i, j, cellData, gameData }) {
  const [opacity, setOpacity] = useState(100);
  const { _cant_bacterium, _cant_other } = gameData.games;
  const { spawn_bacterium, spawn_other, _game_mode} = gameData.games;
  const { _other, _info_bacteria} = cellData;

  let game_mode;
  if (_game_mode === "Game_Mode.ANTIBIOTIC") {
    game_mode = 1;
  } else {
    game_mode = 2;
  }

  useEffect(() => {
    const { _max_power_other, _moves_for_explotion } = gameData.games;
    const { _info_bacteria, _power_other} = cellData

    if (_info_bacteria[0] !== '') {
      if (_info_bacteria[0] === 'i'){
        const opacityInfected = (_info_bacteria[1] / _moves_for_explotion) * 100;
        setOpacity(opacityInfected);
      } else {
        setOpacity(100);
      }
    } else {
      if (cellData._other !== 0) {
        const opacityOther = (_power_other / _max_power_other) * 100;
        setOpacity(opacityOther);
      }
    }
  }, [_info_bacteria, cellData, gameData.games]);

  let cellClass = 'cell'
  if (spawn_bacterium && spawn_bacterium[0] === i && spawn_bacterium[1] === j && _cant_bacterium === 0) {
    cellClass = "spawnBacterium";
  } else if (spawn_bacterium && spawn_bacterium[0] === i && spawn_bacterium[1] === j && _cant_bacterium > 0) {
    cellClass = "spawnBacteriumActive";
  } else if (spawn_other && spawn_other[0] === i && spawn_other[1] === j && _cant_other === 0) {
    cellClass = "spawnOther";
  } else if (spawn_other && spawn_other[0] === i && spawn_other[1] === j && _cant_other > 0) {
    cellClass = "spawnOtherActive";
  }else if (_info_bacteria[0] !== '') {
    switch (_info_bacteria[0]) {
      case 'f':
        cellClass = "bacteriumStrong";
        break;
      case 'b':
        cellClass = "bacterium";
        break;
      case 'd':
        cellClass = "bacteriumWeak";
        break;
      case 'i':
        cellClass = "bacteriumInfected";
        break;
      default:
    }
  }else if (_other !== 0) {
    if (game_mode === 1){
      cellClass = "antibiotic";
    } else {
      cellClass = "bacteriophage";
    }
  } 

  return <td key={`${i}-${j}`} id={`${i}-${j}`} className={cellClass} style={{ opacity: `${opacity}%` }}></td>;
}

export default Cell;
