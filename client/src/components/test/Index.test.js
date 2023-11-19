import { render, screen, fireEvent } from '@testing-library/react'
import Index from '../Index';

describe("<Index />", () =>{

  let BotonRegist;
  let BotonInic;
  let BotonComenzar;

  beforeEach(() =>{
    render(<Index  />);
    BotonRegist = screen.getByRole('button', {name: /Registrar/i});
    BotonInic = screen.getByRole('button', {name: /Login/i});
    BotonComenzar = screen.getByRole('button', {name:/Comenzar/i});
  });
  
  test("render the Index component",() =>{
    expect(BotonRegist).toBeInTheDocument();
    expect(BotonInic).toBeInTheDocument();
    expect(BotonComenzar).toBeInTheDocument();

  });
});