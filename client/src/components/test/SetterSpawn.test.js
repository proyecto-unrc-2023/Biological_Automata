import { render, screen, fireEvent } from '@testing-library/react'
import SetterSpawn from '../Config/SetterSpawn';

describe("<SetterGameMode />", () =>{
  
  let BotonSiguiente;
  let BotonAnterior ;
  let Table;

  beforeEach(() =>{
    render(<SetterSpawn />);
    BotonSiguiente = screen.getByRole('button', {name: /Siguiente/i});
    BotonAnterior = screen.getByRole('button', {name:/Anterior/i});
    Table = screen.getByRole('table');
  });

  test("render the SetterGameMode component",() =>{
    expect(BotonSiguiente).toBeInTheDocument();
    expect(BotonAnterior).toBeInTheDocument();
  });

  test("capture board", () =>{
    expect(Table).toBeInTheDocument();
  });

});