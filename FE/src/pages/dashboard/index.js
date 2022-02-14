import Head from "next/head";
import { Box, Container, Grid } from "@mui/material";
import { DashboardLayout } from "../../components/dashboard-layout";
import { Chart } from "src/components/dashboard/chart";
import { CustomBarChart } from "src/components/dashboard/bar-chart";
import { TotalCustomers } from "src/components/dashboard/example-card";
const Dashboard = ({ powerGenrationResult, consumptionResult }) => (
  <>
    <Box
      component="main"
      sx={{
        flexGrow: 1,
        py: 8,
      }}
    >
      <Container maxWidth={false}>
        <Grid container spacing={3}>
          <Grid item lg={3} md={6} xl={3} xs={6}>
            <TotalCustomers />
          </Grid>
          <Grid item lg={3} md={6} xl={3} xs={6}>
            <TotalCustomers />
          </Grid>
          <Grid item lg={3} md={6} xl={3} xs={6}>
            <TotalCustomers />
          </Grid>
          <Grid item lg={3} md={6} xl={3} xs={6}>
            <TotalCustomers />
          </Grid>
          <Grid item lg={8} md={8} xl={8} xs={12}>
            <Chart
              title="현재 소비량 발전량 비교"
              allowtoggle="off"
              result={powerGenrationResult}
            />
          </Grid>
          <Grid item lg={4} md={4} xl={4} xs={12}>
            <CustomBarChart
              title="전기세 예상 절약 수치"
              result={powerGenrationResult}
            />
          </Grid>
          <Grid item lg={12} md={12} xl={12} xs={12}>
            <Chart
              title="전기 사용량"
              allowtoggle="on"
              result={powerGenrationResult}
            />
          </Grid>
        </Grid>
      </Container>
    </Box>
  </>
);

Dashboard.getLayout = (page) => <DashboardLayout>{page}</DashboardLayout>;

export default Dashboard;

export async function getServerSideProps() {
  const powerGenrationResult = await (
    await fetch(
      `http://localhost:3001/api/predict/power-generation?address=hihi`
    )
  ).json();

  const consumptionResult = await (
    await fetch(`http://localhost:3001/api/predict/consumption?address=hihi`)
  ).json();

  return {
    props: {
      powerGenrationResult,
      consumptionResult,
    },
  };
}
