import { useEffect } from "react";
import axios from "axios";

function App() {

  useEffect(() => {

    axios
      .get("http://127.0.0.1:8000/api/health/")
      .then((res) => {
        console.log("Django Response:", res.data);
      })
      .catch((err) => {
        console.log(err);
      });

  }, []);

  return (
    <div>
      <h1>VenturePulse</h1>
    </div>
  );
}

export default App;