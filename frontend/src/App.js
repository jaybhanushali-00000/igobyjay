import React, {useState} from "react";
import './app.css';
import classes from './app.css';
import { Auth } from "./Auth";
import { Calculator } from "./Calculator";

function App() {  
  const [a,setA] = useState(1);

  const toggle_state =(formNumber) => {
    setA(formNumber);
  }

  return(
    <>
    <div>
      { 
      a===1 ? <Auth onFormSwitch={toggle_state} /> : <Calculator/>
      }
    </div>
    </>
  ) }
export default App;
