import './App.css';
import {Button} from 'react-bootstrap';

function ledControl(pattern) {

    let data = new FormData()
    if (pattern === 'rainbow') {
        data.append("blink_pattern", 'rainbow')
    } else {
        data.append("blink_pattern", 'off')
    }

    const requestOptions = {
        method: 'POST',
        body: data,
        redirect: 'follow'
    }
    fetch('http://192.168.5.111:8000/api/blink-api/', requestOptions)
        .then(res => {
            if (res.ok) {
                return res.json()
            } else {
                return Promise.reject(res)
            }
        })
        .then(json => {
            console.log(json)
        }).catch((response) => {
        console.log(response)
    })

}

function App() {
    return (
        <div className="App">
            <div style={{padding: "10px", display: "flex", justifyContent: "center"}}>
                <div style={{display: "flex", flexDirection: "column"}}>
                    <Button
                        type={"button"}
                        size="lg"
                        style={{marginTop: "1rem"}}
                        onClick={event => {
                            event.preventDefault()
                            ledControl('rainbow')
                        }}>
                        Rainbow
                    </Button>
                </div>
            </div>
            <div style={{padding: "10px", display: "flex", justifyContent: "center"}}>
                <div style={{display: "flex", flexDirection: "column"}}>
                    <Button
                        type={"button"}
                        size="lg"
                        style={{marginTop: "1rem"}}
                        onClick={event => {
                            event.preventDefault()
                            ledControl('off')
                        }}>
                        Off
                    </Button>
                </div>
            </div>
        </div>
    );
}

export default App;
