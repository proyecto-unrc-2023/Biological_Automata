import { render, screen, fireEvent } from '@testing-library/react'
import Register from '../Register';

describe("<Register />", () =>{
  let IngNickname;
  let IngEmail;
  let RepContraseña;
  let IngContraseña;
  let BotonRegistrar;
  
  beforeEach(() =>{
    render(<Register  />);
    IngNickname = screen.getByLabelText(/Nickname:/i);
    IngEmail = screen.getByLabelText(/Email:/i);
    RepContraseña = screen.getByLabelText(/Repetir contraseña:/i);
    IngContraseña = screen.getByLabelText('Contraseña:');
    BotonRegistrar = screen.getByRole('button', {name: /Registrar/i});

  
  });
  test("render the Register component",() =>{
    expect(IngNickname).toBeInTheDocument();
    expect(IngEmail).toBeInTheDocument();
    expect(RepContraseña).toBeInTheDocument();
    expect(BotonRegistrar).toBeInTheDocument();
    expect(IngContraseña).toBeInTheDocument();
  });
});