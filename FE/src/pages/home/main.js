import { useState } from "react";
import Login from "../../components/Login";

function Dashboard() {
  const [login, setLogin] = useState(null);
  const updateLogin = () => {
    setLogin({ address });
  };
  return (
    <>
      <Login updateLogin={updateLogin} />
    </>
  );
}

export default Dashboard;
