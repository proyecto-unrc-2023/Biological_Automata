import { render, screen, fireEvent } from '@testing-library/react'
import SetterSpawn from '../Config/SetterSpawn';

describe("<SetterGameMode in the game mode Antibióticoti/>", () =>{
  
  let BotonSiguiente;
  let BotonAnterior ;
  let BotonSpawnBac;
  let BotonSpawnAnti;
  let Table;


  beforeEach(() =>{
    render(<SetterSpawn gameMode ={1} />);
    BotonSiguiente = screen.getByRole('button', {name: /Siguiente/i});
    BotonAnterior = screen.getByRole('button', {name:/Anterior/i});
    BotonSpawnBac = screen.getByRole('button', {name:/Bacteria/i});
    BotonSpawnAnti = screen.getByRole('button', {name:/Antibiótico/i});

    Table = screen.getByRole('table');
  });

  test("render the SetterGameMode component",() =>{
    expect(BotonSiguiente).toBeInTheDocument();
    expect(BotonAnterior).toBeInTheDocument();
    expect(BotonSpawnBac).toBeInTheDocument();
    expect(BotonSpawnAnti).toBeInTheDocument();
  });

  test("capture board", () =>{
    expect(Table).toBeInTheDocument();
  });

});

describe("<SetterGameMode in the game mode Bacteriófago />", () =>{
  
  let BotonSiguiente;
  let BotonAnterior ;
  let BotonSpawnBac;
  let BotonSpawnVir;
  let Table;


  beforeEach(() =>{
    render(<SetterSpawn gameMode ={2} />);
    BotonSiguiente = screen.getByRole('button', {name: /Siguiente/i});
    BotonAnterior = screen.getByRole('button', {name:/Anterior/i});
    BotonSpawnBac = screen.getByRole('button', {name:/Bacteria/i});
    BotonSpawnVir = screen.getByRole('button', {name:/Bacteriófago/i});

    Table = screen.getByRole('table');
  });

  test("render the SetterGameMode component",() =>{
    expect(BotonSiguiente).toBeInTheDocument();
    expect(BotonAnterior).toBeInTheDocument();
    expect(BotonSpawnBac).toBeInTheDocument();
    expect(BotonSpawnVir).toBeInTheDocument();
  });

  test("capture board", () =>{
    expect(Table).toBeInTheDocument();
  });

});