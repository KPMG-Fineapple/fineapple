import { DashboardLayout } from "../../components/dashboard-layout";
import { useState } from "react";
import Login from "../../components/Login";

function Dashboard() {
  const [login, setLogin] = useState(null);
  const updateLogin = () => {
    setLogin({ address });
    console.log(login);
  };
  return (
    <>
      <Login updateLogin={updateLogin} />
    </>
  );
}

Dashboard.getLayout = (page) => <DashboardLayout>{page}</DashboardLayout>;

export default Dashboard;
