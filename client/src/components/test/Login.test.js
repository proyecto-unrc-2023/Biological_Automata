import { render, screen, fireEvent } from '@testing-library/react'
import userEvent from '@testing-library/user-event';
import Login from '../Login';

describe("<Login />", () =>{
 
  let BotonInic;
  let IngUsuario;
  let IngContraseña;
  let BotonVolver;
  
  beforeEach(() =>{
    render(<Login />);
    BotonInic = screen.getByRole('button', {name: /Iniciar Sesión/i });
    BotonVolver = screen.getByRole('button', {name: /Volver/i });
    IngContraseña = screen.getByLabelText(/Contraseña:/i);
    IngUsuario = screen.getByLabelText(/Usuario:/i);
  });

  test("render the Login component",() =>{  
    expect(IngUsuario).toBeInTheDocument();
    expect(IngContraseña).toBeInTheDocument();
    expect(BotonInic).toBeInTheDocument();
    expect(BotonVolver).toBeInTheDocument();

  });
});