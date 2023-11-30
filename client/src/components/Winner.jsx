import React from 'react';
import '../css/Winner.css'; 

const Winner = ({ winnerType }) => {
  const getImageSource = () => {
    switch (winnerType) {
      case 'Game_Winner.BACTERIUM':
        return './image/GameOver.png';
      case 'Game_Winner.OTHER':
        return './image/YouWin.png';
      default:
        return '';
    }
  };

  return (
    <img className={`winning-image show`} src={getImageSource()} />
    );
};

export default Winner;