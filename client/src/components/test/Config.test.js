import { render, screen} from '@testing-library/react'
import Config from '../Config';


describe("<Config />", () =>{
  test("render the Config component",() =>{
    render(<Config />);

    const BotonAnterior = screen.getByRole('button', {name : /Anterior/i});

    expect(BotonAnterior).toBeInTheDocument();
  });
});