import { render, screen, fireEvent } from '@testing-library/react'
import SetterGameMode from '../Config/SetGameMode';

describe("<SetterGameMode />", () =>{

  let BotonSiguiente;
  let BotonAnterior ;
  
  beforeEach(() =>{
    render(<SetterGameMode />);
    BotonSiguiente = screen.getByRole('button', {name: /Siguiente/i});
    BotonAnterior = screen.getByRole('button', {name:/Anterior/i});
  });
   
  test("render the SetterGameMode component",() =>{
    expect(BotonSiguiente).toBeInTheDocument();
    expect(BotonAnterior).toBeInTheDocument();
  });

});