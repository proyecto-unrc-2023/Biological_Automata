import React, { useState } from 'react';
import '../css/Register-Login.css';

function Register({ onViewChange}) {
  const [nickname, setNickname] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [repPassword, setRepPassword] = useState('');

  const handleRegisterUser = () => {
    if (nickname !== '' && email !== '' && password !== '' && repPassword !== '') {
      if (password !== repPassword) {
        console.error('Error: Las contraseñas no coinciden');
        return;
      }

      const data = {
        nickname: nickname,
        email: email,
        password: password,
        repPassword: repPassword,
      };

      fetch(`http://localhost:5000/game/register`, {
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
              Nickname:
              <input
                type='text'
                value={nickname}
                onChange={(e) => setNickname(e.target.value)}
              />
            </label>
            <label>
              Email:
              <input
                type='email'
                value={email}
                onChange={(e) => setEmail(e.target.value)}
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
            <label>
              Repetir contraseña:
              <input
                type='password'
                value={repPassword}
                onChange={(e) => setRepPassword(e.target.value)}
              />
            </label>
            <button className='buttonInit' onClick={handleRegisterUser}>
              Registrar
            </button>

            <button className='buttonInit' onClick={() => onViewChange('index')}>Volver</button>
          </div>
        </div>
      </div>
  );
}

export default Register;
