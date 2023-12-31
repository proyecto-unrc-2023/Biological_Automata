import React from 'react';
import '../css/Index.css'
import antibiotic from '../images/pill.gif';
import bacteriophageImage from '../images/bacteriophague.png';
import bacteriumLogo from '../images/BacteriumStrong.gif'
import bacterium from '../images/BacteriumNormal.gif'

const creatures = [
  {
    name: 'Bacteria',
    image: bacterium,
    description: 'Estos microorganismos unicelulares puedes verlo como los enemigos principales del juego. Son muy abundantes y pueden reproducirce rapidamente CUIDADO!'
  },

  {
    name: 'Antibiótico',
    image: antibiotic,
    description: 'Combaten las infecciones bacterianas en personas y animales. Funcionan matando las bacterias o dificultando su crecimiento y multiplicación.',
  },

  {
    name: 'Bacteriófago',
    image: bacteriophageImage,
    description: 'Se aprovechan naturalmente de las bacterias al infectarlas y replicarse dentro de ellas hasta que estallan, matando a su huésped microbiano y reproduciendose en el proceso.',
  },
];



function Index({ componentChange, id, setId }) {
  if (!id) {
    const sessionStorageId = sessionStorage.getItem('userId');
    const localStorageId = localStorage.getItem('userId');

    if (sessionStorageId) {
      setId(sessionStorageId);
    } else if (localStorageId) {
      setId(localStorageId);
    }
  }

  const isLoggedIn = id || sessionStorage.getItem('userId') || localStorage.getItem('userId');
  const canStartGame = id !== null;


  const handleLogoutUser = () => {
    if (isLoggedIn) {
      if (localStorage.getItem('userId')) {
        localStorage.removeItem('userId');
      } else {
        sessionStorage.removeItem('userId');
      }
      setId(null);
    } else {
      console.error('Error: No se ha iniciado sesión en ninguna cuenta');
    }
  };

  const handleStartGame = () => {
    if (canStartGame) {
      componentChange('config');
    } else {
      console.error('Error: No se puede comenzar el juego, no se ha iniciado sesión');
    }
  };

  return (
    <div className="index-container">
      <div className='background'>
        {!isLoggedIn && (
          <div>
            <button className='buttonInit' id='user-init' onClick={() => componentChange('register')}>Registrar</button>
            <button className='buttonInit' id='user-init' onClick={() => componentChange('login')}>Login</button>
          </div>
        )}

        {isLoggedIn && (
          <button className='buttonInit' id='user-init' onClick={() => handleLogoutUser()}>Logout</button>
        )}

        <img src={bacteriumLogo} alt="Logo" className="logo" />
        <h1 className="titleInit">Biological Automata</h1>

        <div className="creature-container">
          {creatures.map((creature, index) => (
            <div key={index} className="creature-card">
              <img src={creature.image} alt={creature.name} className="creature-image" />
              <h2>{creature.name}</h2>
              <p>{creature.description}</p>
            </div>
          ))}
        </div>

        <button className='buttonInit' onClick={handleStartGame}>Comenzar</button>
      </div>
    </div>
  );
}

export default Index;
