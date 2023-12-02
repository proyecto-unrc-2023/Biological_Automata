import React, { useEffect, useState } from 'react';
import '../css/Winner.css'; 

const Winner = ({ winnerType }) => {
  const [visible, setVisible] = useState(false);

  useEffect(() => {
    // Espera un breve momento antes de cambiar la opacidad para permitir el efecto de fade-in
    const timeoutId = setTimeout(() => {
      setVisible(true);
    }, 100);

    // Limpia el temporizador al desmontar el componente
    return () => clearTimeout(timeoutId);
  }, []); // El segundo argumento vacío significa que se ejecutará solo en la montura del componente

  const getImageSource = () => {
    switch (winnerType) {
      case 'Game_Winner.BACTERIUM':
        return './image/GameOver3.png';
      case 'Game_Winner.OTHER':
        return './image/YouWin.png';
      default:
        return '';
    }
  };

  return (
    <img
      className={`winning-image ${visible ? 'show' : ''}`}
      src={getImageSource()}
      alt="Winner"
    />
  );
};

export default Winner;