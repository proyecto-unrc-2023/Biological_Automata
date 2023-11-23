import React, { useState } from 'react';
import '../css/Register-Login.css';

function Login({ onViewChange, setId }) {
  const [nickname, setNickname] = useState('');
  const [password, setPassword] = useState('');
  const [stayLoggedIn, setStayLoggedIn] = useState(false); // Nuevo estado para mantener la sesión

  const handleUserLogin = () => {
    if (nickname !== '' && password !== '') {
      const data = {
        nickname: nickname,
        password: password,
      };

      fetch(`http://localhost:5000/game/login`, {
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
          return response.json();
        })
        .then((data) => {
          const userId = data.user.id;
          //Si elije no cerrar session lo guarda en el localStorage
          if (stayLoggedIn) {
            localStorage.setItem('userId', userId);
          } else {
            sessionStorage.setItem('userId', userId);
          }
          setId(userId);
          onViewChange('index');
        })
        .catch((error) => {
          console.error('Hubo un error al enviar los datos', error);
        });
    } else {
      console.error('Error: Por favor, completa todos los campos');
    }
  };

  return (
    <div className='register-content'>
      <div className='background'>
        <div className='content-form'>
          <label>
            Usuario:
            <input
              type='text'
              value={nickname}
              onChange={(e) => setNickname(e.target.value)}
            />
          </label>
          <label>
            Contraseña:
            <input
              type='password'
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
          </label>

          <button className='buttonInit' onClick={handleUserLogin}>
            Iniciar Sesión
          </button>

          <button className='buttonInit' onClick={() => onViewChange('index')}>
            Volver
          </button>

          {/* Botón para mantener la sesión */}
          <label>
            <input
              type='checkbox'
              checked={stayLoggedIn}
              onChange={() => setStayLoggedIn(!stayLoggedIn)}
            />
            No cerrar sesión
          </label>
        </div>
      </div>
    </div>
  );
}

export default Login;

