import { useEffect } from "react"

function App(){ 

    function redirect(e){
      console.log(e.target)
      fetch("http://127.0.0.1:5560/")
       .then(resp => resp.text())
       .then(data => console.log(data))
    }

    function funcCommand(e){
      console.log(e.target)
      fetch("http://127.0.0.1:5560/command")
       .then(resp => resp.text())
       .then(data => console.log(data))
    }
  
  return <div>
            <h1>React</h1>
            <button onClick={ (e) => redirect(e)} className="redirect">Button</button>
            <button onClick={ (e) => funcCommand(e)} className="redirect">Command</button>
         </div>
}

export default App