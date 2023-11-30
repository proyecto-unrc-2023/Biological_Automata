import { render, screen, fireEvent } from '@testing-library/react'
import SetterGameMode from '../Config/SetGameMode';

describe("<SetterGameMode />", () =>{

  let BotonSiguiente;
  let BotonAnterior ;
  let BotonAnti;
  let BotonVir;
  
  beforeEach(() =>{
    render(<SetterGameMode />);
    BotonSiguiente = screen.getByRole('button', {name: /Siguiente/i});
    BotonAnterior = screen.getByRole('button', {name:/Anterior/i});
    BotonAnti = screen.getByRole('button', {name:/Antibiótico/i});
    BotonVir = screen.getByRole('button', {name:/Bacteriófago/i});

  });
   
  test("render the SetterGameMode component",() =>{
    expect(BotonSiguiente).toBeInTheDocument();
    expect(BotonAnterior).toBeInTheDocument();
    expect(BotonAnti).toBeInTheDocument();
    expect(BotonVir).toBeInTheDocument();

  });

});