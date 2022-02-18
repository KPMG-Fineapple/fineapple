import { Box, Container, Grid } from "@mui/material";
import { DashboardLayout } from "../../components/dashboard-layout";
import { Chart } from "src/components/dashboard/chart";
import { CustomBarChart } from "src/components/dashboard/bar-chart";
import { TotalCustomers } from "src/components/dashboard/example-card";
import { useRouter } from "next/router";
import { useState } from "react";
function Dashboard({
  currentResult,
  estimatedElectricitySaving,
  electricityUsage,
}) {
  const router = useRouter();
  const [isLogin, setIsLogin] = useState(
    router.query.isLogin === "true" ? true : false
  );
  return (
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
                result={currentResult}
              />
            </Grid>
            <Grid item lg={4} md={4} xl={4} xs={12}>
              <CustomBarChart
                title="우리집 전기료 절감액"
                result={estimatedElectricitySaving}
              />
            </Grid>
            {isLogin ? (
              <Grid item lg={12} md={12} xl={12} xs={12}>
                <Chart
                  title="우리 집 미래 발전량"
                  allowtoggle="on"
                  result={electricityUsage}
                />
              </Grid>
            ) : (
              <></>
            )}
          </Grid>
        </Container>
      </Box>
    </>
  );
}

Dashboard.getLayout = (page) => <DashboardLayout>{page}</DashboardLayout>;

export default Dashboard;

const getMonthData = (result) => {
  const currentMonthData = result.current.map((monthData) => {
    return monthData.value.reduce((acc, cur) => acc + cur);
  });

  const predictMonthData = result.predict.map((monthData) => {
    return monthData.value.reduce((acc, cur) => acc + cur);
  });

  const data = currentMonthData.map((item, idx) => {
    const { date } = result.current[idx];

    return {
      name: `${date.substring(5, date.length)}월`,
      현재: item,
      예측: predictMonthData[idx],
    };
  });

  return data;
};

const getDayData = (result) => {
  const currentDayData = result.current[11].value;
  const predictDayData = result.predict[11].value;

  const data = currentDayData.map((item, idx) => {
    return {
      name: `${idx + 1}일`,
      현재: item,
      예측: predictDayData[idx],
    };
  });

  return data;
};

const createCurrentResult = (consumption, powerGenration) => {
  return consumption.map((item, idx) => {
    const { date } = item;
    return {
      name: `${date.substring(5, date.length)}월`,
      소비량: item.value.reduce((acc, cur) => acc + cur),
      발전량: powerGenration[idx].value.reduce((acc, cur) => acc + cur),
    };
  });
};

const createElectricitySaving = (cur, next) => {
  const curSum = cur.value.reduce((acc, cur) => acc + cur);
  const nextSum = next.value.reduce((acc, cur) => acc + cur);

  return {
    name: "설치 전과 설치 후 비교",
    "설치 전": curSum,
    "설치 후": nextSum,
  };
};

export async function getServerSideProps() {
  const powerGenrationResult = await (
    await fetch(`http://localhost:3001/api/predict/power-generation`)
  ).json();

  const consumptionResult = await (
    await fetch(`http://localhost:3001/api/predict/consumption`)
  ).json();

  return {
    props: {
      //현재 소비량 발전량 비교
      currentResult: createCurrentResult(
        consumptionResult.current,
        powerGenrationResult.current
      ),
      //전기세 예상 절약 수치
      estimatedElectricitySaving: createElectricitySaving(
        powerGenrationResult.current[powerGenrationResult.current.length - 2],
        powerGenrationResult.predict[0]
      ),
      //전기 사용량
      electricityUsage: {
        days: getDayData(consumptionResult),
        months: getMonthData(consumptionResult),
      },
    },
  };
}
