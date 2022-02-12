import { Box, Button } from "@mui/material";
import TextField from "@mui/material/TextField";
import Grid from "@mui/material/Grid";
import Link from "@mui/material/Link";

import { DashboardLayout } from "../components/dashboard-layout";
import { useState } from "react";
import Typography from "@mui/material/Typography";
import { useRouter } from "next/router";

import Login from "../components/Login";

function Dashboard() {
  const router = useRouter();
  const [login, setLogin] = useState(null);
  const updateLogin = () => {
    setLogin({ address });
    console.log(login);
  };
  return (
    <Box
      sx={{
        marginTop: 8,
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
      }}
    >
      <Typography component="h1" variant="h5">
        원하시는 서비스를 선택해주세요
      </Typography>
      <Box sx={{ mt: 1 }}>
        <Button
          type="submit"
          fullWidth
          variant="contained"
          sx={{ mt: 3, mb: 2 }}
          onClick={() => router.push("/home/main")}
        >
          가정용
        </Button>
        <Button
          type="submit"
          fullWidth
          variant="contained"
          sx={{ mt: 3, mb: 2 }}
          onClick={() => router.push("/home/main")}
        >
          투자용
        </Button>
      </Box>
    </Box>
  );
}

Dashboard.getLayout = (page) => <DashboardLayout>{page}</DashboardLayout>;

export default Dashboard;
