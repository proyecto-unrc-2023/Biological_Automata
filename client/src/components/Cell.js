import React from 'react';

function Cell({i, j, cellData, gameData}) {

  const generateCell = () => {

    const { _antibiotics, _cant_bacteriophage, bacterias } = cellData;
    const { _cant_bacterium, _cant_other } = gameData.games;
    const { spawn_bacterium, spawn_other } = gameData.games;


    let cellClass = 'cell'
    if (spawn_bacterium && spawn_bacterium[0] === i && spawn_bacterium[1] === j && _cant_bacterium === 0) {
      cellClass = "spawnBacterium";
    } else if (spawn_bacterium && spawn_bacterium[0] === i && spawn_bacterium[1] === j && _cant_bacterium > 0) {
      cellClass = "spawnBacteriumActive";
    } else if (spawn_other && spawn_other[0] === i && spawn_other[1] === j && _cant_other === 0) {
      cellClass = "spawnOther";
    } else if (spawn_other && spawn_other[0] === i && spawn_other[1] === j && _cant_other > 0) {
      cellClass = "spawnOtherActive";
    }else if (_cant_bacteriophage !== 0) {
        cellClass = "bacteriophage";
    } else if (_antibiotics !== 0) {
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
    }

    return <td key={`${i}-${j}`} id={`${i}-${j}`} className={cellClass}></td>;
  }

  return generateCell();
}

export default Cell;
