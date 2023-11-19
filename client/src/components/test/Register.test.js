import { render, screen, fireEvent } from '@testing-library/react'
import Register from '../Register';

describe("<Register />", () =>{
  let IngNickname;
  let IngEmail;
  let RepContraseña;
  let BotonRegistrar;
  
  beforeEach(() =>{
    render(<Register  />);
    IngNickname = screen.getByLabelText(/Nickname:/i);
    IngEmail = screen.getByLabelText(/Email:/i);
    RepContraseña = screen.getByLabelText(/Repetir contraseña:/i);
    BotonRegistrar = screen.getByRole('button', {name: /Registrar/i});

  
  });
  test("render the Register component",() =>{
    expect(IngNickname).toBeInTheDocument();
    expect(IngEmail).toBeInTheDocument();
    expect(RepContraseña).toBeInTheDocument();
    expect(BotonRegistrar).toBeInTheDocument();
  });
});