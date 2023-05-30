import React, {useState} from "react";
import './app.css';
import classes from './app.css';

function App() {

  let ENDPOINT ="https://igobyjay-1-jaybhanushali-00000.vercel.app/";
const[num1,setNum1] = useState();
const[num2,setNum2] = useState();
const[num3,setNum3] = useState();
const[num4,setNum4] = useState();
const[tot,setTot] = useState();

const[multi,setMulti] = useState();

const fetchApiData = async(url) => {
  var data =null;
  var result = null;
    try {
      const response = await fetch(url);
      data = await response.json();
      result = data["value"];
     console.log(result);
        } 
    catch (error) {console.log(error);}
    return (result);
  };

  



function handle_SUM_click(){
  let API = ENDPOINT+'fibonacci/'+num1+'_'+num2+"_"+num3+'_'+num4;
  const data_1 = fetchApiData(API);
  data_1.then(function(result){
   // console.log(result);
    setTot(result);
  })
  
  //setTot(data_1);
}



function handle_multi_click(){
  let API = ENDPOINT+'multiplier/'+num1+'_'+num2;
  const data_2 = fetchApiData(API);
  data_2.then(function(result){
    setMulti(result);
  })
}

  return (
   <> 
   <div>The Amazing Calculator</div>{'\n'}
   <div className="meow">
   <div className="meow"><label>Number1</label>{'\n'}
   <input type="int" name="num1" placeholder="number1" onChange={(event)=>
    {
      setNum1(event.target.value)
    }}></input>{'\n'}</div>
   <div className="meow"><label>Number2</label>
   <input type='int' name="num2" placeholder="number2" onChange={(meow)=>
    {
      setNum2(meow.target.value)
    }}></input></div>

<div className="meow"><label>Number3</label>
   <input type='int' name="num2" placeholder="number3" onChange={(meow)=>
    {
      setNum3(meow.target.value)
    }}></input></div>

<div className="meow"><label>Number4</label>
   <input type='int' name="num2" placeholder="number4" onChange={(meow)=>
    {
      setNum4(meow.target.value)
    }}></input></div>


   <div className="meow"><button onClick={handle_SUM_click}>Fibonacci</button>
    <input type="text" value={tot}></input></div>

    <div className="meow">
      <button onClick = {handle_multi_click}>Multiplication</button>
      <input type="text" value={multi}></input> 
    </div>
    </div>
  </>
  )
  }
export default App;
