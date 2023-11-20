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
    description:
      <>
      Estos microorganismos unicelulares puedes verlo como los enemigos principales del juego.
      <br />
      Son muy abundantes y pueden reproducirce rapidamente CUIDADO!.
    </>,
  },

  {
    name: 'Antibiotico',
    image: antibiotic,
    description: 'Combaten las infecciones bacterianas en personas y animales. Funcionan matando las bacterias o dificultando su crecimiento y multiplicación.',
  },

  {
    name: 'Bacteriofago',
    image: bacteriophageImage,
    description: 'Se aprovechan naturalmente de las bacterias al infectarlas y replicarse dentro de ellas hasta que estallan, matando a su huésped microbiano y reproduciendose en el proceso',
  },
];

function Index({ onViewChange }) {
  return (

    <div className="index-container">
      <div className='background'>
        <button className='buttonInit' id='user-init' onClick={() => onViewChange('register')}>Registrar</button>
        <button className='buttonInit' id='user-init' onClick={() => onViewChange('login')}>Login</button>


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

        <button className='buttonInit' onClick={() => onViewChange('config')}>Comenzar</button>
      </div>
    </div>
  );
}

export default Index;






