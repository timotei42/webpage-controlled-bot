import './App.css';
import Button from "./Button";
import axios from 'axios';

const onClickPing = async (address: string) => {
  try {
    const response = await axios.get(address);
    console.log(response.data);
  } catch (error) {
    console.error('Error:', error);
  }
};
function App() {
  return (
    <>
      <h1>Robot Control</h1>
      <h2>Simple Movements</h2>
      <div className="container">
      <Button 
        border="none"
        color="yellow"
        height="40px"
        onClick={() => onClickPing('http://192.168.0.101/mov1')} 
        width="200px"
      >
        Movement 1-1
      </Button>
      <Button 
        border="dotted"
        color="yellow"
        height="40px"
        onClick={() => onClickPing('http://192.168.0.101/mov2')} 
        width="200px"
      >
        Movement 1-2
      </Button>
      <Button 
        border="none"
        color="yellow"
        height="40px"
        onClick={() => onClickPing('http://192.168.0.101/mov3')} 
        width="200px"
      >
        Movement 1-3
      </Button>
      <Button 
        border="none"
        color="yellow"
        height="40px"
        onClick={() => onClickPing('http://192.168.0.101/mov4')} 
        width="200px"
      >
        Movement 1-4
      </Button>
      </div>
      <h2>Combined Movements</h2>
      <div className="container">
      <Button 
        border="none"
        color="green"
        height="40px"
        onClick={() => {
          onClickPing('http://192.168.0.101/mov1');
          onClickPing('http://192.168.0.101/mov3');
        }}
        
        width="200px"
      >
        Movement 2-1
      </Button>
      <Button 
        border="none"
        color="green"
        height="40px"
        onClick={() => {
          onClickPing('http://192.168.0.101/mov2');
          onClickPing('http://192.168.0.101/mov4');
        }}
        
        width="200px"
      >
        Movement 2-2
      </Button>
      </div>
    </>
  );
}

export default App;
