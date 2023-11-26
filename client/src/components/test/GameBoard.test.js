import { render, screen, fireEvent } from '@testing-library/react'
import Create_Game from '../GameBoard';

describe("<Create_Game />", () =>{

  let table;
  let BarraVelocidad;
  beforeEach(() =>{
    render(<Create_Game handleStartGame={true} />);
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