import Head from "next/head";
import { Box, Container, Grid } from "@mui/material";
import { TrafficByDevice } from "../../components/dashboard/traffic-by-device";
import { DashboardLayout } from "../../components/dashboard-layout";
import { Chart } from "src/components/dashboard/chart";

const Dashboard = () => (
  <>
    <Head>
      <title>Dashboard | Material Kit</title>
    </Head>
    <Box
      component="main"
      sx={{
        flexGrow: 1,
        py: 8,
      }}
    >
      <Container maxWidth={false}>
        <Grid container spacing={3}>
          <Grid item lg={8} md={12} xl={9} xs={12}>
            <Chart />
          </Grid>
          <Grid item lg={4} md={6} xl={3} xs={12}>
            <TrafficByDevice sx={{ height: "100%" }} />
          </Grid>
        </Grid>
      </Container>
    </Box>
  </>
);

Dashboard.getLayout = (page) => <DashboardLayout>{page}</DashboardLayout>;

export default Dashboard;
