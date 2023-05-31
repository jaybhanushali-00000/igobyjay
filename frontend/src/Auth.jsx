import React, { useState } from "react";
import { Verified } from "./Verified";
import { Not_verified } from "./Not_verified";
import { Calculator } from "./Calculator";

export const Auth=(props ) => {

    let ENDPOINT ="https://igobyjay-1-sd0ezwrri-jaybhanushali-00000.vercel.app/";
    const [user_id,setUSR] = useState();
    const [password,setPass] = useState();
    const [b,setB] = useState(1);
    const [ver,setVer] = useState();

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

    const handle_auth = async(e) => {
        //e.preventDefault();
        let auth = ENDPOINT+'auth/'+user_id+'_'+password;
        const data = (fetchApiData(auth));
        data.then(function(result){
                  setVer(result);
                  ver === 1 ? props.onFormSwitch(0): props.onFormSwitch(1)
        })
    }


    return (
        <>
         <div>
      <input value={user_id} type= "text" name="user_id" placeholder="user-id" autoComplete="off" onChange={(e) => {setUSR(e.target.value)}}/>
      <input  value={password} type="password" name="password"placeholder="password" autoComplete="off" onChange={(e) => {setPass(e.target.value)}}/>

      <button onClick={handle_auth}>Authentify</button>
    </div>
    </>
    )
}
