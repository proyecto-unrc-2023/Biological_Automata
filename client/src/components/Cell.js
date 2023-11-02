import React from 'react';

function Cell({i, j, cellData, gameData}) {

  const generateCell = () => {

    const { _cant_bacterium, _cant_other } = gameData.games;
    const { spawn_bacterium, spawn_other, _game_mode} = gameData.games;
    const { _other, bacterias} = cellData;

    let game_mode;
    if (_game_mode === "Game_Mode.ANTIBIOTIC") {
      game_mode = 1;
    } else {
      game_mode = 2;
    }

    let cellClass = 'cell'
    if (spawn_bacterium && spawn_bacterium[0] === i && spawn_bacterium[1] === j && _cant_bacterium === 0) {
      cellClass = "spawnBacterium";
    } else if (spawn_bacterium && spawn_bacterium[0] === i && spawn_bacterium[1] === j && _cant_bacterium > 0) {
      cellClass = "spawnBacteriumActive";
    } else if (spawn_other && spawn_other[0] === i && spawn_other[1] === j && _cant_other === 0) {
      cellClass = "spawnOther";
    } else if (spawn_other && spawn_other[0] === i && spawn_other[1] === j && _cant_other > 0) {
      cellClass = "spawnOtherActive";
    }else if (_other !== 0) {
        if (game_mode === 1){
          cellClass = "antibiotic";
        } else {
          cellClass = "bacteriophage";
        }
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
    }

    return <td key={`${i}-${j}`} id={`${i}-${j}`} className={cellClass}></td>;
  }

  return generateCell();
}

export default Cell;
