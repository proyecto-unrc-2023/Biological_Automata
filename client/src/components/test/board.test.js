import { render, screen, fireEvent } from '@testing-library/react'
import Create_board from '../board';

describe("<Create_board />", () =>{

  let table;
  let BarraVelocidad;
  beforeEach(() =>{
    render(<Create_board handleStartGame={true} />);
    BarraVelocidad = screen.getByText(/Velocidad:/i);
    table = screen.getByRole('table');
  });


  test("render the Create_board component",() =>{
    expect(BarraVelocidad).toBeInTheDocument();
  });

  test("capture board", () =>{
    expect(table).toBeInTheDocument();
  });

});