import { Box, Container, Grid } from "@mui/material";
import { DashboardLayout } from "../../components/dashboard-layout";
import { Chart } from "src/components/dashboard/chart";
import { CustomBarChart } from "src/components/dashboard/bar-chart";
import { DashboardCard } from "src/components/dashboard/card";
import { useRouter } from "next/router";
import { useState } from "react";
import AttachMoneyOutlinedIcon from "@mui/icons-material/AttachMoneyOutlined";
import BoltOutlinedIcon from "@mui/icons-material/BoltOutlined";
import AirOutlinedIcon from "@mui/icons-material/AirOutlined";
function Dashboard({
  currentResult,
  estimatedElectricitySaving,
  electricityUsage,
  predictGeneration,
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
            {isLogin ? (
              <>
                <Grid item lg={3} md={6} xl={3} xs={6}>
                  <DashboardCard
                    title="이번 달 총 발전량"
                    content={"120kWh"}
                    icon={<BoltOutlinedIcon fontSize="large" />}
                  />
                </Grid>
                <Grid item lg={3} md={6} xl={3} xs={6}>
                  <DashboardCard
                    title="이번 달 총 소비량"
                    content={"161kWh"}
                    icon={<AttachMoneyOutlinedIcon fontSize="large" />}
                  />
                </Grid>
                <Grid item lg={3} md={6} xl={3} xs={6}>
                  <DashboardCard
                    title="이번 달 총 전기료"
                    content={"13,500원"}
                    icon={<BoltOutlinedIcon fontSize="large" />}
                  />
                </Grid>
                <Grid item lg={3} md={6} xl={3} xs={6}>
                  <DashboardCard
                    title="이번 달 총 발전수익"
                    content={"1,600원"}
                    icon={<AttachMoneyOutlinedIcon fontSize="large" />}
                  />
                </Grid>
              </>
            ) : (
              <>
                <Grid item lg={6} md={6} xl={6} xs={6}>
                  <DashboardCard
                    title="절감 가능한 금액"
                    content={"1,600원"}
                    icon={<AttachMoneyOutlinedIcon fontSize="large" />}
                  />
                </Grid>
                <Grid item lg={6} md={6} xl={6} xs={6}>
                  <DashboardCard
                    title="탄소 중립 기여도"
                    content={"설치 할 시 약 15% 상승합니다."}
                    icon={<AirOutlinedIcon fontSize="large" />}
                  />
                </Grid>
              </>
            )}
            <Grid item lg={8} md={8} xl={8} xs={12}>
              {isLogin ? (
                <Chart
                  title="우리집 소비량 발전량"
                  allowtoggle="off"
                  result={currentResult}
                />
              ) : (
                <Chart
                  title="우리집 예상 소비량 발전량"
                  allowtoggle="on"
                  result={electricityUsage}
                />
              )}
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
                  allowtoggle="off"
                  result={predictGeneration}
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

const getMonthData = (consumptionResult, powerGenrationResult) => {
  const predictConsumption = consumptionResult.predict.map((monthData) => {
    return monthData.value.reduce((acc, cur) => acc + cur);
  });

  const predictPowerGeneration = powerGenrationResult.predict.map(
    (monthData) => {
      return monthData.value.reduce((acc, cur) => acc + cur);
    }
  );

  const data = predictConsumption.map((item, idx) => {
    const { date } = consumptionResult.predict[idx];

    return {
      name: `${date.substring(5, date.length)}월`,
      소비량: item,
      발전량: predictPowerGeneration[idx],
    };
  });

  return data;
};

const getDayData = (consumptionResult, powerGenrationResult) => {
  const predictConsumption = consumptionResult.predict[11].value;
  const predictPowerGeneration = powerGenrationResult.predict[11].value;

  const data = predictConsumption.map((item, idx) => {
    return {
      name: `${idx + 1}일`,
      소비량: item,
      발전량: predictPowerGeneration[idx],
    };
  });

  return data;
};

const createCurrentResult = (consumption, powerGenration) => {
  return consumption.value.map((item, idx) => {
    return {
      name: `${idx + 1}일`,
      소비량: item,
      발전량: powerGenration.value[idx],
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

const createPredictGeneration = (powerGenration) => {
  return powerGenration.map((item) => {
    const { date } = item;
    return {
      name: `${date.substring(5, date.length)}월`,
      발전량: item.value.reduce((acc, cur) => acc + cur),
    };
  });
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
        consumptionResult.current[1],
        powerGenrationResult.current[1]
      ),
      //전기세 예상 절약 수치
      estimatedElectricitySaving: createElectricitySaving(
        powerGenrationResult.current[powerGenrationResult.current.length - 2],
        powerGenrationResult.predict[0]
      ),
      //전기 사용량
      electricityUsage: {
        days: getDayData(consumptionResult, powerGenrationResult),
        months: getMonthData(consumptionResult, powerGenrationResult),
      },
      //예상 발전량
      predictGeneration: createPredictGeneration(powerGenrationResult.predict),
    },
  };
}
